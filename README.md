#FriedRing
##简介
通过mitmproxy实现了交互脚本的录制，通过multimechanize实现了并发测试和测试报告（html格式）生产，同时格式化了mitmproxy脚本为requests格式
##基础
1、mitmproxy

2、multimechanize

3、requests

##安装mitmproxy和multimechanize
###Mac or Unbuntu
	pip install mitmproxy
	pip install -U multi-mechanize
	pip install requests
###Windows
	python -m pip install --upgrade pip(最支持版本8.1.2,多次运行可以升级到对应版本) []()
	python -m pip install netlib pyopenssl pyasn1 urwid pil lxml flask
	python -m pip install pyamf protobuf
	python -m pip install pil
	python -m pip install nose pathod countershape
	python -m pip install matplotlib
	python -m pip install mitmproxy
	pip install -U multi-mechanize
	pip install requests
##安装FiredRing

	pip install -U FiredRing

##使用FriedRing

首先，输入命令

	 python fr.py -p 8888 -w scriptsolution
	 
-p 端口号，-w 测试脚本文件夹

其次，在测试浏览器或者测试手机中设置代理（ip为运行主机ip，端口为888）
按照功能测试流程进行功能测试，在当前文件夹中会产生一个scriptsolition的文件夹，结构如下：
	
	scriptsolution/config.cfg(multimechan的配置文件）
	
	scriptsolution/test _ scripts/v_user.py（默认的初始化脚步）
	
	scriptsolution/test _ scripts/script.py（生成的测试脚步）

在录制完成后，需要修改scriptsolution/test _ scripts/script.py文件，去掉不属于本次测试的请求。

同时可以通过加入assert等信息做断言（详情可以参考requests包）



##运行脚本
###Mac or Unbuntu
在scriptsolution的父文件夹，执行

	multimech-run scriptsolution

###Windows

在scriptsolution的父文件夹，执行

	C:\FriedRing>python c:\Python27\Lib\site-packages\multimechanize\utilities\run.py scriptsolution
	
##查看结果
结果在scriptsolution文件夹下的results里面，按照时间顺序生产的文件夹，里面有一个result.html，用浏览器打开就可以看到结果信息了。
## 源代码地址
	https://github.com/crisschan/FriedRing
##修改历史
- 1.0.0新建了项目
- 1.0.1-1.0.3 因为打包没弄好折腾了几次
- 1.0.4 修复了一个获取headers中有英文双引号会出现，导致到脚本出现语法错误。
- 1.0.5 修复了一个1.0.4 打包错误
- 1.0.6 修复了之前版本中requirement中错误的引用

