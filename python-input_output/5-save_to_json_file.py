#!/usr/bin/python3
"""
Save json in file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object in file formated in json
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
