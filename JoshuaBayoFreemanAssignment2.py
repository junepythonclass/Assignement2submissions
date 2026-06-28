Name = input('Name:')
print(Name)
Age = int(input('Age:'))
if Age >= 15:
    print('eligible for CSE')
else:
    print('uneligible for CSE')
location = input('Address')
print(location)
Phonenumber = input('Tel:')
if len(Phonenumber) != 10:
    print('Invalid phone number Entered')
Track = input('track:')
Tracks = ['Python', 'JavaScript']
if Track not in Tracks:
    print('Not Eligible')
else:
    print('Eligible!')
Cohort = input('cohort')
if Cohort == 'June Intake':
    print('success')
else:
    print('unsuccessful')
    

