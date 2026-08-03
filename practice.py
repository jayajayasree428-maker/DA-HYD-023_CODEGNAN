'''
task:students marks and grade analyzes
90-100-->A
80-89-->B
70-79-->C
60-69-->D
<60-->Fail
#also -ve negative cases should not be allowed and marks should not be greater than 100
'''
'''
marks=int(input("enter marks"))
if marks >=90 and marks<=100:
    print("Grade A")
elif marks>=80 and marks<=89:
    print("grade B")
elif marks>=70 and marks<=79:
    print("grade C")
elif marks>=60 and marks<=69:
    print("grade D")
elif marks<60 and marks>=0:
    print("Fail")
else:
    print("you have entered -ve values or marks greater than 100,so enter the correct marks")

'''
'''
instagram=input("Enter username:")
age=int(input("enter your age"))

if age>18:
    print("welcome",instagram)
'''

'''
marks=int(input("enter marks"))
if marks >0 and marks<=100:
    if marks>=90:
        print("Grade A- Outstanding")
    if marks>=80 and marks<=89:
        print("grade B - Excellent")
    if marks>=70 and marks<=79:
        print("grade C - Good")
    if marks>=60 and marks<=69:
        print("grade D - Fair,needs improvement")
    if marks<60:
        print("Fail")
else:
    print("you have entered -ve values or marks greater than 100,so enter the correct marks")
'''



'''
numbers=int(input("enter numbers"))
if numbers%2==0:
    print("even number")
else:
    print("odd number")
'''


'''

#TASK-2
marks=int(input("enter marks"))
if 90<=marks<=100:
    print("Grade A")
elif 80<=marks<=89:
    print("Grade B")
elif 70<=marks<=79:
    print("Grade C")
elif 60<=marks<=69:
    print("Grade D")
elif 60>marks>=0:
    print("fail")
else:
    print("you have entered -ve values ,only enter +ve values")
'''


'''
#PRACTICE
amount=int(input("enter amount:"))
if amount>=500:
    print("Withdraw amount")
else:
    print("Transaction Unsuccessful")
'''
'''
#PRACTICE
number=int(input("enter value:")) 
if number>=0:
    print("Positive value")
elif number<0:
    print("Negative value")
else:
    print("dont enter strings")

'''


'''
marks= int(input("enter marks:"))
if marks>=90 and marks<=100:
    print("Grade A -Outstanding")
elif marks>=80 and marks<=89:
    print("Grade B -Excellent")
elif marks>=70 and marks<=79:
    print("Grade C -Good")
elif marks>=60 and marks<=69:
    print("Grade D -Fair needs improvement")
elif marks>=50 and marks<=59:
    print("Grade E -Poor,needs serious improvemnet")
elif marks<50 and marks>=0:
    print("Grade F -Failed,needs to reappear")
else:
    print("Invalid marks entered")
'''


'''
number=int(input("enter number:"))
if  number>0 and number%2==0:
    print("even number")
elif  number>0 and number%2!=0:
    print("odd number")
elif  number<0 and number%2==0:
    print("negative even number")
elif number<0 and number%2!=0:
    print("negative odd number")
else:
    print("zero is neither odd nor even")
'''


'''
season=int(input("enter month number"))
if season  in [12,1,2]:
    print("winter")
elif season  in [3,4,5]:
    print("spring")
elif season  in [6,7,8]:
    print("summer")
elif season  in [9,10,11]:
    print("autumn")
else:
    print("invalid month number")
'''

'''
season=int(input("enter month number"))
if season>0 and season>=12:
    if season==12 or season==1 or season ==2:
        print("winter")
    elif season==3 or season==4 or season==5:
        print("spring")
    elif season==6 or season==7 or season==8:
        print("summer")
else:
    print("autumn")

'''
