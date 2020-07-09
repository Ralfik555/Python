matrix = [[1, 2], [3,4], [5,6], [7,8]]
transpose1 = [[row[i] for row in matrix] for i in range(2)]
transpose2 = [row[i] for row in matrix for i in range(2)]
print(matrix)
print(transpose1)
print(transpose2)
