import json
import os

# Print out all saved commands
def list_commands():
	json_data = json.loads(open('commands.json').read())
	print("Saved Commands:")
	print('------------------------------------------------------------------------')

	for command in json_data['commands']:
		print("Shortcut: " + command[0])
		print("Description: " + command[1])
		print("Command: " + command[2])
		print('------------------------------------------------------------------------')



# Add a new command to dataset
def add_command(shortcut, description, command):

	json_data = json.loads(open('commands.json').read())

	json_data['commands'].append([shortcut, description, command])



	with open('commands.json', 'w') as writer:
		writer.write(json.dumps(json_data))
		writer.close()


	print("Added '{}' to dataset.".format(shortcut))


def get_command(shortcut):
	json_data = json.loads(open('commands.json').read())

	ret_command = "echo 'Error in Command_Save'"

	for command in json_data['commands']:
		if command[0] == shortcut:

			ret_command = command[2]
			break

	os.system(ret_command)
get_command("show_file");

#get_command()
#add_command("show_file", "shows files", "ls") 
