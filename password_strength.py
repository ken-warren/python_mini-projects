# Let minimum requirements for the password be;
# length >= 10 characters
# Minimum of 1 lowercase, uppercase, special character and number
# no other characters allowed 

w, x, y, z = 0, 0, 0, 0

password = input('Enter Password: ')
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz'
special_char = '!@£$%^&*()_+'
num = '0123456789'

if (len(password) >= 10):
    for i in password:
        if (i in uppercase):
            w+=1
        if (i in lowercase):
            x+=1
        if (i in special_char):
            y+=1
        if (i in num):
            z+=1
        
if (w >= 1 and x >= 1 and y >= 1 and z >= 1
                    and w + x + y + z == len(password)):
    print('Password Valid')
else:
    print('Password Invalid. Please Try Again')