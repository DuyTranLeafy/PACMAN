import copy
import heapq
import convert
import numpy as np


class AStar:
    converter = convert.MatrixConverter()
    grid = converter.convertCoordinates()
    cd_array = copy.deepcopy(grid)

    array = converter.convertOneZero()
    nparray = np.array(array)

    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
        self.neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def heuristic(self, a, b):
        return abs(b[0] - a[0]) + abs(b[1] - a[1])

    def astar(self):
        close_set = set()
        came_from = {self.start: None}  # Add the start point here
        g_score = {self.start: 0}
        f_score = {self.start: self.heuristic(self.start, self.goal)}
        o_heap = []

        heapq.heappush(o_heap, (f_score[self.start], self.start))

        while o_heap:
            current = heapq.heappop(o_heap)[1]

            if current == self.goal:
                data = []
                while current is not None:
                    data.append(current)
                    current = came_from[current]
                data.reverse()  # Reverse the path before returning
                return data

            close_set.add(current)
            for i, j in self.neighbors:
                neighbor = current[0] + i, current[1] + j
                tentative_g_score = g_score[current] + self.heuristic(current, neighbor)
                if 0 <= neighbor[0] < self.nparray.shape[0]:
                    if 0 <= neighbor[1] < self.nparray.shape[1]:
                        if self.nparray[neighbor[0]][neighbor[1]] == 1:
                            continue
                    else:
                        # array bound y walls
                        continue
                else:
                    # array bound x walls
                    continue

                if neighbor in close_set and tentative_g_score >= g_score.get(neighbor, 0):
                    continue

                if tentative_g_score < g_score.get(neighbor, 0) or neighbor not in [i[1] for i in o_heap]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic(neighbor, self.goal)
                    heapq.heappush(o_heap, (f_score[neighbor], neighbor))


        return False


# # Usage:
# start = (2, 2)
# goal = (30, 2)
#
# astar = AStar(start, goal)
# path = astar.cd_array
#
#
# print(path)
