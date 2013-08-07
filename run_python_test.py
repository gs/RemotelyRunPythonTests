import sublime
import sublime_plugin
import re

class RunPythonTest(sublime_plugin.WindowCommand):
	def run(self):
		path, cmnd = self.settings()
		file_name = self.window.active_view().file_name().replace(str(path), '')
		if re.search('_test.py', file_name):
			self.window.run_command('exec', {'cmd': [cmnd + file_name], 'shell':True} )
		else:
			sublime.error_message("Wtf? Is this a test file?!")

	def settings(self):
		settings = sublime.load_settings("run_python_test.sublime-settings")
		if (settings.get("path")=="") or (settings.get("cmd")==""):
			sublime.error_message("Please define 'cmd' and 'path' in run_python_test.sublime-settings")
		else:
			return [settings.get("path"), settings.get("cmd")]