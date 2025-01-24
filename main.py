import sys
import os
from flask import Flask,session,request
import mimetypes
from urllib import parse 

app = Flask(__name__)
app.secret_key='secrets.token_hex()'

@app.after_request
def set_headers(response):
	if (request.path[:3]=='/@/')&(_nocache^1):
		response.headers['Cache-Control']='public, max-age=432000'
	else:
		response.headers['Cache-Control']='no-store;no-cache;max-age=0;must-revalidate'
		response.headers['Pragma']='no-cache'
	return response

@app.route('/')
def nopath():
	return index('/')

@app.route('/@/<path:file>')
def at(file):
	path=os.path.abspath(os.getcwd()+'/'+file)
	headers=[('Content-Type',mimetypes.guess_type(path.split('/')[-1])[0])]
	
	return sendfile(path,headers)

def keyReplace(data,la,lb):
	i=0
	for e in la:
		data=data.replace(la[i],lb[i])
		i+=1
	return data


@app.route('/<path:pth>')
def index(pth):
	global _template,_404
	fullPath = os.path.abspath(f'{_dir}/{pth}')
	print(fullPath,f'{_dir}/{pth}')
	isdir = os.path.isdir(fullPath)
	if _single:
		if isdir:
			if pth == '':
				pth = '/'
			elif pth[0] != '/':
				pth = '/' + pth
	
			cd = '/'.join(pth.split('/')[:-1]) or '/'
			_l = [
				f'<h1>Directory listing for {os.path.abspath(_dir + pth)}</h1>',
				f"<a href='{cd}'>CD..</a>",
				'<hr><ul>'
			]
	
			for e in os.listdir(fullPath):
				if pth == '/':
					pth = ''
				e_encoded = urllib.parse.quote(e) if _encode else e
				_l.append(f'<li><a href="{pth}/{e_encoded}">{e}</a></li>')
	
			_l.append('</ul><hr>')
			return _template.replace('rep', ''.join(_l))
		else:
			return sendfileEx(fullPath)
	if _active:
		loadBaseFile()
	if isdir:
		
		value,replace=[],[]
		if '${#CD}' in _template:
			value+=['${#CD}']
			if ('/' in pth)^1:replace+=['/']
			else:replace+=['/'.join(('/'+pth).split('/')[:-1])]
		if '${#FULLPATH}' in _template:
			value+=['${#FULLPATH}']
			replace+=[fullPath]
		if '${#PATH}' in _template:
			value+=['${#PATH}']
			replace+=[pth]
		if '${#LIST_' in _template:
			value+=['${#LIST_NAME}','${#LIST_TYPE}','${#LIST_LEN}']
			temp_name,temp_type=[],[]
			for e in os.listdir(fullPath):
				cur_isdir=os.path.isdir(fullPath+'/'+e)
				exec(_filter)
				ev=eval(f'fileFilter("{parse.quote(fullPath)}","{parse.quote(e)}","{cur_isdir}")')
				if ev^1:continue
				temp_name+=[urllib.parse.quote(e) if _encode else e]
				if cur_isdir:temp_type+='1'
				else:temp_type+='0'
			replace+=['\n'.join(temp_name)]
			replace+=['\n'.join(temp_type)]
			replace+=[str(len(temp_name))]

		return keyReplace(_template,value,replace),[('Content-Type','text/html')]
	else:
		return sendfileEx(fullPath)
		
def sendfile(path,headers):
	if os.path.exists(path)^1:
		return _404,404,[('Content-Type','text/html')]
	try:
		file=open(path,'rb')
		data=file.read()
		file.close()
		return data,headers
	except:
		return _404,404,[('Content-Type','text/html')]

def sendfileEx(path):
	return sendfile(path,[('Content-Type',mimetypes.guess_type(path)[0])])
def loadBaseFile():
	global _template,_404,_filter
	with open('template.html','rb') as f:_template=f.read().decode()
	with open('404.html','rb') as f:_404=f.read().decode()
	with open('filter.py','rb') as f:_filter=f.read()
	

if __name__ == '__main__':
	global _dir,_active,_encode,_nocache
	_ip='0.0.0.0'
	_port=8000
	_active=0
	_dir=os.getcwd()
	_encode=0
	_nocache=0
	_single=0
	k=0
	for i in sys.argv:
		k+=1
		if i=='--bind' or i=='-b':_ip=sys.argv[k]
		if i=='--dir' or i=='-d':_dir=sys.argv[k]
		if i=='--active' or i=='-a':_active=1
		if i=='--encode' or i=='-e':_encode=1
		if i=='--nocache' or i=='-n':_nocache=1
		if i=='--single' or i=='-s':_single=1
		if i == '--help' or i == '-h':
			print('[port] --bind [ip] --dir [directory] --active --encode --nocache --single')
			print('[port=8000]: The port to listen on.')
			print('--bind/-b [ip=0.0.0.0]: The specific IP address to bind to.')
			print('--dir/-d [directory=.]: The directory to serve files from.')
			print('--active/-a: Actively reload "template.html" and "404.html" on each request.')
			print('--encode/-e: Encode the path (use this when characters are displayed incorrectly).')
			print('--nocache/-n: Add the "Cache-Control: no-cache" HTTP header to each response.')
			print('--single/-s: Serve a dynamically generated page.')
			sys.exit()
		if i.isdigit():
			_port=int(i)

	if _single^1 :
		loadBaseFile()
	else:
		_404='<h1>404 Not Found</h1>'
		_template='<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"><title>ExploreR</title></head><body>rep</body></html>'

	app.run(host=_ip,port=_port,debug=True)
