#!/usr/bin/python3
"""Module for loading and dumping a args in a list to a JSON file"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


if __name__ == "__main__":
    try:
        jlist = load_from_json_file("add_item.json")
    except FileNotFoundError:
        jlist = []

    if len(sys.argv) > 1:
        jlist.extend(sys.argv[1:])

    save_to_json_file(jlist, "add_item.json")
