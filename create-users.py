#!/usr/bin/python3

# INET4031
# Yeabsra Dereje
# Date Created:
# Date Last Modified:

# os is used to run system commands, re is used for pattern matching, and sys allows reading input from stdin
import os
import re
import sys

def main():
    for line in sys.stdin:

        # Check if the line begins with '#' which indicates a comment that should be skipped
        match = re.match("^#", line)

        # Split the input line into fields so we can extract username, password, names, and groups
        fields = line.strip().split(':')

        # Skip the line if it is a comment or does not contain exactly 5 fields of required user data
        if match or len(fields) != 5:
            continue

        # Extract username, password, and build the GECOS field used in /etc/passwd for user info
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])

        # Split the group field by commas so the user can belong to multiple groups
        groups = fields[4].split(',')

        # Inform the user that an account is about to be created
        print("==> Creating account for %s..." % (username))

        # Build the command that creates the user with no password and sets the GECOS information
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

        # Print and execute the user creation command
        print(cmd)
        os.system(cmd)

        # Inform the user that the password is being set
        print("==> Setting the password for %s..." % (username))

        # Build the command that sets the user's password using the passwd command
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        # Print and execute the password-setting command
        print(cmd)
        os.system(cmd)

        for group in groups:
            # Only assign the user to a group if the field is not '-' (which means no groups)
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))

                # Build the command that adds the user to the specified group
                cmd = "/usr/sbin/adduser %s %s" % (username, group)

                # Print and execute the group assignment command
                print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()

