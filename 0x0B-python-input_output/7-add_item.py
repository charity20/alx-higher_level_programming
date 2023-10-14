#!/usr/bin/python3

"""add args to a python list"""

from sys import argv

load_file = __import__('6-load_from_json_file').load_from_json_file
save_file = __import__('5-save_to_json_file').save_to_json_file

list = []

try:
    list = list(load_file('add_item.json'))
except (ValueError, FileNotFoundError):
    list = []

for items in argv[1:]:
    list.append(item)

save_file(list, 'add_item.json')
