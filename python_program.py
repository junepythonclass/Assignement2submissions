name = input ("What is your name? ")
print ("hello, ", name)
print ("Fill in the following details to check your eligibility for the course.")
age = int(input("What is your age? "))
if age < 15:
    print ("Sorry, you are not eligible for the course.")
else:
    location = input("What is your location? ")
    phone_number = input("What is your phone number? ")
    track = input("Which track are you interested in (Python or JavaScript)? ").lower()
    cohort_intake = input("What is your cohort intake? ")

    if track not in ['python', 'javascript']:
        print ("Sorry, you are not eligible for CSE.")
    else:
        print ("Thank you for providing your details. You are eligible for the course.")