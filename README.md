# INET4031 Add Users Script and User List

## Program Description
This program automates the process of adding multiple users and assigning them to groups on an Ubuntu Linux system. It reads user account information from an input file and runs the necessary system commands to create users, set passwords, and assign group memberships. This reduces manual work and helps keep user creation consistent and repeatable.

## Program User Operation
This program reads a list of users from an input file and creates each user on the system. It also assigns users to the appropriate groups based on the data in the file. The script processes the file line by line, skipping commented or invalid lines, and only acting on lines that contain all required fields.

### Input File Format
Each line in the create-users.input file represents one user. The format is colon-delimited:

username:password:last:first:group1,group2

Field descriptions:
- username – the Linux username to create
- password – the user’s password
- last – last name
- first – first name
- groups – a comma-separated list of groups (example: group01,group02). Use '-' if the user should not be added to any groups.

Skipping a user:
- Any line beginning with '#' is ignored by the script.

Invalid lines:
- If a line does not contain all five fields, the script automatically skips it.

### Command Execution
Before running the script, make it executable:

chmod +x create-users.py

Run the script using input redirection:

./create-users.py < create-users.input

This will process each user in the input file and create them on the system.

### Dry Run
The script includes a dry run mode, which allows the user to preview what actions the script would take without actually creating users or modifying the system. In dry run mode, the os.system() calls remain commented out, and the script only prints the commands that would have been executed.
