RunPythonTests
==============

copy run_python_test.sublime-settings to your User folder and set proper paths and cmds:

`{
  "cmd": "ssh dev 'cd ~/path-to-code; testify '",
  "path": "/Users/path-to-your-code-folder/"
}`



add keybinding:

` { "keys": ["super+shift+r", "y"], "command": "run_python_test" } `
