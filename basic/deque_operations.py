from collections import deque

d = deque([1, 2, 3, 5], 5)
d.append(
    6
)  # append on right side and remove the left most element if it crossed max length
d.appendleft(
    0
)  # append on left side and remove the right most element if it crossed max length
d.pop()
d.popleft()
d.rotate(1)  # move last n elements to the left side and then other elements
