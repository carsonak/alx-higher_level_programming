#!/usr/bin/python3
"""Module for test_base."""
import unittest
import random
import uuid
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
# mock allows to mimic output of functions ands APIs
from unittest import TestCase, mock


class BaseTest(TestCase):
    """Tests for Base class."""

    def setUp(self):
        """Initialise Base instances."""
        self.b1 = Base()
        self.b2 = Base()
        setattr(Base, "_Base__nb_objects", 0)
        self.r1 = Rectangle(3, 5)
        self.r2 = Rectangle(4, 6, 4, 2)
        setattr(Base, "_Base__nb_objects", 0)
        self.s1 = Square(3)
        self.s2 = Square(4, 2, 3)

        self.b74 = Base(74)
        self.s70 = Square(7, 1, id=70)
        self.r7800 = Rectangle(7, 8, id=7800)

    def tearDown(self):
        """Reset public class attribute."""
        setattr(Base, "_Base__nb_objects", 0)

    def test_base_init(self):
        """Test if Base.id initialises properly."""
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 2)
        self.assertEqual(self.b74.id, 74)

    def test_base_to_json_string_non_dicts(self):
        """Test to_json_string handles incorrect lists properly."""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        with self.assertRaises(TypeError, msg="List of mixed objects."):
            Base.to_json_string([{}, {}, None, {}])

    @staticmethod
    def list_of_random_recs_sqrs(n=5):
        """Return a list of n random rectangles and squares."""
        list_o_recs = []
        for i in range(n):
            if i % 2:
                list_o_recs.append(Rectangle(random.randrange(1, 100, 2),
                                             random.randrange(1, 100, 2),
                                             random.randrange(1, 100, 2),
                                             random.randrange(1, 100, 2)))
            else:
                list_o_recs.append(Square(random.randrange(1, 100, 2),
                                          random.randrange(1, 100, 2),
                                          random.randrange(1, 100, 2)))

        return list_o_recs

    @staticmethod
    def sqr_rec_objs_to_dict(*objects, tracker=None):
        """Return a list of dictionaries from a list of sqr and rec objects."""
        list_of_dicts = []
        for obj in objects:
            list_of_dicts.append(obj.to_dictionary())
            if type(tracker) is dict:
                tracker[obj.id] = list_of_dicts[-1]

        return list_of_dicts

    def test_base_save_to_file(self):
        """Test save_to_file."""
        # patch() here is used as a context manager to replace the
        #   open() call in models.base
        # https://docs.python.org/3/library/unittest.mock.html#patch
        #
        # The mock_open() function allows us to mimic the builtin open()
        # function
        # https://docs.python.org/3/library/unittest.mock.html#patch
        with mock.patch("models.base.open", new=mock.mock_open()) as fake_open:
            excepted_out = \
                '[{"x": 0, "y": 0, "id": 1, "height": 5, "width": 3}, \
{"x": 4, "y": 2, "id": 2, "height": 6, "width": 4}, \
{"x": 0, "y": 0, "id": 7800, "height": 8, "width": 7}]'
            Base.save_to_file([self.r1, self.r2, self.r7800])
            # We can assert that our fake_open() was called once with a
            #   specific set of parameters
            fake_open.assert_called_once_with(
                "./Rectangle.json", "w", encoding='UTF-8')
            # Calling our fake_open() will yield a new Mock object
            # which has an attribute called write that we can conveniently
            # assert
            # https://docs.python.org/3/library/unittest.mock.html#calling
            fake_open().write.assert_called_once_with(excepted_out)

        with mock.patch("models.base.open", new=mock.mock_open()) as fake_open:
            excepted_out = '[{"id": 1, "size": 3, "x": 0, "y": 0}, \
{"id": 2, "size": 4, "x": 2, "y": 3}, \
{"id": 70, "size": 7, "x": 1, "y": 0}]'
            Base.save_to_file([self.s1, self.s2, self.s70])
            fake_open.assert_called_once_with(
                "./Square.json", "w", encoding='UTF-8')
            fake_open().write.assert_called_once_with(excepted_out)

        with mock.patch("models.base.open", new=mock.mock_open()) as fake_open:
            excepted_out = '[]'
            Base.save_to_file([])
            fake_open.assert_has_calls([
                mock.call("./Square.json", "w", encoding='UTF-8'),
                mock.call("./Rectangle.json", "w", encoding='UTF-8')],
                any_order=True)
            fake_open().write.assert_has_calls([
                mock.call(excepted_out), mock.call(excepted_out)],
                any_order=True)

        with mock.patch("models.base.open", new=mock.mock_open()) as fake_open:
            excepted_out = '[]'
            Base.save_to_file(None)
            fake_open.assert_has_calls([
                mock.call("./Square.json", "w", encoding='UTF-8'),
                mock.call("./Rectangle.json", "w", encoding='UTF-8')],
                any_order=True)
            fake_open().write.assert_has_calls([
                mock.call(excepted_out), mock.call(excepted_out)],
                any_order=True)

    def test_base_save_to_file_exceptions(self):
        """Test save_to_file exceptions."""
        with self.assertRaises(TypeError, msg="Incorrect type: No args."):
            Base.save_to_file()

        with self.assertRaises(TypeError, msg="Incorrect type: string."):
            Base.save_to_file("list")

        with self.assertRaises(TypeError, msg="Incorrect type: Dictionary."):
            Base.save_to_file({})

        with self.assertRaises(TypeError, msg="Incorrect type: Int."):
            Base.save_to_file(44)

        with self.assertRaises(TypeError, msg="Incorrect type: Float"):
            Base.save_to_file(2.8)

        with self.assertRaises(TypeError, msg="Incorrect type: Tuple."):
            Base.save_to_file(())

    def test_base_to_json_string(self):
        """Test to_json_string converts items properly."""
        map_dictionaries = {}
        list_dictionaries = self.list_of_random_recs_sqrs()
        list_dictionaries = self.sqr_rec_objs_to_dict(*list_dictionaries,
                                                      tracker=map_dictionaries)
        for i in range(0, 5):
            rd = {"id": (len(list_dictionaries) + 10),
                  "name": str(uuid.uuid4())}
            list_dictionaries.append(rd)
            map_dictionaries[rd.get("id")] = rd

        rjson = Base.to_json_string(list_dictionaries)
        self.assertIsNotNone(
            rjson, msg="to_json_string is not returning a string")

        output_list = json.loads(rjson)
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

        self.assertEqual(len(map_dictionaries), 0,
                         f"to_json_string doesn't correctly serialize \
                            {list_dictionaries}: {rjson}")

    def test_from_json_string(self):
        """Test from_json_string."""
        list_output = [{"id": 1, "size": 3, "x": 0, "y": 0},
                       {"id": 2, "size": 4, "x": 2, "y": 3},
                       {"id": 70, "size": 7, "x": 1, "y": 0}]
        string_input = '[{"id": 1, "size": 3, "x": 0, "y": 0}, \
{"id": 2, "size": 4, "x": 2, "y": 3}, \
{"id": 70, "size": 7, "x": 1, "y": 0}]'

        self.assertEqual(Base.from_json_string(string_input), list_output)
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string("[1, 2, 3]"), [1, 2, 3])

    def polygon_test(self, poly, **keys):
        """Assert all polygon attributes."""
        polygon_attrs = {"size": 0, "width": 0, "height": 0,
                         "x": 0, "y": 0, "id": 0}
        polygon_attrs.update(keys)
        if polygon_attrs["size"]:
            polygon_attrs["height"] = polygon_attrs["size"]
            polygon_attrs["width"] = polygon_attrs["size"]

        for attr, val in polygon_attrs.items():
            with self.subTest(attr=attr, val=val):
                self.assertEqual(getattr(poly, attr, 0), val)

    def test_create(self):
        """Test create static method."""
        rec_attrs = {"width": 3, "height": 6, "x": 4, "y": 5, "id": 3645}
        rec = Base.create(**rec_attrs)
        self.polygon_test(rec, **rec_attrs)

        sqr_attrs = {"size": 7, "x": 1, "y": 2, "id": 712}
        sqr = Base.create(**sqr_attrs)
        self.polygon_test(sqr, **sqr_attrs)

        rec_attrs = {"id": 2200}
        rec = Base.create(**rec_attrs)
        self.polygon_test(rec, **{"width": 2, "height": 2, "id": 2200})

        sqr_attrs = {"size": 7, "id": 700}
        sqr = Base.create(**sqr_attrs)
        self.polygon_test(sqr, **sqr_attrs)

    def test_load_from_file(self):
        """Test load_from_file."""
        sqr_list = [{"id": 1, "size": 3, "x": 0, "y": 0},
                    {"id": 2, "size": 4, "x": 2, "y": 3},
                    {"id": 70, "size": 7, "x": 1, "y": 0}]
        rec_list = [{"x": 0, "y": 0, "id": 1, "height": 5, "width": 3},
                    {"x": 4, "y": 2, "id": 2, "height": 6, "width": 4},
                    {"x": 0, "y": 0, "id": 7800, "height": 8, "width": 7}]

        with mock.patch("models.base.open",
                        new=mock.mock_open(read_data=json.dumps(sqr_list))) \
                as fake_file:
            sqr_instances = Square.load_from_file()
            fake_file.assert_called_once_with(
                "./Square.json", encoding="UTF-8")

        for i, poly in enumerate(sqr_instances):
            self.polygon_test(poly, **sqr_list[i])

        with mock.patch("models.base.open",
                        new=mock.mock_open(read_data=json.dumps(rec_list))) \
                as fake_file:
            rec_instances = Rectangle.load_from_file()
            fake_file.assert_called_once_with(
                "./Rectangle.json", encoding="UTF-8")

        for i, poly in enumerate(rec_instances):
            self.polygon_test(poly, **rec_list[i])


if __name__ == '__main__':
    unittest.main()
