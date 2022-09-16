# https://www.codingninjas.com/codestudio/problems/painter's-partition-problem_1089557

# return the minimum area in time unit
def distribute_wall(boards: list[int], total_painters: int) -> int:
    start = boards[0]
    end = sum(boards)
    min_time = -1
    while start <= end:
        mid = start + (end - start) // 2
        if is_possible_to_allocate(boards, total_painters, mid):
            min_time = mid
            end = mid - 1
        else:
            start = mid + 1
    return min_time


def is_possible_to_allocate(boards, total_painters, mid):
    painted_boards = 0
    no_of_allocated_painters = 1
    for board in boards:
        if painted_boards + board <= mid:
            painted_boards += board
        else:
            no_of_allocated_painters += 1
            if no_of_allocated_painters > total_painters or board > mid:
                return False
            painted_boards = board
    return True


if __name__ == "__main__":
    print(f"{distribute_wall([2, 1, 5, 6, 2,3 ], 3)=}")
