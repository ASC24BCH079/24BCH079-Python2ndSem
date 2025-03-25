names = [('Sarthak', 'Sushant'), 'Tejawswini', ('Keshav', 'Nishant'), 'Vrinda', 'Shraddha']
boys = 0
girls = 0
for n in names:
    if isinstance(n, tuple):
        boys += len(n)
    else:
        girls += 1
print("Number of boys:", boys)
print("Number of girls:", girls)
