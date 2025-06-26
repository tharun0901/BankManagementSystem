def remove(inp,i):
    if i<0 or i>=len(inp):
        print("Invalid input")
        return inp
    result=inp[:i]+inp[i+1:]
    return result
