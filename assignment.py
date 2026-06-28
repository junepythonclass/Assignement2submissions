print("=== student Registration  ===")

name = input("Enter your name: ")
age = input("Enter your age: ")
location = input("Enter your location: ")
phone_number = input("Enter your phone number: ")
track = input("Enter your track: ")
cohort_intake = input("Enter your cohort intake: ")

print("\n=== Registration Summary ===")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Location: {location}")
print(f"Phone Number: {phone_number}")
print(f"Track: {track}")
print(f"Cohort Intake: {cohort_intake}")
print("Registration complete!")




print("=== CSE Eligibility Check ===")

name = input("Enter your name: ")
age = int(input("Enter your age: "))  # int() converts text to number
track = input("Enter your track (python/javascript): ").lower()  # .lower() makes it case-insensitive


allowed_tracks = ["python", "javascript"]

if age < 18:
    print(f"Sorry {name}, you are not eligible for the course. Minimum age is 18.")
elif track not in allowed_tracks:
    print(f"Sorry {name}, you are not eligible for CSE. Track must be Python or Javascript.")
else:
    print(f"Congrats {name}! You are eligible for CSE in the {track} track.")
print("Check complete.")






print("=== CSE Eligibility Check ===")

name = input("Enter your name: ")
age = int(input("Enter your age: "))  # int() converts text to number
track = input("Enter your track (python/javascript): ").lower()  # .lower() makes it case-insensitive


allowed_tracks = ["python", "javascript"]

if age < 18:
    print(f"Sorry {name}, you are not eligible for the course. Minimum age is 18.")
elif track not in allowed_tracks:
    print(f"Sorry {name}, you are not eligible for CSE. Track must be Python or Javascript.")
else:
    print(f"Congrats {name}! You are eligible for CSE in the {track} track.")
print("Check complete.")


