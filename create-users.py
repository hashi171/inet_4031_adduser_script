#!/usr/bin/python3

# INET4031
# Duale Hashi
# Date Created: 10/27
# Date Last Modified: 10/27

# os = run OS commands; re = detect comment lines; sys = read lines from STDIN
import os
import re
import sys

# Read each line from the redirected input file
def main():
    for line in sys.stdin:

        # Skip any line that starts with '#' (these are comments in the input file)
        match = re.match("^#", line)

        # Remove extra spaces and split each input line by ':' into fields
        fields = line.strip().split(':')

        # Skip lines that are comments or don’t have exactly 5 fields to avoid bad data
        if match or len(fields) != 5:
            continue

        # Store username, password, and GECOS info (GECOS is full name info in /etc/passwd)
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])

        # Split group field by commas to handle multiple groups
        groups = fields[4].split(',')

        # Create user account
        print("==> Creating account for %s..." % (username))
        # Build adduser command that adds the user with no password but includes GECOS info
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
        print(cmd)
        os.system(cmd)

        # Set user password using echo and passwd command
        print("==> Setting the password for %s..." % (username))
        # Command sends the password twice (for confirmation) to passwd via pipe
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)
        print(cmd)
        os.system(cmd)

        # Add user to groups if the group is not '-'
        for group in groups:
            # Only add user to actual groups; skip '-' entries
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                print(cmd)
                os.system(cmd)

if __name__ == '__main__':
    main()
    for line in sys.stdin:

        # Skip the line that stats with # line
        match = re.match("^#",line)

        #REPLACE THIS COMMENT - why is the code doing this?
        fields = line.strip().split(':')

        #REPLACE THESE COMMENTS with a single comment describing the logic of the IF 
        #what would an appropriate comment be for describing what this IF statement is checking for?
        #what happens if the IF statement evaluates to true?
        #how does this IF statement rely on what happened in the prior two lines of code? The match and fields lines.
        #the code clearly shows that the variables match and the length of fields is being checked for being != 5  so why is it doing that?
        if match or len(fields) != 5:
            continue

        #REPLACE THIS COMMENT - what is the purpose of the next three lines. How does it relate to what is stored in the passwd file?
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        #REPLACE THIS COMMENT - why is this split being done?
        groups = fields[4].split(',')

        #REPLACE THIS COMMENT - what is the point of this print statement?
        print("==> Creating account for %s..." % (username))
        #REPLACE THIS COMMENT - what is this line doing?  What will the variable "cmd" contain.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #REMOVE THIS COMMENT AFTER YOU UNDERSTAND WHAT TO DO - these statements are currently "commented out" as talked about in class
