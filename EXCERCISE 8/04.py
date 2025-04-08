LIST = ['madam', 'python', 'malayalam', 12321] 
palindrome=list(filter(lambda s: str(s)==str(s) [::-1],LIST)) 
print("palindrome:",palindrome)