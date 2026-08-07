'''
#Write a program to calculate the prices of all products
#1200, 1500, 1600, 1800 
products = list (map(int,input().split(',')))
total = 0
for i in products:
    total = total + i
print(total)
                 
#Write a program Password analyze a password
#How many uppercase, lowercase,
#how many digits,
#special characters
#Sum of items in a cart 
password = "AbC@123xY"

upper = 0
lower = 0
digit = 0
special = 0

for i in password:
    if i >= 'A' and i <= 'Z':
        upper = upper + 1
    elif i >= 'a' and i <= 'z':
        lower = lower + 1
    elif i >= '0' and i <= '9':
        digit = digit + 1
    else:
        special = special + 1

print("Uppercase =", upper)
print("Lowercase =", lower)
print("Digits =", digit)
print("Special Characters =", special)

#Write a program gmail
email = input().slpit()
for mail in email:
    print(mail.split("@")[1])

'''

