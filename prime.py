n = int(input("enter a number :"))
i = 1
count = 0
while( i<=n ):
    if i%n == 0:
        count = count + 1
    i= i+1

if count == 2:
    print("it is a prime number ")
else:
    print("this is not an prime number")