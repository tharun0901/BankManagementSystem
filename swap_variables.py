num = int(input("Enter the number: "))
num_str=str(num)
num_digits=len(num_str)
sum=0
n=num
while n>0:
    digit=n%10
    sum+=digit**num_digits
    n=n//10
print(sum)