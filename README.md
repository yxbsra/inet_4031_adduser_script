# INET4031 Add Users Script and User List
## Program Description
This program automates the process of adding multiple users and assigning them to groups on an Ubuntu Linux system. Normally, a system administrator would manually run commands such as `adduser`, `passwd`, and `usermod -aG` for every user that needs to be created. This script performs those same operations automatically by reading user information from an input file and executing the required system commands. This saves time, reduces errors, and ensures consistent configuration across multiple servers.
## Program User Operation
This program reads a list of users from an input file and creates each user on the system. It also assigns users to the appropriate groups based on the data provided. The script processes the file line‑by‑line, skipping invalid or commented lines, and performs all required user and group operations automatically. The sections below explain how to prepare the input file, how to run the script, and how to perform a dry run.
### Input File Format
Each line in the `create-users.input` file represents one user. The format is colon‑delimited:
username:password:last:first:group1,group2
Field descriptions:
- username – the Linux username to create
- password – the user’s password
- last – last name
- first – first name
- groups – a comma‑separated list of groups (example: group01,group02). Use `-` if the user should not be added to any groups.
Skipping a user:
- Any line beginning with `#` is ignored by the script.
Invalid lines:
- If a line does not contain enough fields, the script automatically skips it.
### Command Execution
Before running the script, make it executable:
chmod +x create-users.py
Run the script using input redirection:
./create-users.py < create-users.input
This will process each user in the input file and create them on the system.
### Dry Run
The script includes a dry run mode, which allows the user to preview what actions the script would take without actually creating any users or groups. When dry run mode is enabled, the script prints the commands it would execute but does not modify the system. This is useful for verifying the input file before making real changes.
