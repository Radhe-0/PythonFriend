## PythonFriend: Easy Way to Use Python in Godot

PythonFriend is a tool for Godot that makes it easy to use Python code in your Godot projects.

## What PythonFriend Does

- **Run Python functions from Godot:** Call Python code directly from Godot and get results back.
- **Simple to use:** Easy setup and integration.
- **Monitor Python interactions:** Use Tkinter to visualize and debug the flow of data between Godot and Python. This helps track the communication process and identify issues.
- **Works with many Python tools:** Compatible with a variety of Python libraries.
- **Cross-platform:** Works on Windows, Linux, and macOS.
- **Supports Python virtual environments:** Manage your Python dependencies easily.

## How to Install

1. Download the files from this page and place the `addons/python_friend` folder in your Godot project directory.
2. Enable the PythonFriend tool in your Godot project settings.

## How to Set It Up

1. **Create and activate a Python virtual environment** inside `addons/python_friend/python_stuff/`.
2. **Install the required Python packages** by running `pip install -r requirements.txt` from the `addons/python_friend/python_stuff/` folder.
3. **Tkinter Installation (Linux Only):** On Linux systems, you may need to install Tkinter separately. You can do this using your distribution's package manager. For example, on Debian or Ubuntu, you can use the following command:

   ```bash
   sudo apt-get install python3-tk 
   ```
4. **Create a `.gdignore` file** in the virtual environment folder (`addons/python_friend/python_stuff/venv/`) to prevent Godot from including files from the virtual environment.
5. **Add a `PythonFriend` node** to your Godot scene.
6. **Configure the `PythonFriend` node:**
   - **Python Interpreter:** Specify the path to your Python interpreter within the virtual environment. Example: `res://addons/python_friend/python_stuff/venv/bin/python3`
   - **Main Python File:** Provide the path to your main Python file containing the functions to be called. Example: `res://addons/python_friend/python_stuff/main.py`
   - **Executable File Name:** The name of the executable file created from your main Python file, which must be in the same folder as the exported Godot project. Examples:
     - **Linux/MacOS:** `py_backend`
     - **Windows:** `py_backend.exe`

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

def generate_sum(params):  # This function expects a dictionary 'params' containing 'a' and 'b' keys.
    a = params.get('a')
    b = params.get('b')
    result = a + b
    return {"result": result}

func_map = {
    "generate_sum": generate_sum,
}

if __name__ == "__main__":
    # Set the application name for creating communication directories.
    app_name = "YourProjectName"  # Replace with your project's name
    godot_friend.set_app_name(app_name)
    # Make Python functions accessible from Godot by name.
    godot_friend.add_map(func_map)
    # Set tkinter debug even in export
    godot_friend.set_debug(True)
    # Process input from Godot and execute corresponding Python functions.
    godot_friend.ready()
```

## Exporting Your Godot Project with PythonFriend

To successfully export your Godot project with PythonFriend, follow these steps:

1. **Export the Godot Project:**
   - Export your Godot project as usual to an empty directory of your choice. Ensure the exported project folder contains all necessary files for distribution.

2. **Create the Python Executable:**
   - Navigate to the `addons/python_friend/python_stuff/` directory in your project.
   - Activate the virtual environment you created for the project.
   - Run the following command to create a standalone executable of your main Python script:

     ```sh
     pyinstaller --onefile --windowed main.py
     ```

     If you renamed your main Python script from `main.py` to something else, replace `main.py` with the new name.

3. **Locate the Executable:**
   - PyInstaller will generate several directories. Locate the `dist` directory within your project folder. Inside `dist`, you will find the executable:
     - **Linux/macOS:** The executable will be named `main`.
     - **Windows:** The executable will be named `main.exe`.

4. **Prepare the Executable for Distribution:**
   - Copy the appropriate executable file (`main` for Linux/macOS or `main.exe` for Windows) from the `dist` directory.
   - Paste this file into the same directory where you exported your Godot project.
   - Rename the executable to `py_backend` for Linux/macOS or `py_backend.exe` for Windows, ensuring it matches the configuration in your Godot project settings.

By following these steps, you'll have the necessary Python executable in place alongside your exported Godot project, allowing for proper interaction between the Godot application and Python backend.

## How it Works

PythonFriend uses a straightforward method for communication between Godot and Python via `.json` files:

1. **Godot sends information:** Calls to Python functions are saved in `comm_channel.json` with function names and arguments.
2. **Python reads the information:** The Python script reads `comm_channel.json`.
3. **Python runs the function:** Executes the function specified in the `.json` file using the provided arguments.
4. **Python sends back the results:** Results are saved in `comm_channel.json`.
5. **Godot reads the results:** Godot reads the updated `comm_channel.json` to get the function results.
6. **File Cleanup:** The contents of `comm_channel.json` are cleared after processing. The file itself is not deleted.

### Monitoring and Debugging

- **Tkinter for Flow Monitoring:** Tkinter is used in Python to display debug messages and monitor the flow of information between Godot and Python. This helps to track and visualize communication, making it easier to understand the data exchange process.
- **Editor Debugging:** Errors in Python code can be observed and debugged within the Godot editor. This allows for real-time feedback and troubleshooting during development.

## Limitations

PythonFriend is currently in its early stages and has a few limitations:

- **Call Frequency:** It's not recommended to make more than 150 calls to Python per minute due to potential performance bottlenecks.
- **Android Support:** The current implementation is not compatible with Android.
- **Error Handling:** While basic error handling is in place, more robust mechanisms are planned for future updates.


**PythonFriend makes it easy to add Python to your Godot projects!** 



