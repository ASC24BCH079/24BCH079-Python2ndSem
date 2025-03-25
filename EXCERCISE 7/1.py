f = ["rose", "lily", "jasmine", "tulip", "marigold"]
uf = set()

for x in f:
    uf.add(x.upper())

print("Original flowers:", f)
print("Uppercase flowers in set:", uf)
