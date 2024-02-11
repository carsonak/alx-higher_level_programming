#!/usr/bin/python3
"""Module for save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write a python object to a JSON txt file

    Args:
        my_obj (any): A python object
        filename (any): the file to be written to
    """

    with open(file=filename, mode="w", encoding="utf-8") as afile:
        json.dump(fp=afile, obj=my_obj)


if __name__ == "__main__":
    filename = "my_list.json"
    my_list = [1, 2, 3]
    save_to_json_file(my_list, filename)

    filename = "my_dict.json"
    my_dict = {
        'id': 12,
        'name': "John",
        'places': ["San Francisco", "Tokyo"],
        'is_active': True,
        'info': {
            'age': 36,
            'average': 3.14
        }
    }
    save_to_json_file(my_dict, filename)

    try:
        filename = "my_set.json"
        my_set = {132, 3}
        save_to_json_file(my_set, filename)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
