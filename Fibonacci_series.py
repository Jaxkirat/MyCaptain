n= int(input("Enter Number of terms"))

a = 0
b=  1
c = 0

if n <= 0:
   print("Please enter a positive number")
elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(a)
else:
   print("Fibonacci sequence:")
   while c < n:
       print(a)
       nth = a + b
       a = b
       b = nth
       c = c+1
