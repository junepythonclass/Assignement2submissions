# Ask user for details

name = input("Enter your name: ")
age = int(input("Enter your age: "))
location = input("Enter your location: ")
phone = input("Enter your phone number: ")
track = input("Enter your track (Python or JavaScript): ")
cohort = input("Enter your cohort intake: ")

# Check eligibility

if age < 15:
    print("Not eligible for the course")

elif track.lower() not in ["python", "javascript"]:
    print("Wrong course please try again ")

else:
    print("\n===== STUDENT DETAILS =====")
    print("Name:", name)
    print("Age:", age)
    print("Location:", location)
    print("Phone Number:", phone)
    print("Track:", track)
    print("Cohort Intake:", cohort)
    print("Eligible for the course")