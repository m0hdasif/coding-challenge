from ctypes import addressof, c_int, c_wchar_p

# get id of a variable
a = 12
print(f"integer:{a}")
print(id(a), hex(id(a)))
print(addressof(c_int(a)))

# get id of a string
a = "asif"
print(f"string:{a}")
print(id(a), hex(id(a)))
# a[0], a[1] all have the different address and no relationship with a
print(addressof(c_wchar_p(a)))
# get id of list
a = [
    1,
    2,
    3,
    4,
]
print(f"list:{a}")
print(id(a), hex(id(a)))

# get id of tuple
a = (1, 2, 3, 4, 5)
print(f"tuple:{a}")
print(id(a), hex(id(a)))

# get id of a dictionary
a = {"a": 1, "b": 2}
print(f"dictionary:{a}")
print(id(a), hex(id(a)))
