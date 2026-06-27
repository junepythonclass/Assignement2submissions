#Assignment
#write a python program that asks a user to input their name, age, location, phone number,their track(python or javascript) and the cohort intake
#if someone is below 15, computer should say not eligible for the course, if track is not py or javas, computer should say not eligible for CSE
name = input("Enter your name: ")
age = int(input("Enter your age: "))
location = input("Enter your location: ")
phonenumber = input("Enter your phone number: ")
track = input("Enter your track (python or javascript): ")
cohort = input("Enter cohort intake: ")

if age < 15:
    print("Not eligible for course")
elif track.lower() not in ["python", "javascript"]:
    print("Not eligible for CSE")
else:
    print(f"\nSuccess! Welcome {name} to the {track.title()} track for {cohort}.")