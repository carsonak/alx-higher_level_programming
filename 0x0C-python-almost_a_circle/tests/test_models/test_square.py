#!/usr/bin/python3
"""Module for test_square."""
from unittest import mock
from unittest import TestCase
from io import StringIO
from models.base import Base
from models.square import Square


class RectangleTest(TestCase):
    """Tests for Square class."""

    def setUp(self):
        """Initialise square instances."""
        self.r1 = Square(3)
        self.r2 = Square(4, 2, 3)
        self.r70 = Square(7, 1, id=70)

    def tearDown(self):
        """Reset public class attribute."""
        setattr(Base, "_Base__nb_objects", 0)

    def test_rectangle_intiialsation(self):
        """Testing instance attributes have initialised properly."""
        self.assertEqual((self.r1.size, self.r1.x, self.r1.y, self.r1.id),
                         (3, 0, 0, 1), "Assert r1 attrs")
        self.assertEqual((self.r2.size, self.r2.x, self.r2.y, self.r2.id),
                         (4, 2, 3, 2), "Assert r2 attrs")
        self.assertEqual((self.r70.size, self.r70.x, self.r70.y, self.r70.id),
                         (7, 1, 0, 70), "Assert r70 attrs")

    def test_rectangle_area(self):
        """Testing the area() method."""
        self.assertEqual(self.r1.area(), (3 * 3), "Assert r1 area")
        self.assertEqual(self.r70.area(), (7 ** 2), "Assert r70 area")

    def test_rectangle_to_dictionary(self):
        """Testing the to_dictionary() method."""
        self.assertEqual(self.r2.to_dictionary(),
                         {'id': 2, 'size': 4, 'x': 2, 'y': 3})

    def test_rectangle_str(self):
        """Testing the __str__() magic method."""
        self.assertEqual(str(self.r1), "[Square] (1) 0/0 - 3")
        self.assertEqual(str(self.r2), "[Square] (2) 2/3 - 4")
        with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
            print(self.r70)
            self.assertEqual(mock_stdout.getvalue(),
                             "[Square] (70) 1/0 - 7\n")

    def test_rectangle_display(self):
        """Testing the display() method."""
        with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
            excepted_out: str = "###\n" * 3
            self.r1.display()
            self.assertEqual(mock_stdout.getvalue(), excepted_out)

        with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
            excepted_out = "\n\n\n" + (((" " * 2) + "####\n") * 4)
            self.r2.display()
            self.assertEqual(mock_stdout.getvalue(), excepted_out)

        with mock.patch('sys.stdout', new=StringIO()) as mock_stdout:
            excepted_out = (" " + ("#" * 7) + "\n") * 7
            self.r70.display()
            self.assertEqual(mock_stdout.getvalue(), excepted_out)

    def test_rectangle_update(self):
        """Testing the update() method."""
        self.r1.update()
        self.assertEqual((self.r1.id, self.r1.size, self.r1.x,
                         self.r1.y), (1, 3, 0, 0), "Assert r1")

        self.r1.update(99, 99, 99, 99, 99, 99, 99, 99, 99)
        self.assertEqual((self.r1.id, self.r1.size, self.r1.x,
                         self.r1.y), (99, 99, 99, 99), "Assert r1")
        self.r1.update(1, 2)
        self.assertEqual((self.r1.id, self.r1.size, self.r1.x,
                         self.r1.y), (1, 2, 99, 99), "Assert r1")
        self.r1.update(3, 4, 5, 6)
        self.assertEqual((self.r1.id, self.r1.size, self.r1.x,
                         self.r1.y), (3, 4, 5, 6), "Assert r1")
        self.r1.update(size=7, id=123, meno=45)
        self.assertEqual((self.r1.id, self.r1.size, self.r1.x,
                         self.r1.y), (123, 7, 5, 6), "Assert r1")
        self.r1.update(id=7, size=8, y=10, x=9)
        self.assertEqual((self.r1.id, self.r1.size, self.r1.x,
                         self.r1.y), (7, 8, 9, 10), "Assert r1")
        self.r1.update(1, 2, height=3, x=4)
        self.assertEqual((self.r1.id, self.r1.size, self.r1.x,
                         self.r1.y), (1, 2, 9, 10), "Assert r1")
        self.r1.update(1, 2, 3, 4, {"id": 77, "x": 3})
        self.assertEqual((self.r1.id, self.r1.size, self.r1.x,
                         self.r1.y), (1, 2, 3, 4), "Assert r1")

    def test_rectangle_update_ValueError(self):
        """Testing initialisation exceptions."""
        with self.assertRaises(ValueError, msg="size < 1"):
            self.r1.update(1, -4, 0)

        with self.assertRaises(ValueError, msg="size == 1"):
            self.r1.update(1, 0, 0)

        with self.assertRaises(ValueError, msg="x and y < 0"):
            self.r1.update(1, 4, -1, -5)

        with self.assertRaises(ValueError, msg="y < 0"):
            self.r1.update(1, 4, 5, -5)

        with self.assertRaises(ValueError, msg="size < 1 kwarg"):
            self.r1.update(size=0)

        with self.assertRaises(ValueError, msg="size < 1 kwarg"):
            self.r1.update(size=-7)

        with self.assertRaises(ValueError, msg="x <  kwarg"):
            self.r1.update(x=-4)

        with self.assertRaises(ValueError, msg="y <  kwarg"):
            self.r1.update(y=-4)

    def test_rectangle_update_TypeError(self):
        """Testing the update() method exceptions."""
        args_dict = {0: "id", 1: "size", 2: "x", 3: "y"}
        args_list = [1, 2, 3, 4]
        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = "99"
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="string arg"):
                    self.r1.update(cpy[0], cpy[1], cpy[2], cpy[3])

        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = (99, )
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="tuple arg"):
                    self.r1.update(cpy[0], cpy[1], cpy[2], cpy[3])

        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = [99]
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="list arg"):
                    self.r1.update(cpy[0], cpy[1], cpy[2], cpy[3])

        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = {"ninety-nine": 99}
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="dict arg"):
                    self.r1.update(cpy[0], cpy[1], cpy[2], cpy[3])

        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = 99.99
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="float arg"):
                    self.r1.update(cpy[0], cpy[1], cpy[2], cpy[3])

        for i in range(len(args_list) - 1):
            cpy = args_list[:]
            cpy[i] = None
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="None arg"):
                    self.r1.update(cpy[0], cpy[1], cpy[2], cpy[3])

        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = "99"
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="string kwarg"):
                    self.r1.update(id=cpy[0], size=cpy[1], x=cpy[2], y=cpy[3])

        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = (99, )
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="tuple kwarg"):
                    self.r1.update(id=cpy[0], size=cpy[1], x=cpy[2], y=cpy[3])

        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = [99]
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="list kwarg"):
                    self.r1.update(id=cpy[0], size=cpy[1], x=cpy[2], y=cpy[3])

        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = {"ninety-nine": 99}
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="dict kwarg"):
                    self.r1.update(id=cpy[0], size=cpy[1], x=cpy[2], y=cpy[3])

        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = 99.99
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="float kwarg"):
                    self.r1.update(id=cpy[0], size=cpy[1], x=cpy[2], y=cpy[3])

        for i in range(len(args_list) - 1):
            cpy = args_list[:]
            cpy[i] = None
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="None kwarg"):
                    self.r1.update(id=cpy[0], size=cpy[1], x=cpy[2], y=cpy[3])

    def test_rectangle_intialisation_ValueError(self):
        """Testing initialisation exceptions."""
        with self.assertRaises(ValueError, msg="size < 1"):
            r1 = Square(-4)

        with self.assertRaises(ValueError, msg="size == 0"):
            r1 = Square(0)

        with self.assertRaises(ValueError, msg="x and y < 0"):
            r1 = Square(4, -5, -1, 1)

        with self.assertRaises(ValueError, msg="y < 0"):
            r1 = Square(4, 5, -1, 1)

    def test_rectangle_intialisation_TypeError(self):
        """Testing initialisation TypeError exceptions."""
        with self.assertRaises(TypeError, msg="No size"):
            r1 = Square()

        args_dict = {0: "size", 1: "x", 2: "y", 3: "id"}
        args_list = [2, 3, 4, 1]
        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = "99"
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="string arg"):
                    r1 = Square(cpy[0], cpy[1], cpy[2], cpy[3])

        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = (99, )
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="tuple arg"):
                    r1 = Square(cpy[0], cpy[1], cpy[2], cpy[3])

        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = [99]
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="list arg"):
                    r1 = Square(cpy[0], cpy[1], cpy[2], cpy[3])

        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = {"ninety-nine": 99}
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="dict arg"):
                    r1 = Square(cpy[0], cpy[1], cpy[2], cpy[3])

        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = 99.99
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="float arg"):
                    r1 = Square(cpy[0], cpy[1], cpy[2], cpy[3])

        for i in range(len(args_list) - 1):
            cpy = args_list[:]
            cpy[i] = None
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="None arg"):
                    r1 = Square(cpy[0], cpy[1], cpy[2], cpy[3])
