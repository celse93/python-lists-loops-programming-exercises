# Your code here
def matrix_builder(int):
    matrix = []
    small_matrix = []

    for y in range(0, int):
        small_matrix.append(1)

    for x in range(0, int):
        matrix.append(small_matrix)
    
    return matrix

print(matrix_builder(3))