n = str(input("enter a string "))
countupper = 0
countlower = 0
while (int i<n) :
    if n.lower():
        countlower+=1
    elif n.upper():
        countupper+=1
    else:
        print("it is invalid")
print("entered string upper contains of {countupper}")
print(f"entered string lower contains of {countlower}")