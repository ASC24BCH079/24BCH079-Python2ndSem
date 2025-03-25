food = [("Butter",60), ("Sugar",80), ("Banana",70), ("Milk",112), ("Bread",50), ("Eggs",200), ("Syrup",150)]
srt = sorted(food, key=lambda x: x[1], reverse=True)
print("Food items sorted by price in descending order:")
for f in srt:
    print(f[0], "-", f[1])