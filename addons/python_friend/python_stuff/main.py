# main.py
# godot_friend example, you can edit it for your convenience

# Imports the module responsible for Godot-Python communication
import godot_friend

#  The parameters for the functions are handled within the dictionary passed in 'params'.

def generate_greeting(params): # This function expects a dictionary 'params' containing a 'name' key.
	name = params.get('name') 

	return {"greeting": f"Hello, {name}!"}

# This function is not directly called by Godot and serves as a helper function. Therefore, it does not take the 'params' dictionary as input.
def add(a, b):
	return a + b


def generate_sum(params): # This function expects a dictionary 'params' containing 'a' and 'b' keys.
	a = params.get('a')
	b = params.get('b')
	result = add(a, b)

	return {"result": result}


# This dictionary maps function names (strings) to their corresponding Python functions, allowing Godot to call them by name.
func_map = {
	"generate_greeting": generate_greeting,
	"generate_sum": generate_sum,
}
	

if __name__ == "__main__":
	# Sets the name of the Godot application. This is used to create a directory for communication data within 'godot/app_userdata/<app_name>'.
	# Please, use the name set in "application/config/name" Godot property (or in project config --> Application --> Name)
	app_name = ""
	godot_friend.set_app_name(app_name)
	# Makes the Python functions accessible from the Godot application by name.
	godot_friend.add_map(func_map) 
	# Set tkinter debug even in export
	godot_friend.set_debug(True)
	# Processes input from Godot and executes the corresponding Python function.
	godot_friend.ready()
