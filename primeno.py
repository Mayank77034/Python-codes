n = int(input("ENTER A NUMBER:")) #7
i = 1
count = 0
while (i <= n):
    if n % i == 0:
        count = count + 1
    i+=1

if count == 2:
    print("it is a prime number")

else :
    print("it is a composite number")
    4