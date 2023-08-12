#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import *
    import sys
    args_len = len(sys.argv)
    if args_len != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operation = sys.argv[2]

    if operation == '+':
        print("{} {} {} = {}".format(a, operation, b, add(a, b)))
    elif operation == '-':
        print("{} {} {} = {}".format(a, operation, b, sub(a, b)))
    elif operation == '*':
        print("{} {} {} = {}".format(a, operation, b, mul(a, b)))
    elif operation == '/':
        print("{} {} {} = {}".format(a, operation, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
