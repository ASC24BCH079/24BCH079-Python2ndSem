def count_vowels(s):
    v = "aAeEiIoOuU"
    c = 0
    for ch in s:
        if ch in v:
            c += 1
    return c
s = input("Enter a string:")
print("The number of vowels in the given string are:", (count_vowels(s)))