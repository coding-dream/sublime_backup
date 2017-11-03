## 自定义插件说明
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

