#!/usr/bin/python3
for digit in range(10):
    for one_digit in range(digit + 1, 10):
        print("{:02d}".format(digit * 10 + one_digit), end=", " 
                if digit < 8 or one_digit < 9 
                else "\n")
