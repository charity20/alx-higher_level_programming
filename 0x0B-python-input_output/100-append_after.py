#!/usr/bin/python3
"""insert a line of text"""


def append_after(filename="", search_string="", new_string=""):
    """insert a line of text to a file"""

    with open(filename, 'r+') as f:
        lines = f.readlines()

        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string + '\n')
