name = input("What is your name?")
age = int(input("How old are you?"))
location = input("Place of residence:")
# in python's head, everything is viewed as text. so, to convert you specify that it in an integer aka int, check line 6 for reference
telephone_number = input("Phone number:")
track = input("Indicate your respective track:").lower ()
if age < 15:
    print ("Not eligible")

if track == "python" or track == "javacsript":
    print("Eligible for CSE")
# careful when you are using "and" plus "or"
elif track not in ["python", "javascript"]:
    print("Not eligible for CSE")
print()

