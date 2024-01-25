#!/usr/bin/python3
"""module that rotate 2D matrix 90 degree clockwise"""


def reverse_list(lst):
    """this function reverse a list"""
    for rows in range(len(lst)):
        lst[rows] = lst[rows][::-1]


def rotate_2d_matrix(matrix):
    """swap elements indexes and reverse\
    inner lists using reverse_list function"""
    for i in range(len(matrix)):
        for j in range(i, len(matrix[0])):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    reverse_list(matrix)
