x = int(input("enter a marks of tenth :"))
xii = int(input("enter a marks of twelfth :"))
graduaton_marks = int(input("enter a graduation marks :"))
stream   = str("stream chaged or not (yes or no): ").lower() == 'yes'
if stream :
    adjusted = graduation_marks-5
else :
    adjusted =  graduation_marks
if x > 80 and xii >80 and adjusted >70 :
    print("you are eligible")
else :
    print("you are not able")

