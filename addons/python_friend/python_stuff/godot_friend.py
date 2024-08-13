import json
from platformdirs import user_data_dir
from pathlib import Path


app_name = ""
godot_data_dir = Path(user_data_dir("godot/app_userdata"))
app_data_dir = godot_data_dir / app_name

func_map = {}

def set_app_name(name):
	global app_name
	global app_data_dir
	app_name = name
	app_data_dir = godot_data_dir / app_name


def get_py_input():
	py_input = app_data_dir / "py_input.json"
	if py_input.exists():
		with open(py_input, 'r') as file:
			data = json.load(file)
			py_input.unlink()
			return data
	return None


def set_py_output(data):
	py_output = app_data_dir / "py_output.json"
	with open(py_output, 'w') as file:
		json.dump(data, file, indent=4)


def add_map(mapping):
	global func_map
	func_map = mapping


def ready():
	try:
		py_input = get_py_input()
		func = py_input.get("func")
		params = py_input.get("params")

		if func in func_map:
			data = func_map[func](params)
			set_py_output(data)
		else:
			set_py_output({"error": f"Function '{func}' not found in function map."})
	except Exception as e:
		set_py_output({"error": str(e)})