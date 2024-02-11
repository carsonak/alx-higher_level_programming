#!/usr/bin/python3
"""Module for function pascal_triangle"""


def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle of order n"""

    pal = []
    if n > 0:
        for g in range(n):
            row = []
            if g > 0:
                for h in range(len(pal[g - 1])):
                    if h > 0:
                        row.append(pal[g-1][h-1] + pal[g-1][h])
                    else:
                        row.append(1)

            row.append(1)
            pal.append(row)

    return pal


if __name__ == "__main__":
    def print_triangle(triangle):
        """Print the triangle"""

        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print_triangle(pascal_triangle(1))
    print_triangle(pascal_triangle(2))
    print_triangle(pascal_triangle(3))
    print_triangle(pascal_triangle(9))
    print_triangle(pascal_triangle(0))
    print_triangle(pascal_triangle(-2))
