import sublime
import sublime_plugin
import re

class RunPythonTest(sublime_plugin.WindowCommand):
	def run(self):
		path, cmnd = self.settings()
		file_name = self.window.active_view().file_name().replace(str(path), '')
		if re.search('_test.py', file_name):
			cmd = cmnd + file_name
			self.window.run_command('exec', {'cmd': [cmd], 'shell':True} )

	def settings(self):
		settings = sublime.load_settings("run_python_test.sublime-settings")
		cmd = settings.get("cmd")
		path= settings.get("path")
		return [path, cmd]