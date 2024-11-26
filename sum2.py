# num1 = int(input("enter a number 1:"))
# num2 = int(input("enter a number 2:"))
# sum = num1 + num2
# print(sum)

# name = str(input("enter a name "))
# greetings = ["hello",{name},"nice to meet you"]
# print(greetings)

# #area of rectamge
# length = float(input("enter a length"))
# width = float(input("enter a width"))
# area = length * width
# print(area)

# #prime or not
# n = int(input("enter a number"))
# count = 0
# i = 1
# while (i<=n):
#     if(n%i == 0):
#         count = count +1
#     i = i+1
# if(count == 2):
#     print("the number is prime")

# else:
#     print("not") 


#vowels
sentence = str(input("enter a sewntence :"))
string = sentence.lower()
list1 = ['a','e','i','o','u']
count = 0
for i in string:
    if i in list1:
        count = count +1
print("it is a counting of vowels in this stering ",count)                