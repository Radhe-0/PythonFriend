## PythonFriend: Easy Way to Use Python in Godot

PythonFriend is a tool for Godot that makes it easy to use Python code in your Godot projects. 

**What PythonFriend Does:**

- **Run Python functions from Godot:**  You can call Python code directly from Godot and get results back.
- **Simple to use:** It's easy to set up and use.
- **Find and fix Python problems in Godot:** You can see Python errors in Godot, which makes it easier to fix them.
- **Works with many Python tools:** It works with a lot of Python libraries.
- **Works on Windows, Linux, and macOS:** You can use it on different computers.
- **Use Python virtual environments:** This makes it easier to manage your Python projects.
- **Combine Python code with your Godot game:**  You can make your Godot games using Python code.

## How to Install

1. Download the files from this page and put the `addons/python_friend` folder in the same place as your Godot project.
2. Turn on the PythonFriend tool in your Godot project settings.

## How to Set It Up:

1. **Make a Python virtual environment inside `addons/python_friend/python_stuff/`.** 
2. **Open your virtual environment and run `pip install -r requirements.txt` from the `addons/python_friend/python_stuff/` folder.** 
3. **Make a `.gdignore` file in the virtual environment folder (`addons/python_friend/python_stuff/venv/`).** This stops Godot from using files from the virtual environment.
4. **Add a `PythonFriend` node to your Godot scene.**
5. **Tell the `PythonFriend` node where your virtual environment is, the name of your main Python file (`main.py`), and the name of your executable file.**
    - **Python Interpreter:**  Put the path to your Python program in your virtual environment. Example: `res://addons/python_friend/python_stuff/venv/bin/python3`
    - **Main Python File:** Put the path to your main Python file that has the functions you want to use. Example: `res://addons/python_friend/python_stuff/main.py`
    - **Executable File Name:** This is the name of your main Python file after you've made it into an executable program. The name changes depending on your computer:
        - **Linux/MacOS:** `py_backend`
        - **Windows:** `py_backend.exe`
        - This executable file needs to be in the same folder as the Godot program.


## Example


- **Godot script:**

```gdscript
extends Control

func _ready():
	var params = {"a": 10, "b": 6}
	$PythonFriend.python_run("generate_sum", params)

func _on_python_friend_python_output(output, is_error):
	print(output)
	print(is_error)
```


- **Python script (main.py):**

```python
import godot_friend

def generate_sum(params): # This function expects a dictionary 'params' containing 'a' and 'b' keys.
	a = params.get('a')
	b = params.get('b')
	result = a + b

	return {"result": result}


func_map = {
	"generate_sum": generate_sum,
}
	

if __name__ == "__main__":
	# Sets the name of the Godot application. This is used to create a directory for communication data within 'godot/app_userdata/<app_name>'.
	# Please, use the name set in "application/config/name" Godot property (or in project config --> Application --> Name)
	app_name = "YourProjectName" # Replace with your project's name
	godot_friend.set_app_name(app_name)
	# Makes the Python functions accessible from the Godot application by name.
	godot_friend.add_map(func_map) 
	# Processes input from Godot and executes the corresponding Python function.
	godot_friend.ready()
```

**How it Works:**

PythonFriend uses a simple way to let Godot and Python talk to each other.  They share information using `.json` files:

1. **Godot sends information:** When you use `call_function` in Godot, it saves a `.json` file with the function name and arguments.
2. **Python reads the information:** The Python script runs and reads the `.json` file.
3. **Python runs the function:** The Python script then runs the function you asked for, using the arguments from the `.json` file.
4. **Python sends back the results:** The Python script saves the results of the function call in a new `.json` file.
5. **Godot reads the results:** Godot reads the `.json` file and gets the results of the function call.
6. **The `.json` files are deleted:** Once the information is used, the `.json` files are deleted.

This process happens quickly and smoothly, letting you run Python code from Godot without any complex setup. 

**PythonFriend makes it easy to add Python to your Godot projects!** 



