n = int(input("enter a number"))
i = 1
count = 0
while(i<=n):
    if n % i == 0:
        count +=1
    i+=1

if count == 2:
    print("this is a prime number")
else :
    print("this is not an  prime number")
