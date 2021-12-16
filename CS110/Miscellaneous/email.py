fname = input('Enter your first name: ')
lname = input('Enter your last name: ')
gradDate = input('Enter the year you will graduate: ')

postFix = '@gssm.k12.sc.us'

emailAddress = fname[0].lower() + lname[:7].lower() + gradDate[2:] + postFix

print(emailAddress)

i = emailAddress.index('@')

print('20' + emailAddress[i-2:i])