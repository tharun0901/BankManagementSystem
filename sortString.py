str=input("Enter the string:")
n=len(str)
print(n)
w=[word.upper() for word in str.split()]
sorted(w)
for word in w:
    print(word)
