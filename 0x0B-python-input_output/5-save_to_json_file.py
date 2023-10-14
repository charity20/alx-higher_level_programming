#!/usr/bin/python3

import json


def save_to_json_file(my_obj, filename):
    """convert objen with json string to txt file"""

    with open(filename, 'w') as f:
        filename = f.write(json.dumps(my_obj))
    return filename
