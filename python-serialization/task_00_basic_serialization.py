#!/usr/bin/python3
"""serialize dictonaty in json-file and json-file in dictonary."""


import json


def serialize_and_save_to_file(data, filename):
    """Serializes a dictionary and saves it as a JSON file."""
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Uploads a JSON file and converts it into a dictionary."""
    with open(filename, 'r') as f:
        return json.load(f)
