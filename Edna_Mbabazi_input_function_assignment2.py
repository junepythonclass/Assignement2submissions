#The name input funtion 
name = input("what is your name?:")
print (name)

#age input function with the condition of eligibility being 15 and above
age = input("what is your age?:")
age = int(age)
if age >= 15:
  print("eligible")
else:
  print("no eligibility")  

#location input function
location = input("where do you stay?:")
print(location)

#Phone number function and must be a number 
phone = input("what is your mobile number?:")
phone = int(phone)
print(phone)

#education input function with a condition of belonging to a cohort 
education = input("what is your education track?:")
if education == "javascript":
  print ("one of us")
elif education == "python":
  print("also one of us")
else:
  print("not one of us")
