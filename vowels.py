n = str(input("enter a string"))
n = n.lower()
vowels = 'aeiou'
count = 0
for char in n :
    if char in vowels :
        count += 1
print(f"the total count of vowel is :{count}")