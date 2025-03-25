def tl(s):
    r = ""
    for ch in s:
        if 65 <= ord(ch)<= 90:
            r += chr(ord(ch) + 32)
        else:
            r += ch
    return r
def tu(s):
    r = ""
    for ch in s:
        if 97 <= ord(ch) <= 122:
            r += chr(ord(ch) - 32)
        else:
            r += ch
    return r

def t(s):
    r = ""
    for ch in s:
        if 65 <= ord(ch) <= 90: 
            r += chr(ord(ch) + 32)
        elif 97 <= ord(ch) <= 122: 
            r += chr(ord(ch) - 32)
        else:
            r += ch
    return r
s = input("Enter a string: ")
print("Lowercase:", tl(s))
print("Uppercase:", tu(s))
print("Toggle case:", t(s))