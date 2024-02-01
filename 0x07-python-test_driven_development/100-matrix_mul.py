#!/usr/bin/python3
"""Module for multipying matrices"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices, raise exceptions on invalid input"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    elif type(m_b) is not list:
        raise TypeError("m_b must be a list")

    clen_a, clen_b = len(m_a), len(m_b)
    if clen_a > 0 and type(m_a[0]) is not list:
        raise TypeError("m_a must be a list of lists")
    elif clen_b > 0 and type(m_b[0]) is not list:
        raise TypeError("m_b must be a list of lists")

    if clen_a < 1 or (clen_a == 1 and len(m_a[0]) < 1):
        raise ValueError("m_a can't be empty")
    elif clen_b < 1 or (clen_b == 1 and len(m_b[0]) < 1):
        raise ValueError("m_b can't be empty")

    rlen_a, rlen_b = len(m_a[0]), len(m_b[0])
    m_res = []
    # Iterate through every row of m_a
    for roa in range(clen_a):
        m_res.append([0] * rlen_b)
        # Iterate through every column of m_b
        for cob in range(rlen_b):
            for rob in range(clen_b):
                if type(m_a[roa][rob]) is not int and \
                        type(m_a[roa][rob]) is not float:
                    raise TypeError(
                        "m_a should contain only integers or floats")
                elif type(m_b[rob][cob]) is not int and \
                        type(m_b[rob][cob]) is not float:
                    raise TypeError(
                        "m_b should contain only integers or floats")

                if len(m_b[rob]) != rlen_b:
                    raise TypeError(
                        "each row of m_b must be of the same size")
                elif cob < 1 and len(m_a[roa]) != rlen_a:
                    raise TypeError(
                        "each row of m_a must be of the same size")
                # No. of cols in m_a should be equal to No. of rows in m_b
                if cob < 1 and len(m_a[roa]) != clen_b:
                    raise ValueError("m_a and m_b can't be multiplied")

                m_res[roa][cob] += m_a[roa][rob] * m_b[rob][cob]

    return m_res


if __name__ == "__main__":
    """print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
    print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
    mat_a = [[2, 3, 4],
             [5, 6, 7],
             [8, 9, 10],
             [11, 12, 13],
             [14, 15, 16],
             [17, 18, 19]]
    mat_b = [[2, 3, 4, 5],
             [6, 7, 8, 9],
             [10, 11, 12, 13]]
    print(matrix_mul(mat_a, mat_b))
    mat_a = [[2, 3, 4, 5, 6, 7],
             [8, 9, 10, 11, 12, 13]]
    mat_b = [[2, 3, 4, 5],
             [6, 7, 8, 9],
             [10, 11, 12, 13],
             [14, 15, 16, 17],
             [18, 19, 20, 21],
             [22, 23, 24, 25]]
    print(matrix_mul(mat_a, mat_b))
    mat_a = [[1, 0, 0],
             [0, 1, 0],
             [0, 0, 1]]
    mat_b = [[8, 9, 10],
             [2, 3, 4],
             [5, 6.0, 7]]
    print(matrix_mul(mat_a, mat_b))"""
    mat_a = [[5, 6, 7], [8, 9], [2, 3, 4]]
    mat_b = [[2, 3], [4, 5], [5, 6]]
    print(matrix_mul(mat_a, mat_b))
