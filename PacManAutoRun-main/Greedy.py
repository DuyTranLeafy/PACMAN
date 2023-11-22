import copy
import convert
import numpy as np
import AStar

class Greedy:
    converter = convert.MatrixConverter()
    grid = converter.convertCoordinates()
    cd_array = copy.deepcopy(grid)
    matrix = np.array(converter.convertOneZero())  # Convert to NumPy array

    def __init__(self):
        self.visited = set()
        self.path = []
        self.steps = 0

    def heuristic(self, current, _):
        return abs(current[0] - self.matrix.shape[0]//2) + abs(current[1] - self.matrix.shape[1]//2)

    def get_neighbors(self, position):
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        result = []
        for dx, dy in neighbors:
            new_x, new_y = position[0] + dx, position[1] + dy
            if 0 <= new_x < self.matrix.shape[0] and 0 <= new_y < self.matrix.shape[1]:
                result.append((new_x, new_y))
        return result

    def greedy(self, start):
        priority_queue = [(self.heuristic(start, None), start)]

        while priority_queue:
            _, vertex = min(priority_queue)
            priority_queue.remove((_, vertex))

            if self.matrix[vertex[0]][vertex[1]] == 0 and vertex not in self.visited:
                self.path.append(vertex)
                self.visited.add(vertex)
                self.steps += 1

                neighbors = self.get_neighbors(vertex)
                for neighbor in neighbors:
                    if self.matrix[neighbor[0]][neighbor[1]] == 0 and neighbor not in self.visited:
                        priority_queue.append((self.heuristic(neighbor, None), neighbor))

        return self.path,self.steps

    def optimal(self, location):
        greedy = Greedy()
        path, steps = greedy.greedy(location)
        i = 0
        long = len(path)
        while i < long - 1:
            if not (abs(path[i][0] - path[i + 1][0]) + abs(path[i][1] - path[i + 1][1]) == 1):
                solver = AStar.AStar(path[i], path[i + 1])
                path1 = solver.astar()

                path1.pop(0)
                path1.pop(-1)
                path = path[:i + 1] + path1 + path[i + 1:]
                i = i - 1
                long = len(path)
            i = i + 1
        return path, steps

# Sử dụng ví dụ:
# greedy = Greedy()
# path = greedy.optimal()
# print(path)
