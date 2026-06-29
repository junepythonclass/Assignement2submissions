# Program to check course eligibility

# Get user information
name = input("Enter your name: ")
age = int(input("Enter your age: "))
location = input("Enter your location: ")
phone = input("Enter your phone number: ")
track = input("Enter your track (Python or JavaScript): ").lower()
cohort = input("Enter your cohort intake: ")

# Check eligibility
if age < 15:
    print("\nSorry,", name + ", you are not eligible for the course because you are below 15 years.")
elif track != "python" and track != "javascript":
    print("\nSorry,", name + ", you are not eligible for CSE because your track is not Python or JavaScript.")
else:
    print("\n===== STUDENT DETAILS =====")
    print("Name:", name)
    print("Age:", age)
    print("Location:", location)
    print("Phone Number:", phone)
    print("Track:", track.capitalize())
    print("Cohort Intake:", cohort)
    print("Congratulations,", name + "! You are eligible for the course.")