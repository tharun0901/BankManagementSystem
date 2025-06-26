def sum_taget(arr,t):
    l=len(arr)
    for i in range(l):
        for j in range(i+1,l):
         if arr[i]+arr[j]==t:
            return f"{arr[i]},{arr[j]}"
arr=[2,3,5,8,5,1]
t=6
print(sum_taget(arr,t))