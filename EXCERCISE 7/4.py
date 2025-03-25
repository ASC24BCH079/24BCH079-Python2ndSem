ns = {"Amit", "Anjali", "Bhavesh", "Binod", "Akash", "Bharat", "Anita", "Suraj", "Sarthak", "Sushant"}
a, b, s = set(), set(), set()

for x in ns:
    if x.startswith("A"):
        a.add(x)
    elif x.startswith("B"):
        b.add(x)
print("Names starting with A:", a)
print("Names starting with B:", b)
