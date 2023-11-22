import copy
import convert
import AStar


class DFS:
    converter = convert.MatrixConverter()
    grid = converter.convertCoordinates()
    cd_array = copy.deepcopy(grid)
    matrix = converter.convertOneZero()

    def __init__(self):
        self.visited = set()
        self.path = []

    def get_neighbors(self, position):
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        result = []
        for dx, dy in neighbors:
            new_x, new_y = position[0] + dx, position[1] + dy
            if 0 <= new_x < len(self.matrix) and 0 <= new_y < len(self.matrix[0]):
                result.append((new_x, new_y))
        return result

    def dfs(self, start):
        stack = [start]
        while stack:
            vertex = stack.pop()
            if vertex not in self.visited and self.matrix[vertex[0]][vertex[1]] == 0:
                self.path.append(vertex)
                self.visited.add(vertex)
                stack.extend(neighbor for neighbor in self.get_neighbors(vertex) if neighbor not in self.visited)
        return self.path

    def optimal(self, location):
        dfs = DFS()
        path = dfs.dfs(location)
        i = 0
        long = len(path)
        while i < long - 1:
            if not (abs(path[i][0] - path[i + 1][0]) + abs(path[i][1] - path[i + 1][1]) == 1):
                solver = AStar.AStar(path[i], path[i + 1])
                path1 = solver.astar()
                path1.pop(0)  # xóa phần tử đầu tiên
                path1.pop(-1)  # xóa phần tử cuối cùng
                path = path[:i + 1] + path1 + path[i + 1:]
                i = 0
                long = len(path)
            i = i + 1
        return path


# # Usage:
# dfs = DFS()
# path = dfs.dfs((2,2))
# print(path)

