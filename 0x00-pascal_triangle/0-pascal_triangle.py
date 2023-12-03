#!/usr/bin/python3
"""Pascal triangle """


def pascal_triangle(n):
    """returns list of lists"""
    triangle_elements = []
    for row in range(n):
        temp_elements = []
        for column in range(row + 1):
            if column == 0 or column == row:
                temp_elements.append(1)
            else:
                temp_elements.append(
                    triangle_elements[row-1][column-1] + triangle_elements
                    [row-1][column])
        triangle_elements.append(temp_elements)
    return triangle_elements
