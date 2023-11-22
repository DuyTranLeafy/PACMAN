from collections import deque
import convert

def bfs(matrix, start_row, start_col, visited, visited_coordinates):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start_row, start_col)])
    visited[start_row][start_col] = True
    found_coordinates = []

    while queue:
        current_row, current_col = queue.popleft()

        if matrix[current_row][current_col] == 0:
            found_coordinates.append((current_row, current_col))
            visited[current_row][current_col] = True

        for direction in directions:
            new_row, new_col = current_row + direction[0], current_col + direction[1]

            if 0 <= new_row < rows and 0 <= new_col < cols and not visited[new_row][new_col]:
                queue.append((new_row, new_col))
                visited[new_row][new_col] = True

    for coord in found_coordinates:
        visited_coordinates.add(coord)

    return found_coordinates

def search_matrix(matrix, start_row, start_col, visited_coordinates):
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    found = False

    while True:
        found_coordinates = bfs(matrix, start_row, start_col, visited, visited_coordinates)

        if not found_coordinates:
            break

        for coord in found_coordinates:
            print(coord)

        remaining_coordinates = set(found_coordinates) - visited_coordinates

        if remaining_coordinates:
            start_row, start_col = remaining_coordinates.pop()
            found = True
        else:
            break

    return found

converter = convert.MatrixConverter()
matrix = converter.convertOneZero()

visited_coordinates = set()
start_row, start_col = 2, 2

while search_matrix(matrix, start_row, start_col, visited_coordinates):
    pass
