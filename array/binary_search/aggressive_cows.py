def find_max_distance(positions: list[int], total_cattle: int) -> int:
    start = 0
    end = max(positions)
    max_distance = -1
    positions.sort()
    while start < end:
        mid = start + (end - start) // 2
        if is_possible(positions, total_cattle, mid):
            max_distance = mid
            start = mid + 1
        else:
            end = mid - 1
    return max_distance


def is_possible(positions: list[int], total_cattle: int, mid: int) -> bool:
    allotted_positions = 1
    distance = -1
    for pos in positions:
        if (pos - distance) >= mid:
            allotted_positions += 1
            if allotted_positions >= total_cattle:
                return True
            distance = pos
    return False


if __name__ == "__main__":
    print(f"{find_max_distance([4,2,1,3,6],2)=}")
