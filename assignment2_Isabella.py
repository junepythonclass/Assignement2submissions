name = input("What is your name?:")
age = int(input("How old are you?:"))
track = input("What track are you taking?:")
location = input("Where are you located?:")
number = int(input("What is your phone number?:"))
cohort = input("What cohort are you enrolled in?")

if age < 15:
    print("Not eligible for CSE")
else:
    print("Eligible for CSE")

if track == "Python":
    print("Eligible for CSE")
elif track == "JavaScript":
    print("Eligibe for CSE")
else:
    print("Not eligible")


#Assignment
#write a python program that asks a user to input their name, age, location, phone number,their track(python or javascript) and the cohort intake
#if someone is below 15, computer should say not eligible for the course, if track is not py or javas, computer should say not eligible for CSE
