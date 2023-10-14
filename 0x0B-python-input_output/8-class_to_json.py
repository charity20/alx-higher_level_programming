#!/usr/bin/python3


def class_to_json(obj):
    """check the object data type"""

    if isinstance(obj, dict):
        result = {}

        for key, value in obj.items():
            result[key] = class_to_json(value)
        return result
    elif isinstance(obj, list):
        result = [class_to_json(item) for item in obj]
        return result
    elif isinstance(obj, (str, int, bool)):
        return obj
    else:
        return str(obj)
