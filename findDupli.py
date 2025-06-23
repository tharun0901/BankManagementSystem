def dupli(s):
    
    for i in set(s):
        c=0
        for j in s:
            if (i==j):
                c+=1
        print(f"{i},{c}")
dupli("banana")
