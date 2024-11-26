n = int(input("enter a number:"))
i = 1
count = 0
while (n%i==0) :
    if i%n == 0:
        count = count + 1
    i +=1
if count == 2:
    print("it is a prime number")
else:
    print("it is not")

