# -*- coding: utf-8 -*-
import sublime
import sublime_plugin

class GetTimeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "get Time ! \n")

class SayHelloCommand(sublime_plugin.TextCommand):
	def run(self, edit,message):
		self.view.insert(edit, 0, "say Hello: " + message + "\n")
class CreateTempletCommand(sublime_plugin.TextCommand):
	def run(self,edit):
		currentView = self.view
		allSelect = currentView.sel()
		firstSelect = allSelect[0]
		content = currentView.substr(firstSelect)

		tempBuilder = "\t// ===== begin =====\n"
		for line in content.split("\n"):
			tempBuilder += "\t" + line + "\n"
		tempBuilder += "\t// ===== end =====\n"

		# ���е���ǰѡ�е�����
		currentView.run_command('cut')

		# ��������
		currentView.insert(edit,0,tempBuilder)
