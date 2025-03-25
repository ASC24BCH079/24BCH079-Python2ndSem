n = set()

n.add("Amit")
n.add("Neha")
n.add("Raj")
n.add("Priya")
n.add("Vikas")

if "Amit" in n:
    n.remove("Amit")
    n.add("Aman")

if len(n) > 2:
    n.pop()
    n.pop()

print("Final set of names:", n)
