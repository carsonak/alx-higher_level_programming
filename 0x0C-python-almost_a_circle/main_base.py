#!/usr/bin/python3
"""Module for main_base."""
import random
import uuid
import json
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


def list_of_random_recs_sqrs(n=5):
    """Return a list of n random rectangles and squares."""
    list_o_recs = []
    for i in range(n):
        list_o_recs.append(Rectangle(random.randrange(1, 100, 2),
                                     random.randrange(1, 100, 2),
                                     random.randrange(1, 100, 2),
                                     random.randrange(1, 100, 2)))
        list_o_recs.append(Square(random.randrange(1, 100, 2),
                                  random.randrange(1, 100, 2),
                                  random.randrange(1, 100, 2)))

    return list_o_recs


def sqr_rec_objs_to_dict(*objects: Rectangle | Square, tracker=None):
    """Return a list of dictionaries from a list of sqr and rec objects."""
    list_of_dicts = []
    for obj in objects:
        list_of_dicts.append(obj.to_dictionary())
        if type(tracker) is dict:
            tracker[obj.id] = list_of_dicts[-1]

    return list_of_dicts


def test_base_to_json_string():
    """Test to_json_string converts items properly."""
    map_dictionaries = {}
    list_dictionaries = list_of_random_recs_sqrs()
    list_dictionaries = sqr_rec_objs_to_dict(
        tracker=map_dictionaries, *list_dictionaries)
    for i in range(0, 5):
        rd = {"id": (len(list_dictionaries) + 10),
              "name": str(uuid.uuid4())}
        list_dictionaries.append(rd)
        map_dictionaries[rd.get("id")] = rd

    rjson = Base.to_json_string(list_dictionaries)
    if rjson is None:
        print("to_json_string is not returning a string")
        exit(1)

    output_list: list[dict] = json.loads(rjson)
    for output in output_list:
        id_output = output.get("id")
        if id_output is None:
            break
        dict_output = map_dictionaries.get(id_output)
        if dict_output is None:
            break
        if dict_output != output:
            break
        del map_dictionaries[id_output]

    if len(map_dictionaries) != 0:
        print("to_json_string doesn't correctly serialize {}: {}".format(
            list_dictionaries, rjson))
        exit(1)

    print("OK")


if __name__ == "__main__":
    test_base_to_json_string()
