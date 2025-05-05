age = 17

if age >= 18:
    print("You can vote")
elif age >= 16:
    print("You can drive")
else:
    print("You are too young for both")

print(age)

isBirthday = True
if(isBirthday):
    print("Happy Birthday")
    age = 18
    if(age >= 18):
        print("Yay! You can vote")
print("You are now " + (str)(age))

if (age <= 18 and age >= 16):       #True and True
    print("You are almost able to vote, but you can drive")

if (age > 18 or age == 18):     #False or True
    print("You can vote and you can drive")

grade = 68
#A - 90 or greater
#B - 80 or greater
#C - 70 or greater
#D - 60 or greater
#F- 59 or less
letterGrade = ""

if grade >= 90:
    letterGrade = "A"
elif grade >= 80:
    letterGrade = "B"
elif grade >= 70:
    letterGrade = "C"
elif grade >= 60:
    letterGrade = "D"
else:
    letterGrade = "F"

print("You received a " + letterGrade + " in this class")