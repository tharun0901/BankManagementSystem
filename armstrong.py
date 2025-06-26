def arm(n):
    num=int(n)
    noofdigit=len(n)
    s=0
    t=num
    while t>0:
        d=t%10
        s=s+d**noofdigit
        t=t//10
    print(s)
    if num==s:
        print("it is armstrong number")
    else:
        print("it is not armstrong number")
n=input("Enter the number:")
arm(n)