tisl = [(1,'Sushant',15), (2,'Keshav',14), (3,'Sarthak',18), (4,'Toshika',9), (5,'John',18), (6,"Mary",17), (7,"Tom",19), (8,"Lisa",18)]
r, n, a = zip(*tisl)
print("Roll numbers:", list(r))
print("Names:", list(n))
print("Ages:", list(a))
