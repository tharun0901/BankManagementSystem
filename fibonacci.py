def series(n):
   a=0
   b=1
   for i in range(n):
      print(a)
      a,b=b,a+b
a=int(input("Enter the number:"))
series(a)