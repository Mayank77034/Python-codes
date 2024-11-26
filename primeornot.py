n = int(input("enter a prime number"))
count = 0
i = 1
while i<=n:
    if n%i == 0:
        count = count + 1
    i = i+1
if count == 2:
    print("it is a prime number")
else:
    print("it is not a prime number")    

