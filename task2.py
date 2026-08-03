
season=int(input("enter month number:"))
if season<0 or season>=12:
    if season==12 or season==1 or season ==2:
        print("Season:winter")
    elif season==3 or season==4 or season==5:
        print("Season:spring")
    elif season==6 or season==7 or season==8:
        print("Season:summer")
else:
    print("Season:autumn")

marks= int(input("enter marks:"))
if marks>=90 and marks<=100:
    print("Grade A ")
    print("Outstanding")
elif marks>=80 and marks<=89:
    print("Grade B")
    print("Excellent")
elif marks>=70 and marks<=79:
    print("Grade C")
    print("Good")
elif marks>=60 and marks<=69:
    print("Grade D")
    print("Fair needs improvement")
elif marks>=50 and marks<=59:
    print("Grade E ")
    print("Poor,needs serious improvemnet")
elif marks<50 and marks>=0:
    print("Grade F")
    print("Failed,needs to reappear")
else:
    print("Invalid marks entered")

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
















