#for <variable> in range(int):
    #Code Goes here

for i in range(5):
    print(i + 1)

print()
age = 20
for i in range(20):
    print(i)

fruits =["apple", "banana", "cherry", "oranges", "strawberry", "blackberry"]
for fruit in fruits:
    print(fruit)

count = 0
while count < 5:
    print("Counting: ", count)
    count += 1  # count = count + 1

password = "password"
isPassword = False
while (isPassword == False):
    userPass = input("What is the password: ")
    if (userPass == password):
        isPassword = True

for i in range(19):
    print(i + 2)

count = 2
while count < 21:
    print(count)
    count += 1

#
##
###
####
#####
height = input("How tall would you like your triangle ")
for i in range((int)(height)):
    print("#" * (i + 1))

count = 1
while count <= (int)(height):
    print("#" * (count))
    count += 1