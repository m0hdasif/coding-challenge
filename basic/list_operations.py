from bisect import bisect_left

a = [1, 1, 3, {"b": {"c": 1}}, 5]
a.insert(2, "string")  # insert at given index
a.remove(
    1
)  # remove element with value and raise exception if doest not exists.add()
a.pop(2)  # remove with index
# https://www.geeksforgeeks.org/python-cloning-copying-list/
a_copy = a[:]  # shallow copy
a_copy[2]["b"] = {"hello": 1}  # changed both clones
# https://stackoverflow.com/questions/19744829/python-priority-queue-implementation


elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
bisect_left(elements, 4)  # return element index if it exists
bisect_left(elements, 0)  # return 0 if minimum and not exists
bisect_left(elements, 12)  # return len if it max and not exists
