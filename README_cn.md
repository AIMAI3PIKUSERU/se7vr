# se7vr
[English](https://github.com/AIMAI3PIKUSERU/se7vr/blob/master/README.md)
#### 介绍
这是一个基于Python的轻量,强自定义性的服务器程序

#### 额外的库
本程序基于flask 库,安装方式:

```shell
pip install flask
```

#### 使用说明

在终端输入`python main.py`即可运行,浏览器输入[127.0.0.1:8000](http://127.0.0.1:8000)即可访问
仓库中的main.py以外的文件全都不是必须的,只是给美化留了一条后路
如果你想体验 `python -m http.server`的界面,输入`python main.py -s`即可
键入 --help/-h 参数以查看帮助,其输出如下

|toggle|/|
|------|-|
| --bind/-b   |[ip=0.0.0.0]: The specific IP address to bind to.|
| --dir/-d    |[directory=.]: The directory to serve files from.|
| --active/-a |Actively reload "template.html", "404.html"and "filter.py" on each request.|
| --encode/-e |Encode the path (use this when characters are displayed incorrectly).|
| --nocache/-n|Add the "Cache-Control: no-cache" HTTP header to each response.|
| --single/-s |Serve a dynamically generated page.|

|翻译|
|----|
|你要绑定到的具体 IP 地址。|
|用于提供文件服务的目录。|
|在每次请求时重新加载 "template.html"、"404.html" 和 "filter.py"。|
|对路径进行编码（字符显示不正确的情况启用）。|
|为每个响应添加 "Cache-Control: no-cache" 的 HTTP 响应头。|
|提供动态生成的页面。|

#### 关于--single/-s开关以及美化
当不打开这个开关时,每一次对于目录的访问都会将main.py同一文件夹下的`template.html`,作为响应主体返回给客户端,同时,会对这个文件夹中的特定的文本进行替换,替换的文本以及对应含义如下
|替换文本|含义|
|-------|----|
|`${#CD}`|返回上级目录的`<a>`标签的href属性|
|`${#FULLPATH}`|当前的目录的完整路径|
|`${#PATH}`|运行目录的相对路径|
|`${#LIST_NAME}`|当前目录的所有文件和文件夹的名称(一个一行)|
|`${#LIST_TYPE}`|`文件/文件夹`,用`0/1`表示(一个一行),与`${#LIST_NAME}`的顺序完全一致,可用于对`文件/文件夹`设置不同的样式|
|`${#LIST_LEN}`|上面两个列表的长度|另外,如果文件未被找到,则会返回`404.html`|

---

#### 关于filter.py
这个.py文件里面应该有一个名为fileFilter的函数,定义如下:
```python
def fileFilter(fullpath,name,isdir):
    	if isdir:return 1 #如果是目录,则返回1(True),则所有的目录都不会被拦截
	if 'secret' in name:return 0 #如果文件名中有'secret'则返回0(False),即拦截这个文件
	return 1
```

