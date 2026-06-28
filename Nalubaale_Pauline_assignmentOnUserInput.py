#write a python that asks a user to input their name, age, location, phone number, their track(python or Javascript) and the cohort intake
#If someone is below 15, computer should say not eligible for the course, if track is not py or javas, computer should say not eligible for CSE
name = input("What is your name:")
age = int(input("How old are you?:"))
if age < 15:
    print("Not eligible for the course")
else:
    print("Continue")

location = input("Your current location:")
phone_number = input("Your phone number:")

tracks = ["py", "javascript"]
track = input("Track of Study:") #
if track not in tracks:
    print("Not eligible for CSE")
else:
    print("Eligible for CSE")

cohort_intake = input("Which cohort are you?")

