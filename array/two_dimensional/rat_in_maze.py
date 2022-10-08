# start from top-left(0,0) to bottom-right(n-1,m-1)
def find_all_paths(maze: list[list[int]]) -> list[str]:
    if not maze[0][0]:
        return []
    paths = []
    visited = [[0 for _ in row] for row in maze]
    current_location = (0, 0)
    solve(maze, visited, paths, current_location, "")
    return paths


def solve(
    maze: list[list[int]],
    visited: list[list[int]],
    paths: list[str],
    current_location: tuple[int, int],
    path,
):
    x, y = current_location
    if y == (len(maze) - 1) and x == (len(maze[y]) - 1):
        paths.append(path)
        return

    visited[y][x] = 1
    new_location_map = {
        "D": (x, y + 1),
        "L": (x - 1, y),
        "R": (x + 1, y),
        "U": (x, y - 1),
    }
    for turn, new_location in new_location_map.items():
        if is_safe(maze, visited, new_location):
            path += turn
            solve(maze, visited, paths, new_location, path)
            path = path[:-1]  # remove path to get other paths

    visited[y][x] = 0  # reset visited for other paths


def is_safe(
    maze: list[list[int]], visited: list[list[int]], location: tuple[int, int]
):
    x, y = location
    return (
        # within maze
        0 <= y < len(maze)
        and 0 <= x < len(maze[y])
        and maze[y][x]  # if path allowed
        and not visited[y][x]  # path not visited
    )


if __name__ == "__main__":
    maze = [[1, 0, 0, 0], [1, 1, 0, 0], [1, 1, 1, 0], [0, 1, 1, 1]]
    print(find_all_paths(maze))
