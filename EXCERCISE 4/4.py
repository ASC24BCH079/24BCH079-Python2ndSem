def remover(s1,s2):
    r = ""
    i = 0
    n1 = len(s1)
    n2 = len(s2)
    while i < n2:
        if i <= n2-n1 and s2[i:i+n1] == s1:
            i += n1
        else:
            r += s2[i]
            i += 1
    return r
s2 = input("Enter main string: ")
s1 = input("Enter string to remove: ")
print("The main string after removing the unwanted string is:", (remover(s1,s2)))