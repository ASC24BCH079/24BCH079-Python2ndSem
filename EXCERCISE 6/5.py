a = [(1, 2), (), (3, 4), 5, 6, (), 7, (), (8, 9), (10, 11), (), (), 12]
req = [t for t in a if t != ()]
print("List after removing empty tuples:", req)