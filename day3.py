#Numeric datatype --> int,float,complex along with boolean

#input formatting -->Accepting input from the user --> input()

#Accepting integer input from user
#by default input() accepts any input --> str
#int(input()) --> will accept only integers
'''age = int(input( 'Enter the age:'))
print(age)
print(type(age))

#float(input()) -->accepts integers,float values
age = float(input('Enter the age:'))
print(age)
print(type(age))

#Accepting string input from corner

name = input("Enter the name:")
print(name)
print(type(name))

#Accept group of values

marks = input("Enter the marks")
print(marks)

a = input().split() #by default split() has space
print(a)

#space separated values
a = input().split() #now you enter spaces in output
print(a)
#comma separated values
a = input("Enter the values:").split(',')
print(a)

#List of integers
marks = list(map(int,input("Enter the values").split(',')))
print(marks)

#Now we want to accept 2 values from user
age,salary = map(int,input("Enter the values").split(','))
print(age)
print(salary)

#Single input -->(input))
#two inputs -->a,b = map(int,input().split(','))
#any number result as list --> a = list(map(int,input(),split(',')))
marks = list(map(float,input("Enter the values").split(',')))
print(marks)

#group of float values
age,salary = map(float,input("Enter the values").split(','))
print(age)


#Accepting input from user --> int,float --> input formatting

#Operators --> Operators perform operations between values (operands)
#7 types -->Arithematic,Assignment,Comparison (Relationship)
#Membership,Identity,Logical,Bitwise

#Arithemartic Operators -->Arithematic operations
#+ , = ,*,/
print(5+3)
print(5-3)
print(5*3)
print(5/3) #Float value
#Floor Division (Integer division) -->returns quotient
print(5//3)
#Modulus -->divisible rules -->returns remainder
print(5%3)
#power (exponential)
print(5**3)

#Task -->Accept integer input as length,breadth --> find the area of rectancle
#Area = length * breadth

length,breadth = map(int,input("Enter the values:").split(','))
area = length * breadth
print(area)

#Assignment operators -->Assign the values
# = , +- , -=
a = 45
print(a)
#Update the value of a
a = a + 5 #a+= 5
print(a)
b = 35
b += a #b = b + a
print(b)
b -= 5 #b = b-5
print(b)

#Task : *=,/=,//=,%=,**= workout

#Comparison Operators -->we compare the values -->boolean
# -- (equal to) , != (not equal to) , < (less than) , >(greater than)
# -- (less than or equal to) --(greaterv than or equal to)

age = 25
print(age == 25) #returns Bpplean output
print(age != 35)
print(age < 25)
print(age <= 25)
print(age > 35)
print(age >= 35)

print(-5 < -1)

#Membership operators --> in,not in
#it checks for the existance of an object in a collection

marks = [56,75,45,85]
print(35 in marks)
print(35 in 355) #TypeError

print(25 not in marks)
print('code' in 'codegnan')
print('$' in "abc$frg')


#Logical Operators --> logical decision making -->and,or,not
#and -->and conditions to be satisfied
#of --> any one condition to be satisfied

a = (25 in [25,45,65]) and 45 < 56
print(a)
b = 45 > 56 or 25 <= 45
print(b)
c = not(True)
print(c)

#Identity operators --> check for identity of an object --> id()

a = 35
b = 35
print(id(a))
print(id(b))
print(a is b)
c = a
print(id(c))
print(c is a)'''

a = [1,3,4,5]
print(id(a))
c = a
print(id(c))
print(c is a)































