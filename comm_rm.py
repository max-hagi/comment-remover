# Author: Maxime Savehilaghi

# README: This script will remove c++ formatted comments from a file passed as
# command-line argument

import sys


def removeComments(argv):
    f = open(argv, "r")
    f2 = open("inputC_rm.cpp", "w")

    quotes = False
    written = False
    multiline = False
    chars = []

    for line in f:
        written = False
        chars[:] = line

        # Scanning every character of the line
        for i in range(len(chars)):

            # Check for quotes
            if chars[i] == "\"":
                # Beginning of quote
                if quotes is False:
                    quotes = True
                # End of quote
                else:
                    quotes = False

            # Beginning symbol of comment
            if chars[i] == '/' and quotes is False and multiline is False:
                # Single line comment
                if chars[i + 1] == '/':
                    # Check if the remainder of the line is empty before writing
                    if len(line[:i]) != 0:
                        f2.write(line[:i] + "\n")
                    written = True
                    continue

                # Beginning of multiline comment
                if chars[i + 1] == "*":
                    f2.write(line[:i] + "\n")
                    written = True
                    multiline = True

            # End of multiline comment
            if multiline is True and quotes is False and chars[i] == "*":
                if chars[i + 1] == "/":
                    multiline = False
                    # Check if the remainder of the line is empty before writing
                    if len(line[i:]) != 0:
                        f2.write(line[i + 2:] + "\n")
                    written = True

        # No comments, write the hole line
        if not written and not multiline:
            if len(chars) != 0:
                f2.write(line + "\n")

    f.close()
    f2.close()


removeComments(sys.argv[1])
