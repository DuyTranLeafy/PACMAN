import random
import convert

converter = convert.MatrixConverter()
matrix = converter.convertOneZero()


def random_zero_coordinate(matrix):
    zero_coordinates = [(i, j) for i, row in enumerate(matrix) for j, value in enumerate(row) if value == 0]

    if zero_coordinates:
        chosen_coordinate = random.choice(zero_coordinates)
        return chosen_coordinate
    else:
        return None


# Áp dụng thuật toán random
random_coordinate = random_zero_coordinate(matrix)

# In tọa độ được random
print("Random coordinate:", random_coordinate)
