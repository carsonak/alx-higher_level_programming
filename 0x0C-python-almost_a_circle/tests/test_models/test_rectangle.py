#!/usr/bin/python3
"""Module for test_rectangle."""

from models.rectangle import Rectangle
from models.base import Base
from io import StringIO
# mock allows to mimic output of functions ands APIs
from unittest import TestCase, mock


class RectangleTest(TestCase):
    """Tests for Rectangle class."""

    def setUp(self):
        """Initialise rectangle instances."""
        self.r1 = Rectangle(3, 5)
        self.r2 = Rectangle(4, 6, 4, 2)
        self.r7800 = Rectangle(7, 8, id=7800)
        self.r3 = Rectangle(2, 2, 7)

    def tearDown(self):
        """Reset public class attribute."""
        setattr(Base, "_Base__nb_objects", 0)

    def test_rectangle_intiialsation(self):
        """Testing instance attributes have initialised properly."""
        self.assertEqual((self.r1.width, self.r1.height, self.r1.x, self.r1.y,
                          self.r1.id), (3, 5, 0, 0, 1), "Assert r1 attrs")
        self.assertEqual((self.r2.width, self.r2.height, self.r2.x, self.r2.y,
                          self.r2.id), (4, 6, 4, 2, 2), "Assert r2 attrs")
        self.assertEqual((self.r7800.width, self.r7800.height, self.r7800.x,
                          self.r7800.y, self.r7800.id), (7, 8, 0, 0, 7800),
                         "Assert r7800 attrs")
        self.assertEqual((self.r3.width, self.r3.height, self.r3.x, self.r3.y,
                          self.r3.id), (2, 2, 7, 0, 3), "Assert r3 attrs")

    def test_rectangle_area(self):
        """Testing the area() method."""
        self.assertEqual(self.r1.area(), (3 * 5), "Assert r1 area")
        self.assertEqual(self.r3.area(), (2 * 2), "Assert r3 area")

    def test_rectangle_to_dictionary(self):
        """Testing the to_dictionary() method."""
        self.assertEqual(self.r3.to_dictionary(),
                         {'x': 7, 'y': 0, 'id': 3, 'height': 2, 'width': 2})

    def test_rectangle_str(self):
        """Testing the __str__() magic method."""
        self.assertEqual(str(self.r1), "[Rectangle] (1) 0/0 - 3/5")
        self.assertEqual(str(self.r2), "[Rectangle] (2) 4/2 - 4/6")
        self.assertEqual(str(self.r7800), "[Rectangle] (7800) 0/0 - 7/8")
        with mock.patch('sys.stdout', StringIO()) as mock_stdout:
            print(self.r3)
            self.assertEqual(mock_stdout.getvalue(),
                             "[Rectangle] (3) 7/0 - 2/2\n")

    def test_rectangle_display(self):
        """Testing the display() method."""
        with mock.patch('sys.stdout', StringIO()) as mock_stdout:
            excepted_out = "###\n" * 5
            self.r1.display()
            self.assertEqual(mock_stdout.getvalue(), excepted_out)

        with mock.patch('sys.stdout', StringIO()) as mock_stdout:
            excepted_out = "\n\n" + (((" " * 4) + "####\n") * 6)
            self.r2.display()
            self.assertEqual(mock_stdout.getvalue(), excepted_out)

        with mock.patch('sys.stdout', StringIO()) as mock_stdout:
            excepted_out = ((" " * 7) + "##\n") * 2
            self.r3.display()
            self.assertEqual(mock_stdout.getvalue(), excepted_out)

    def test_rectangle_update(self):
        """Testing the update() method."""
        self.r1.update()
        self.assertEqual((self.r1.id, self.r1.width, self.r1.height,
                         self.r1.x, self.r1.y), (1, 3, 5, 0, 0),
                         "Assert r1")

        self.r1.update(99, 99, 99, 99, 99, 99, 99, 99, 99)
        self.assertEqual((self.r1.id, self.r1.width, self.r1.height,
                         self.r1.x, self.r1.y), (99, 99, 99, 99, 99),
                         "Assert r1")
        self.r1.update(1, 2)
        self.assertEqual((self.r1.id, self.r1.width, self.r1.height,
                         self.r1.x, self.r1.y), (1, 2, 99, 99, 99),
                         "Assert r1")
        self.r1.update(3, 4, 5, 6, 7)
        self.assertEqual((self.r1.id, self.r1.width, self.r1.height,
                         self.r1.x, self.r1.y), (3, 4, 5, 6, 7),
                         "Assert r1")
        self.r1.update(width=8, id=123, meno=45)
        self.assertEqual((self.r1.id, self.r1.width, self.r1.height,
                         self.r1.x, self.r1.y), (123, 8, 5, 6, 7),
                         "Assert r1")
        self.r1.update(width=9, id=8, height=10, y=12, x=11)
        self.assertEqual((self.r1.id, self.r1.width, self.r1.height,
                         self.r1.x, self.r1.y), (8, 9, 10, 11, 12),
                         "Assert r1")
        self.r1.update(1, 2, height=3, x=4)
        self.assertEqual((self.r1.id, self.r1.width, self.r1.height,
                         self.r1.x, self.r1.y), (1, 2, 10, 11, 12),
                         "Assert r1")
        self.r1.update(1, 2, 3, 4, 5, {"id": 77, "x": 3})
        self.assertEqual((self.r1.id, self.r1.width, self.r1.height,
                         self.r1.x, self.r1.y), (1, 2, 3, 4, 5),
                         "Assert r1")

    def test_rectangle_update_ValueError(self):
        """Testing initialisation exceptions."""
        with self.assertRaises(ValueError, msg="width and height < 1"):
            self.r1.update(1, -4, 0)

        with self.assertRaises(ValueError, msg="height < 1"):
            self.r1.update(1, 4, 0)

        with self.assertRaises(ValueError, msg="x and y < 0"):
            self.r1.update(1, 4, 5, -1, -5)

        with self.assertRaises(ValueError, msg="y < 0"):
            self.r1.update(1, 4, 5, -1, -5)

        with self.assertRaises(ValueError, msg="width < 1 kwarg"):
            self.r1.update(width=0)

        with self.assertRaises(ValueError, msg="height < 1 kwarg"):
            self.r1.update(height=-7)

        with self.assertRaises(ValueError, msg="x <  kwarg"):
            self.r1.update(x=-4)

        with self.assertRaises(ValueError, msg="y <  kwarg"):
            self.r1.update(y=-4)

    def test_rectangle_update_TypeError(self):
        """Testing the update() method exceptions."""
        args_dict = {0: "width", 1: "height", 2: "x", 3: "y", 4: "id"}
        args_list = [1, 2, 3, 4, 5]
        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = "99"
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="string arg"):
                    self.r1.update(cpy[0], cpy[1], cpy[2], cpy[3], cpy[4])

        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = (99, )
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="tuple arg"):
                    self.r1.update(cpy[0], cpy[1], cpy[2], cpy[3], cpy[4])

        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = [99]
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="list arg"):
                    self.r1.update(cpy[0], cpy[1], cpy[2], cpy[3], cpy[4])

        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = {"ninety-nine": 99}
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="dict arg"):
                    self.r1.update(cpy[0], cpy[1], cpy[2], cpy[3], cpy[4])

        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = 99.99
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="float arg"):
                    self.r1.update(cpy[0], cpy[1], cpy[2], cpy[3], cpy[4])

        for i in range(len(args_list) - 1):
            cpy = args_list[:]
            cpy[i] = None
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="None arg"):
                    self.r1.update(cpy[0], cpy[1], cpy[2], cpy[3], cpy[4])

        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = "99"
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="string kwarg"):
                    self.r1.update(width=cpy[0], id=cpy[1], height=cpy[2],
                                   x=cpy[3], y=cpy[4])

        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = (99, )
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="tuple kwarg"):
                    self.r1.update(width=cpy[0], id=cpy[1], height=cpy[2],
                                   x=cpy[3], y=cpy[4])

        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = [99]
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="list kwarg"):
                    self.r1.update(width=cpy[0], id=cpy[1], height=cpy[2],
                                   x=cpy[3], y=cpy[4])

        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = {"ninety-nine": 99}
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="dict kwarg"):
                    self.r1.update(width=cpy[0], id=cpy[1], height=cpy[2],
                                   x=cpy[3], y=cpy[4])

        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = 99.99
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="float kwarg"):
                    self.r1.update(width=cpy[0], id=cpy[1], height=cpy[2],
                                   x=cpy[3], y=cpy[4])

        for i in range(len(args_list) - 1):
            cpy = args_list[:]
            cpy[i] = None
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="None kwarg"):
                    self.r1.update(width=cpy[0], id=cpy[1], height=cpy[2],
                                   x=cpy[3], y=cpy[4])

    def test_rectangle_intialisation_ValueError(self):
        """Testing initialisation exceptions."""
        with self.assertRaises(ValueError, msg="Width and height < 1"):
            Rectangle(0, -4)

        with self.assertRaises(ValueError, msg="height < 1"):
            Rectangle(7, -4)

        with self.assertRaises(ValueError, msg="x and y < 0"):
            Rectangle(3, 5, -1, -5)

        with self.assertRaises(ValueError, msg="y < 0"):
            Rectangle(3, 5, 1, -5)

    def test_rectangle_intialisation_TypeError(self):
        """Testing initialisation TypeError exceptions."""
        with self.assertRaises(TypeError, msg="No width and height"):
            Rectangle()

        with self.assertRaises(TypeError, msg="No height"):
            Rectangle(5)

        args_dict = {0: "width", 1: "height", 2: "x", 3: "y", 4: "id"}
        args_list = [1, 2, 3, 4, 5]
        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = "99"
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="string arg"):
                    Rectangle(cpy[0], cpy[1], cpy[2], cpy[3], cpy[4])

        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = (99, )
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="tuple arg"):
                    Rectangle(cpy[0], cpy[1], cpy[2], cpy[3], cpy[4])

        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = [99]
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="list arg"):
                    Rectangle(cpy[0], cpy[1], cpy[2], cpy[3], cpy[4])

        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = {"ninety-nine": 99}
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="dict arg"):
                    Rectangle(cpy[0], cpy[1], cpy[2], cpy[3], cpy[4])

        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = 99.99
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="float arg"):
                    Rectangle(cpy[0], cpy[1], cpy[2], cpy[3], cpy[4])

        for i in range(len(args_list) - 1):
            cpy = args_list[:]
            cpy[i] = None
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="None arg"):
                    Rectangle(cpy[0], cpy[1], cpy[2], cpy[3], cpy[4])
