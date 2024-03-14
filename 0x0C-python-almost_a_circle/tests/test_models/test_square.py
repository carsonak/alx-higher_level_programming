#!/usr/bin/python3
"""Module for test_square."""
from io import StringIO
from unittest import TestCase, mock
from models.base import Base
# mock allows to mimic output of functions ands APIs
from models.square import Square


class RectangleTest(TestCase):
    """Tests for Square class."""

    def setUp(self):
        """Initialise square instances."""
        self.s1 = Square(3)
        self.s2 = Square(4, 2, 3)
        self.s70 = Square(7, 1, id=70)

    def tearDown(self):
        """Reset public class attribute."""
        setattr(Base, "_Base__nb_objects", 0)

    def test_rectangle_intiialsation(self):
        """Testing instance attributes have initialised properly."""
        self.assertEqual((self.s1.size, self.s1.x, self.s1.y, self.s1.id),
                         (3, 0, 0, 1), "Assert r1 attrs")
        self.assertEqual((self.s2.size, self.s2.x, self.s2.y, self.s2.id),
                         (4, 2, 3, 2), "Assert r2 attrs")
        self.assertEqual((self.s70.size, self.s70.x, self.s70.y, self.s70.id),
                         (7, 1, 0, 70), "Assert r70 attrs")

    def test_rectangle_area(self):
        """Testing the area() method."""
        self.assertEqual(self.s1.area(), (3 * 3), "Assert r1 area")
        self.assertEqual(self.s70.area(), (7 ** 2), "Assert r70 area")

    def test_rectangle_to_dictionary(self):
        """Testing the to_dictionary() method."""
        self.assertEqual(self.s2.to_dictionary(),
                         {'id': 2, 'size': 4, 'x': 2, 'y': 3})

    def test_rectangle_str(self):
        """Testing the __str__() magic method."""
        self.assertEqual(str(self.s1), "[Square] (1) 0/0 - 3")
        self.assertEqual(str(self.s2), "[Square] (2) 2/3 - 4")
        # patch in this case is used to replace stdout with string stream obj
        # https://docs.python.org/3/library/io.html#text-i-o
        # As sys.stdout has not been explicity imported in any module we can
        #   instead patch any stdout call from the sys module
        with mock.patch('sys.stdout', StringIO()) as mock_stdout:
            print(self.s70)
            self.assertEqual(mock_stdout.getvalue(),
                             "[Square] (70) 1/0 - 7\n")

    def test_rectangle_display(self):
        """Testing the display() method."""
        with mock.patch('sys.stdout', StringIO()) as mock_stdout:
            excepted_out: str = "###\n" * 3
            self.s1.display()
            self.assertEqual(mock_stdout.getvalue(), excepted_out)

        with mock.patch('sys.stdout', StringIO()) as mock_stdout:
            excepted_out = "\n\n\n" + (((" " * 2) + "####\n") * 4)
            self.s2.display()
            self.assertEqual(mock_stdout.getvalue(), excepted_out)

        with mock.patch('sys.stdout', StringIO()) as mock_stdout:
            excepted_out = (" " + ("#" * 7) + "\n") * 7
            self.s70.display()
            self.assertEqual(mock_stdout.getvalue(), excepted_out)

    def test_rectangle_update(self):
        """Testing the update() method."""
        self.s1.update()
        self.assertEqual((self.s1.id, self.s1.size, self.s1.x,
                         self.s1.y), (1, 3, 0, 0), "Assert r1")

        self.s1.update(99, 99, 99, 99, 99, 99, 99, 99, 99)
        self.assertEqual((self.s1.id, self.s1.size, self.s1.x,
                         self.s1.y), (99, 99, 99, 99), "Assert r1")
        self.s1.update(1, 2)
        self.assertEqual((self.s1.id, self.s1.size, self.s1.x,
                         self.s1.y), (1, 2, 99, 99), "Assert r1")
        self.s1.update(3, 4, 5, 6)
        self.assertEqual((self.s1.id, self.s1.size, self.s1.x,
                         self.s1.y), (3, 4, 5, 6), "Assert r1")
        self.s1.update(size=7, id=123, meno=45)
        self.assertEqual((self.s1.id, self.s1.size, self.s1.x,
                         self.s1.y), (123, 7, 5, 6), "Assert r1")
        self.s1.update(id=7, size=8, y=10, x=9)
        self.assertEqual((self.s1.id, self.s1.size, self.s1.x,
                         self.s1.y), (7, 8, 9, 10), "Assert r1")
        self.s1.update(1, 2, height=3, x=4)
        self.assertEqual((self.s1.id, self.s1.size, self.s1.x,
                         self.s1.y), (1, 2, 9, 10), "Assert r1")
        self.s1.update(1, 2, 3, 4, {"id": 77, "x": 3})
        self.assertEqual((self.s1.id, self.s1.size, self.s1.x,
                         self.s1.y), (1, 2, 3, 4), "Assert r1")

    def test_rectangle_update_ValueError(self):
        """Testing initialisation exceptions."""
        with self.assertRaises(ValueError, msg="size < 1"):
            self.s1.update(1, -4, 0)

        with self.assertRaises(ValueError, msg="size == 1"):
            self.s1.update(1, 0, 0)

        with self.assertRaises(ValueError, msg="x and y < 0"):
            self.s1.update(1, 4, -1, -5)

        with self.assertRaises(ValueError, msg="y < 0"):
            self.s1.update(1, 4, 5, -5)

        with self.assertRaises(ValueError, msg="size < 1 kwarg"):
            self.s1.update(size=0)

        with self.assertRaises(ValueError, msg="size < 1 kwarg"):
            self.s1.update(size=-7)

        with self.assertRaises(ValueError, msg="x <  kwarg"):
            self.s1.update(x=-4)

        with self.assertRaises(ValueError, msg="y <  kwarg"):
            self.s1.update(y=-4)

    def test_rectangle_update_TypeError(self):
        """Testing the update() method exceptions."""
        args_dict = {0: "id", 1: "size", 2: "x", 3: "y"}
        args_list = [1, 2, 3, 4]
        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = "99"
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="string arg"):
                    self.s1.update(cpy[0], cpy[1], cpy[2], cpy[3])

        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = (99, )
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="tuple arg"):
                    self.s1.update(cpy[0], cpy[1], cpy[2], cpy[3])

        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = [99]
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="list arg"):
                    self.s1.update(cpy[0], cpy[1], cpy[2], cpy[3])

        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = {"ninety-nine": 99}
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="dict arg"):
                    self.s1.update(cpy[0], cpy[1], cpy[2], cpy[3])

        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = 99.99
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="float arg"):
                    self.s1.update(cpy[0], cpy[1], cpy[2], cpy[3])

        for i in range(len(args_list) - 1):
            cpy = args_list[:]
            cpy[i] = None
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="None arg"):
                    self.s1.update(cpy[0], cpy[1], cpy[2], cpy[3])

        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = "99"
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="string kwarg"):
                    self.s1.update(id=cpy[0], size=cpy[1], x=cpy[2], y=cpy[3])

        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = (99, )
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="tuple kwarg"):
                    self.s1.update(id=cpy[0], size=cpy[1], x=cpy[2], y=cpy[3])

        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = [99]
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="list kwarg"):
                    self.s1.update(id=cpy[0], size=cpy[1], x=cpy[2], y=cpy[3])

        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = {"ninety-nine": 99}
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="dict kwarg"):
                    self.s1.update(id=cpy[0], size=cpy[1], x=cpy[2], y=cpy[3])

        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = 99.99
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="float kwarg"):
                    self.s1.update(id=cpy[0], size=cpy[1], x=cpy[2], y=cpy[3])

        for i in range(len(args_list) - 1):
            cpy = args_list[:]
            cpy[i] = None
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="None kwarg"):
                    self.s1.update(id=cpy[0], size=cpy[1], x=cpy[2], y=cpy[3])

    def test_rectangle_intialisation_ValueError(self):
        """Testing initialisation exceptions."""
        with self.assertRaises(ValueError, msg="size < 1"):
            Square(-4)

        with self.assertRaises(ValueError, msg="size == 0"):
            Square(0)

        with self.assertRaises(ValueError, msg="x and y < 0"):
            Square(4, -5, -1, 1)

        with self.assertRaises(ValueError, msg="y < 0"):
            Square(4, 5, -1, 1)

    def test_rectangle_intialisation_TypeError(self):
        """Testing initialisation TypeError exceptions."""
        with self.assertRaises(TypeError, msg="No size"):
            Square()

        args_dict = {0: "size", 1: "x", 2: "y", 3: "id"}
        args_list = [2, 3, 4, 1]
        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = "99"
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="string arg"):
                    Square(cpy[0], cpy[1], cpy[2], cpy[3])

        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = (99, )
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="tuple arg"):
                    Square(cpy[0], cpy[1], cpy[2], cpy[3])

        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = [99]
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="list arg"):
                    Square(cpy[0], cpy[1], cpy[2], cpy[3])

        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = {"ninety-nine": 99}
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="dict arg"):
                    Square(cpy[0], cpy[1], cpy[2], cpy[3])

        for i in range(len(args_list)):
            cpy = args_list[:]
            cpy[i] = 99.99
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="float arg"):
                    Square(cpy[0], cpy[1], cpy[2], cpy[3])

        for i in range(len(args_list) - 1):
            cpy = args_list[:]
            cpy[i] = None
            with self.subTest(arg=args_dict[i]):
                with self.assertRaises(TypeError, msg="None arg"):
                    Square(cpy[0], cpy[1], cpy[2], cpy[3])
