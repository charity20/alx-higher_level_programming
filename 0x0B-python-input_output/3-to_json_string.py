#!/usr/bin/python3

"""Return JSON representation"""

import json


def to_json_string(my_obj):
    """Serialize an object in JSON"""

    return json.dumps(my_obj)
