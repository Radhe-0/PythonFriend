@tool
extends EditorPlugin


func _enter_tree():
	add_custom_type("PythonFriend", "Node", preload("plugin.gd"), preload("icon.svg"))


func _exit_tree():
	remove_custom_type("PythonFriend")
