## Package Control安装

**备份**

点击 Packages（Preferences > Browse Packages），把该目录下内容拷贝一份，同步云端即可

**安装插件**

按 Ctrl+` 调出console

方式一：使用【package control组件】安装（先安装组件）

```	
import urllib.request,os; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); open(os.path.join(ipp, pf), 'wb').write(urllib.request.urlopen( 'http://sublime.wbond.net/' + pf.replace(' ','%20')).read())
```
重启Sublime Text 3。如果在Perferences->package settings中看到package control这一项，则安装成功。

按下Ctrl+Shift+P调出命令面板输入install 调出 Install Package 选项并回车，然后在列表中选中要安装的插件。

方式二：把下载好的插件直接放到Packages目录（菜单->preferences->browse packages）

## Python3输出中文的问题
Python - Sublime Text 3 控制台不能输出中文的解决方法

工具 -> 编译系统  -> 新编译系统
```
{  
    "cmd": ["python","-u","$file"],  
    "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",  
    "selector": "source.python",  
    "encoding": "cp936" 
}
```
保存mypython.sublime-build，然后在工具->编译系统->选择 "mypython.sublime-build" 

## sublineText 输出乱码问题
http://blog.csdn.net/jim7424994/article/details/22675759
```
# encoding=utf8
import io  
import sys  
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')         #改变标准输出的默认编码  

import requests
class Animal:
	def fly(self):
		print("我想飞 起来")

class Dog(Animal):
	def say(self):
		print("我想飞 起来")

dog = Dog()
dog.say()
dog.fly()

url = "http://blog.csdn.net/rocklee"
html = requests.get(url)
print(html.content.decode("utf8"))
```
## 资源
https://packagecontrol.io/

## Sublime Text3的一些神奇快捷键(windows)

1. Ctrl+O可以打开当前你编辑的文件所在文件夹
2. Alt+Shift+2进行左右分屏，Alt+Shift+3分竖三屏,Alt+Shift+1分成1屏。
3. Ctrl+P输入：
```
@ss跳转到ss符号所在位置
#key跳转到key关键字所在位置
:10跳转到第10行
```
4. Ctrl + Enter 在当前行下面新增一行然后跳至该行；Ctrl + Shift + Enter 在当前行上面增加一行并跳至该行。
5. Ctrl + ←/→ 进行逐词移动，相应的，Ctrl + Shift + ←/→ 进行逐词选择。
6. Ctrl+D，选中某个词，多次Ctrl +D 可以选择文中所有某个关键词，并统一修改，这个太强了，比正则好用到哪里。
7. 同步编辑除了Ctrl+D，还有一个方式：按住Shift，然后按住鼠标右键，最后，垂直向下拉，就像Eclipse那个强大的多选功能一样。
8. Ctrl+F后，Enter查找下一个，Shift+Enter，查找上一个。Ctrl+H，查找替换，就不多说了。
9. **Ctrl+Shift+F**，重要，牛掰。怎么说呢，可以叫全项目查找。
10. Ctrl+R定位函数；Ctrl+G定位到行；
11. 编辑代码时我们经常会开多个窗口，所以分屏很重要。Windows下：Alt + Shift + 2进行左右分屏，Alt + Shift + 8进行上下分屏，Alt + Shift + 5进行上下左右分屏（即分为四屏）
12. Ctrl + `  打开Sublime Txt的控制台。



## 强大的功能
像Eclipse一样查找函数定义

在方法或者某个类上面点击右键->选择goto_definition即可（这已经是sublime默认的功能）

为了更加方便，我们设置了一个快捷键，到

Preferences-> keyBindings->会弹出两个设置快捷键的文件，我们只修改右边那个，左边的是系统默认的，右边的是用户自己的，修改的会覆盖掉默认的某些快捷键，设计真好！

```
[
	{ "keys": ["ctrl+i"], "command": "goto_definition" }
]
```

将文件夹加入项目，点击菜单 Project -> Add Fold To Project，选择你要加入项目的文件夹即可。但是默认sublime不显示左边的sideBar，View -> Side Bar -> Show Side Bar（都是sublime默认含有的，没装插件）


## 定制属于自己的快捷键
设置快捷键。在SublimeText里，打开Preferences -> Key Bindings - User。

比如：修改快捷键为Eclipse，在Preferences菜单选择Key Bindings，将下面的代码粘贴到Users文件内。

## 定制专属的编译器
SublimeText3;完毕后上面选择:

Build System–New Build System 输入：
```
{
	"shell_cmd": "D:\\Codes\\sublime_backup\\runJava.bat $file",
	"file_regex": "^(...*?):([0-9]*):?([0-9]*)",
	"selector": "source.java",
	"encoding": "GBK"
}
```
新建一个bat文件,内容如下
```
@echo off
cd %~dp1
echo Compiling %~nx1......
if exist %~n1.class (
del %~n1.class
)
javac -encoding UTF-8 %~nx1
if exist %~n1.class (
echo ------Output------
java %~n1
)
```

## 常用高效插件
**ConvertToUTF8**

![安装后，将可以将常用中文编码转换成UTF-8](http://upload-images.jianshu.io/upload_images/26219-6872c20b77473a8c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240/format/jpg)

**Sublime Terminal**

可以在当前文件位置打开终端

**DocBlockr**

可以自动生成PHPDoc风格的注释。它支持的语言有Javascript, PHP, ActionScript, CoffeeScript, Java, Objective C, C, C++

**MarkdownPreview**

根据md文件生成html文件。

按CTRL + B生成网页HTML；在最前面添加[TOC]自动生成目录；

```
[TOC]

## Java是最好的
1. first
2. second
3. three

## C是最好的
1. first
2. sencond
3. three
## Python是最好的
1. first
2. sencodn
3. three
```

## 激活注册
```
—– BEGIN LICENSE —–
TwitterInc
200 User License
EA7E-890007
1D77F72E 390CDD93 4DCBA022 FAF60790
61AA12C0 A37081C5 D0316412 4584D136
94D7F7D4 95BC8C1C 527DA828 560BB037
D1EDDD8C AE7B379F 50C9D69D B35179EF
2FE898C4 8E4277A8 555CE714 E1FB0E43
D5D52613 C3D12E98 BC49967F 7652EED2
9D2D2E61 67610860 6D338B72 5CF95C69
E36B85CC 84991F19 7575D828 470A92AB
—— END LICENSE ——
```
## 自定义插件
1. 创建一个MyCustomPlugin文件夹
2. 创建一个MyPlugin.py文件，名字随意，SublimeText不是根据这个找命令的。
该文件内每个类都是一个命令，但是类的命名有规定。

如 
```
import sublime
import sublime_plugin


class GetTimeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "get Time ! \n")

class SayHelloCommand(sublime_plugin.TextCommand):
	def run(self, edit,message):
		self.view.insert(edit, 0, "say Hello" + message + "\n")

```
3. 然后在`Default (Windows).sublime-keymap`文件中设置该命令对应的快捷键就可以了。
```
[
	{ "keys": ["ctrl+shift+j"], "command": "get_time"},
	{ "keys": ["ctrl+shift+k"], "command": "say_hello","args":{"message":"hello python"} }
]
```
4. 如果你想给某个命令设置个菜单入口（可选），可以这么做。

新建Main.sublime-menu文件，内容如下：
```
[
    {
        "caption": "我的插件",
        "id": "x5pro0001",
        "children":
        [
            {"id":"deeper001","caption": "获取时间","command": "get_time"},
			{"id":"deeper002","caption": "打个招呼","command": "say_hello","args":{"message":"最近可好！"} },
			{"id":"deeper003","caption": "生成Java模板","command": "create_templet"}
        ]
    }
]
```
5. 然后把这两个文件都放在MyCustomPlugin文件夹下，然后移动到SublimeText的Packages目录即可。

如：我的SublimeText目录是`C:\Users\Administrator\AppData\Roaming\Sublime Text 3\Packages`

一个基本插件已经开发完成，非常简单。


**官方接口**

英文版：http://www.sublimetext.com/docs/3/api_reference.html

中文版 ：http://www.oschina.net/translate/sublime-text-plugin-api-reference

