from urllib import parse 
def fileFilter(fullpath,name,isdir):#返回了false的条目会被过滤掉
	if isdir:return 1
	if '  0' in name:return 0
	if not ('.py' in name):
		return 0
	return 1