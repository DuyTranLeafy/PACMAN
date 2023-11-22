import random

import convert


class MatrixHandler:
    converter = convert.MatrixConverter()
    matrix = converter.convertOneZero()

    def random_zero_coordinate(self):
        zero_coordinates = [(i, j) for i, row in enumerate(self.matrix) for j, value in enumerate(row) if value == 0]

        if zero_coordinates:
            chosen_coordinate = random.choice(zero_coordinates)
            return chosen_coordinate
        else:
            return None


# matrix_handler = MatrixHandler()
#
# random_coordinate = matrix_handler.random_zero_coordinate()
#
# # In tọa độ được random
# print("Random coordinate:", random_coordinate)
