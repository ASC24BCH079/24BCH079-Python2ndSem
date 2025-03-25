import random

s = set()
while len(s) < 10:
    s.add(random.randint(15, 45))

c = sum(1 for x in s if x < 30)
s = {x for x in s if x <= 35}

print("Generated numbers:", s)
print("Count of numbers less than 30:", c)
print("Numbers after removing those greater than 35:", s)
