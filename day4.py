'''
Identity Operators -->checks the identity of an object --> id()
#id, is not

a = 5
b = a
print(id(a))
print(id(b))
c = 5
print(id(c))
print(a is c)
print(5 == 5)

a =[1,3,5,6]
b = a
print(id(a))
print(id(b))
c = [1,3,5,6]
print(id(c))
#As we have Lists (Mutable Collection), both c and a lists will have different
#ids whereas values are same
print(c is a) #Output False
print(c == a) #Output True
print(a is not c)

#Bitwise operators --> we perform bitwise operations over operands
#& (and) , | (or),^(XOR),shifting operators (<<,>>)
#Number will be converted to binary format

print(5&3) #both 5 and 3 to be converted binary and bitwise and is performed

print(5|3) #bitwise OR
print(5^3) #BItwise XOR

print(5 and 3) #here and is logical operator checks for both existances
#returns % in above case

print(5 or 3) #returns 3 in this case

#Leftshift Operator << ,Right Shift OPerator >>

print(5 < 1) #False Comparision
print(5 << 1) #Left shift operation by 1 position
print(5 >> ) #Right shift operation

print(15 << 2) #convert 15 to binary and perform 2 items left shifting

print(15 >> 2) #same 2 times right shifting


#Input Formatting --> input(),int(input()),float(input())
#You know -->single input
#2 or 3 inputs --> map()
#group of integers --> list(map(int,input().split(','))

names = input("Enter the names:").split(',')
print(names)

name1,name2 = map(str,input("Enter the Friends Names:").split(','))
print(name1,name2)
'''
#Tokens -->Numeric Datatypes --> Operators -->Flow of the program
#Control Block Statements -->they control the flow of the program
#when to execute,how to execute
#Conditional Statements --> if,else,elif (re;y pon condition to be executed)
#Repitition statements (Loops) --> for,while

#Conditional statements -->if usage
'''
Syntax  :
if <condition>:
    statement(s)...
    ......

#age = 15
age = int(input("Enter the age:"))
if age >=18:
    print('Your age is:',age)


age = int(input("Enter the age:"))
if age>=18 and age in [19,21,22]:
    print('Your Age is',age)
print(age)
#else keywprd if with else --> if-else

else:
    statement(s)..

if-else usage as below:

if <condition>:
    statement(s)...
    ....
else:
    statement(s)......
    ....
'''

#Vote Eligibility -->To check his/her voter eligibility and give access...

age = int(input("Enter the age:"))
if age>=18:
    print("You have Voter eligibility and age is",age)
    print("Access Granted")
else:
    age = 18-age
    print("You dont have eligibility as your age is",age)







































    
