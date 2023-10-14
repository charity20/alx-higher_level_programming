#!/usr/bin/python3
"""insert a line of text"""


def append_after(filename="", search_string="", new_string=""):
    """insert a line of text to a file"""

    with open(filename, 'r') as f:
        lines = f.readlines()

    with open(filename, 'w') as fl:
        l = ''
        for line in lines:
            l += line
            if search_string in line:
                l += new_string
            fl.write(s)
