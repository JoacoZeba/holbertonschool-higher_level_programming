#!/usr/bin/python3
"""
Load from json in file
"""
import sys


sj = __import__("5-save_to_json_file").save_to_json_file
lj = __import__("6-load_from_json_file").load_from_json_file
av = sys.argv[1:]

try:
    data = lj("add_item.json")
except FileNotFoundError:
    data = []

data.extend(av)
sj(data, "add_item.json")
