'''
#write a python program to calculate the innings of a batsman and count the boundaries ,
#Dotballs and the total score
# [4,6,1,0,2,4,0,6]
runs=list(map(int,input("enter no.of runs:").split(',')))
boundaries=dotballs=total_score=0
for i in runs:
    total_score+=i
    if i==4 or i==6:
        boundaries+=1
    elif i==0:
        dotballs+=1
print('boundaries:',boundaries)
print('dotballs:',dotballs)
print('total_score:',total_score)

#Write a program prone password attempts
password='4567'
max_attempts=5
current_attempt=0
while current_attempt<max_attempts:
    entered_password=input("enter password:")
    if entered_password==password:
        print("Unlocked")
        break
    else:
        print("entered password is wrong.Try again")
        current_attempt+=1
else:
    print("phone locked try after 30 seconds")
'''
password='1234'
max_attempts=3
current_attempt=0
while current_attempt<max_attempts:
    entered_password=input("enter password:")
    if entered_password==password:
        print("Unlocked")
        break
    else:
        print("entered password is wrong.Try again")
        current_attempt+=1
else:
    print("phone locked try after 30 seconds")
            


