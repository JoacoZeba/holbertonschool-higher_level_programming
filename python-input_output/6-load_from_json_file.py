#!/usr/bin/python3
"""
Load from json in file
"""
import json


def load_from_json_file(filename):
    """
    load an object located in file formated in json
    """
    with open(filename, encoding="utf-8") as file:
        json.load(file)
