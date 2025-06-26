def tsum(l):
    res=[]
    length=len(l)
    for i in range(length-2):
        if i>0 and l[i]==l[i-1]:
            continue
        le=i+1
        r=length-1
        while le<r:
            total=l[i]+l[le]+l[r]
            if total<0:
                le=le+1
            elif total>0:
                r=r-1
            else:
                res.append([l[i],l[le],l[r]])