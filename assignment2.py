Name = input("Full name: ")
print(Name)
Age = int(input("Current age: "))
if Age >= 15:
    print("Eligible")
    Location = input("Location: ")
    print(Location)
    Phonenumber = int(input("Phonenumber: "))
    if Phonenumber == 10:
        print("valid")
        Track = input("Track: ")
        Tracks = ["python","javascript"]
        if Track not in Tracks:
            print("not eligible for CSE")
        else:   
            Cohort = input("Cohort intake: ")
            if Cohort == "june intake":
                print("Available")
            else:
                print("Intake not available")
    else:
        print("Not valid")
else:
    print("Not eligible any programme")
    





