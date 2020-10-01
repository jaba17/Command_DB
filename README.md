# Command_DB
A simple CLI tool which manages your favorite Linux commands.


# How to install: 
In order to install you have to execute the ./setup file. 
But first you have to make the file executable by typing ```sudo chmod +x setup```

*More Installation infos coming soon.*


# How to use: 

## Add a new command to the DB: 
In order to add a new command you have to give it a unique id, eg "list_files" for the command "ls -la". 
```
# ./command_db.py add "list_files" "ls -la"
```

Furthermore, you can add a description of the command if you want. 
```
# ./command_db.py add "list_files" "ls -la" -d "This command lists all files in the CD."
```

## Remove a command: 
*TODO*


## List all commands: 
This prints out all saved commands in a list. 
```
# ./command_db.py list
```

## Execute a specific command
```
# ./command_db.py execute "list_files"
```