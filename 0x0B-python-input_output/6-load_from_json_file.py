#!/usr/bin/python3

"""create an object from a json file"""

import json


def load_from_json_file(filename):
    """create json object from json file"""

    with open(filename, 'r') as f:
        data = json.load(f)
        return data
