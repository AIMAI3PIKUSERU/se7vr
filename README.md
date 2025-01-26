# se7vr

#### 介绍
这是一个基于Python的轻量,强自定义性的服务器程序

#### 额外的库
本程序基于flask 库,安装方式:

```
pip install flask
```

#### 使用说明

在终端输入`python main.py`即可运行,浏览器输入[127.0.0.1:8000](http://127.0.0.1:8000)即可访问
仓库中的main.py以外的文件全都不是必须的,只是给美化留了一条后路
如果你想体验 `python -m http.server`的界面,输入`python main.py -s`即可
键入 --help/-h 参数以查看帮助,其输出如下
|[port] |--bind [ip] --dir [directory] --active --encode --nocache --single|
|-----|------|
| --bind/-b | [ip=0.0.0.0]: The specific IP address to bind to. |
| --dir/-d  | [directory=.]: The directory to serve files from. |
|--active/-a| Actively reload "template.html" and "404.html" on each request.|
|--encode/-e| Encode the path (use this when characters are displayed incorrectly).|
|--nocache/-n| Add the "Cache-Control: no-cache" HTTP header to each response.|

