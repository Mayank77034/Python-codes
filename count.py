user = str(input("enter a string"))
lowercount = 0
uppercount = 0
digitcount = 0
for char in user :
    if char .islower():
        lowercount = lowercount + 1
    elif char .isupper():
        uppercount = uppercount + 1
    elif char .isdigit():
        digitcount = digitcount +1

print(f"in entered string there is {lowercount} lowercase")
print(f"in entered string there is {uppercount} uppercase")
print(f"in entered string there is {digitcount} digits")
