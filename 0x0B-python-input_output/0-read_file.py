#!/usr/bin/python3
"""Open file and eead it to stdoutput"""


def read_file(filename=""):
    """open file and rename the file as f then read it to std output"""

    with open(filename, 'r', encoding='utf-8') as f:
        read_data = f.read()
        print(read_data, end='')
