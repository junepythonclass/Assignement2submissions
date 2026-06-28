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

#create a function that accept input.
#with atleast 2 examples for each explain in the simplest way possible all operators (its definition, examples and examples for each)

#example1 
#In this example, this function is a block of code shown by collon(:). I have the input of type int as the operand, = signs are the operator
def multiplication():
    num1= int(input("First value:")) 
    num2= int(input("Second Value:"))
    print(num1 * num2)
multiplication()

#Example 2
#In this example, the function is odd number, = is the assignment operator
def oddNumber():
    num1 = int(input("Numbers:"))
oddNumber()

