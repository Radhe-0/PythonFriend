# PythonFriend

```
extends Control

func _on_button_pressed():
	var params = {"a": 10, "b": 6}
	$PythonFriend.python_run("generate_sum", params)

func _on_python_friend_python_output(output, is_error):
	print(output)
	print(is_error)
```
