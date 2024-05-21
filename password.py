# This function generates a password

import random

print('Your password: ')

# create a list of all possible characters
chars = 'abcdefghijklmnopqrstuvwxyz1234567890!@£$%^&*()?/\~{[]}'

password = ''
for x in range(16):
    password += random.choice(chars)
    
print(password)
