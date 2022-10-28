"""
Basics toy example
"""


def normalize(matrix):
    """
    This code is bad. But I want to make sure no one uses kain name.
    """
    minimum = 100000
    maximum = -100000
    for row in matrix:
        for element in row:
            if element > maximum:
                maximum = element
            if element < minimum:
                minimum = element

    new_matrix = []
    rang = maximum - minimum
    for row in matrix:
        new_row = []
        for element in row:
            new_element = (element - minimum) / rang
            new_row.append(new_element)
        new_matrix.append(new_row)

    return new_matrix
