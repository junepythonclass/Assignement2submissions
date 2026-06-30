def register_student():
    # Collecting user input
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    location = input("Enter your location: ")
    phone = input("Enter your phone number: ")
    track = input("Enter your track (python/javascript): ").lower()
    cohort = input("Enter your cohort intake: ")

    # Validation logic
    if age < 15:
        print("Not eligible for the course: You must be at least 15 years old.")
    elif track != "python" and track != "javascript":
        print("Not eligible for CSE: Track must be either 'python' or 'javascript'.")
    else:
        print("\n--- Registration Successful ---")
        print(f"Name: {name}")
        print(f"Age: {age}")
        print(f"Location: {location}")
        print(f"Phone: {phone}")
        print(f"Track: {track.capitalize()}")
        print(f"Cohort: {cohort}")
        If you are running the program, here is a clean block of sample inputs you can copy and paste one by one to see h

### Scenario: Successful Registration
Copy these values into the console when prompted by the program:

| Prompt | Sample Input |
| :--- | :--- |
| **Enter your name:** | Sarah Jenkins |
| **Enter your age:** | 22 |
| **Enter your location:** | Nairobi |
| **Enter your phone number:** | +254700000000 |
| **Enter your track (python/javascript):** | javascript |
| **Enter your cohort intake:** | 2024-B |

***

### Scenario: Age Restriction Trigger
| Prompt | Sample Input |
| :--- | :--- |
| **Enter your name:** | Sam Junior |
| **Enter your age:** | 14 |
| **Enter your location:** | Lagos |
| **Enter your phone number:** | 08012345678 |
| **Enter your track (python/javascript):** | python |
| **Enter your cohort intake:** | 2024-A |

***

### Scenario: Invalid Track Trigger
| Prompt | Sample Input |
| :--- | :--- |
| **Enter your name:** | Mark Doe |
| **Enter your age:** | 25 |
| **Enter your location:** | Cape Town |
| **Enter your phone number:** | 0210000000 |
| **Enter your track (python/javascript):** | java |
| **Enter your cohort intake:** | 202