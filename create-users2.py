#!/usr/bin/python3

# INET4031
# Yeabsra Dereje

import os
import re
import sys

# This program supports two modes of operation:
#   1. Dry-run mode (Y): The script does NOT execute any system commands.
#      Instead, it prints the commands that *would* have run. This allows
#      the user to safely preview account creation without modifying the system.
#
#   2. Normal mode (N): The script executes all os.system() commands to
#      actually create users, set passwords, and assign groups.
#
# Dry-run mode is controlled by the 'dry_run' boolean. When dry_run is True,
# every system command is printed but skipped. When dry_run is False, the
# commands are executed normally.
#
# Additionally, in dry-run mode the script prints error messages for invalid
# input lines and prints messages for skipped comment lines. In normal mode,
# these messages are suppressed to avoid cluttering real system output.

mode = input("Run in dry-run mode? (Y/N): ").strip().upper()
dry_run = (mode == "Y")

def main():
    for line in sys.stdin:

        # Check if the line begins with '#' which indicates a comment that should be skipped
        match = re.match("^#", line)

        # Split the input line into fields so we can extract username, password, names, and groups
        fields = line.strip().split(':')

        # Skip the line if it is a comment or does not contain exactly 5 fields of required user data
        if match or len(fields) != 5:
            if dry_run:
                if match:
                    print("Skipped line (comment):", line.strip())
                else:
                    print("Error: Line does not contain 5 fields:", line.strip())
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
        if not dry_run:
            os.system(cmd)

        # Inform the user that the password is being set
        print("==> Setting the password for %s..." % (username))

        # Build the command that sets the user's password using the passwd command
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        # Print and execute the password-setting command
        print(cmd)
        if not dry_run:
            os.system(cmd)

        for group in groups:
            # Only assign the user to a group if the field is not '-' (which means no groups)
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))

                # Build the command that adds the user to the specified group
                cmd = "/usr/sbin/adduser %s %s" % (username, group)

                # Print and execute the group assignment command
                print(cmd)
                if not dry_run:
                    os.system(cmd)

if __name__ == '__main__':
    main()

