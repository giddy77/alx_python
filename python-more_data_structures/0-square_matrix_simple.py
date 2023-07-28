def square_matrix_simple(matrix=[]):
    # Use map to apply the square function to each element in each row
    squared_matrix = [list(map(lambda x: x ** 2, row)) for row in matrix]

    return squared_matrix
