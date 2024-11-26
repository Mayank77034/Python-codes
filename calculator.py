first = int(input("enter a first number"))
operator = input("enter a operator (+,-,*,/,%):")
second = int(input("enter a second number"))
if operator =="+":
    print(first+second)
elif operator =="-":
    print(first-second)
elif operator =="*":
    print(first*second)
elif operator =="/":
    print(first/second)
elif operator =="%":
    print(first%second)  
else :
    print("invalid operation")             