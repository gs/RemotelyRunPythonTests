import sublime
import sublime_plugin
import re

class RemotelyRunPythonTest(sublime_plugin.WindowCommand):
	def run(self):
		path, cmnd, out = self.settings()
		file_name = self.window.active_view().file_name().replace(str(path), '')
		if re.search('_test.py', file_name):
			self.window.run_command('exec', {'cmd': [cmnd + file_name], 'shell':True} )
			self.window.run_command('exec', {'cmd': [out], 'shell':True} )
		else:
			sublime.error_message("Wtf? Is this a test file?!")

	def settings(self):
		settings = sublime.load_settings("remotely_run_python_test.sublime-settings")
		path = settings.get("path")
		cmd = settings.get("cmd")
		out = settings.get("out")
		if (path == "") or (cmd == ""):
			sublime.error_message("Please define 'cmd' and 'path' in remotely_run_python_test.sublime-settings")
		else:
			return [path, cmd, out]