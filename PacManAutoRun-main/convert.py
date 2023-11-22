import copy
import matrix


class MatrixConverter:
    def __init__(self):
        self.WIDTH = 900
        self.HEIGHT = 950
        self.level = copy.deepcopy(matrix.matrix)
        self.matrix_convert = [[0]*len(self.level[0]) for _ in range(len(self.level))]

    def convertCoordinates(self):
        num1 = (self.HEIGHT - 50) // 32
        num2 = (self.WIDTH // 30)
        for i in range(len(self.level)):
            for j in range(len(self.level[i])):
                if self.level[i][j] == 1:
                    self.matrix_convert[i][j] = [j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)]
                elif self.level[i][j] == 2:
                    self.matrix_convert[i][j] = [j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)]
                else:
                    self.matrix_convert[i][j] = 0
        return self.matrix_convert

    def convertOneZero(self):
        for i in range(len(self.level)):
            for j in range(len(self.level[i])):
                if self.level[i][j] == 1:
                    self.matrix_convert[i][j] = 0
                elif self.level[i][j] == 2:
                    self.matrix_convert[i][j] = 0
                else:
                    self.matrix_convert[i][j] = 1
        return self.matrix_convert


# new = MatrixConverter()
# matrix1 = new.convertCoordinates()
#
# print(matrix1[3][2][1])
