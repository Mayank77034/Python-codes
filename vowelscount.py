n = str(input("enter a string :"))
n = n.lower()
vowels = 'aeiou'

count = 0
for char in n :
    if char in vowels :
        count+=1
print(f"the count of vowels in string is :{count}")