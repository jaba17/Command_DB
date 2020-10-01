#!/usr/bin/python3

import json
import os
import click


# Main Function
@click.group()
def cli():
	pass


# Print out all saved commands
@cli.command()
def list():
	json_data = json.loads(open('commands.json').read())
	click.echo("Saved Commands:")
	click.echo('------------------------------------------------------------------------')
	for command in json_data['commands']:
		click.echo("Shortcut: " + command[0])
		click.echo("Description: " + command[1])
		click.echo("Command: " + command[2])
		click.echo('------------------------------------------------------------------------')


# Add a new command to dataset
@cli.command()
@click.option('--d',  help='Description', default='')
@click.argument('args', nargs=2)
def add(args, d):
	command = args[0]
	shortcut = args[1]
	json_data = json.loads(open('commands.json').read())
	commands = json_data['commands']
	print(commands)

	if any(shortcut in x[0] for x in commands):
		click.echo("Error: Shortcut already used.")

	if any(shortcut in x[2] for x in commands):
		click.echo("Error: Command already saved.")

		
	else: 
		json_data['commands'].append([shortcut, d, command])

		with open('commands.json', 'w') as writer:

			writer.write(json.dumps(json_data))
			writer.close()

		click.echo("Added '{}' to dataset.".format(shortcut))


# Get the command and execute it
@click.argument('shortcut')
@cli.command()
def execute(shortcut):
	json_data = json.loads(open('commands.json').read())

	ret_command = "echo 'Error in Command_Save'"

	for command in json_data['commands']:
		if command[0] == shortcut:

			ret_command = command[2]
			break
	click.echo("Executing '{}'.".format(shortcut))
	os.system(ret_command)


# Start cli() function
if __name__ == '__main__':
    cli()