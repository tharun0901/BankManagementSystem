def nrepeat(s):
    n=len(s)
    for i in range(n):
        unique=True
        for j in range(n):
            if s[i]==s[j] and i!=j:
                unique=False
                break
        if unique:
                return i
    return -1
print(nrepeat("leetcode"))