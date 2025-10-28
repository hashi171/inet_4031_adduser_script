#!/usr/bin/python3
# INET4031
# Duale Hashi
# Step 7 – Interactive Dry Run Version
# This version allows the user to choose whether to do a dry-run (simulate commands)
# or run the real user creation. Dry-run mode prevents any system changes.

import os
import re
import sys

def main():
    # Ask user whether to run in dry-run mode or normal mode
    dry_run = input("Run in dry-run mode? (Y/N): ").strip().upper() == "Y"

    # Ask user which input file to use
    filename = input("Please enter the file to process: ")

    # Open the input file and process line by line
    with open(filename, 'r') as infile:
        for line in infile:
            # Detect comment lines (starting with '#')
            match = re.match("^#", line)

            # Split line into fields separated by ':'
            fields = line.strip().split(':')

            # Skip comment lines or lines missing fields
            if match or len(fields) != 5:
                if dry_run:
                    print(f"[Dry Run] Skipping line: {line.strip()} (comment or missing fields)")
                continue

            username = fields[0]
            password = fields[1]
            gecos = "%s %s,,," % (fields[3], fields[2])
            groups = fields[4].split(',')

            print(f"==> Creating account for {username}...")

            # Build the command that would create the user
            cmd1 = f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}"
            if dry_run:
                print(f"[Dry Run] Would run: {cmd1}")
            else:
                os.system(cmd1)

            print(f"==> Setting password for {username}...")
            # Build the command that would set the password
            cmd2 = f"/bin/echo -ne '{password}\\n{password}' | /usr/bin/sudo /usr/bin/passwd {username}"
            if dry_run:
                print(f"[Dry Run] Would run: {cmd2}")
            else:
                os.system(cmd2)

            # Add user to any groups listed
            for group in groups:
                if group != '-':
                    cmd3 = f"/usr/sbin/adduser {username} {group}"
                    print(f"==> Assigning {username} to group {group}...")
                    if dry_run:
                        print(f"[Dry Run] Would run: {cmd3}")
                    else:
                        os.system(cmd3)

if __name__ == '__main__':
    main()
