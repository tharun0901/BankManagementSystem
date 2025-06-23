def secondLargest(li):
    for i in range(len(li)):
        for j in range(len(li)):
            if(li[i]<li[j]):
                li[i],li[j]=li[j],li[i]
    return li[len(li)-2]
arr=[7,4,3,2,8]
print(secondLargest(arr))