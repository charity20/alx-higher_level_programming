#!/usr/bin/python3
def uppercase(s):
    for i in range(len(s)):
        char = ord(s[i])
        if 97 <= char <= 122:
            char = char - 32
        print("{:c}".format(char), end="")
    print()
