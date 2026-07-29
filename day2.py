'''
Tokens --> Variables,punctuators

Variables --> Named memory location,its a placholdernfor data
#Rules are to be followed

#MultiAssignment of variables

name,age,place = 'Codegnan',7,'Hyderabad'
print(name,age,place)
print(name,age,place,sep=',')
print(name,age,place,sep='------>')

#a,b = 2,4,5 #ValueError as too many values to unpack
#Reassigning variables

name = "Codegnan"
a,b = 45,1.5
print(a,b)
ab = b,a
print(a,b,sep=',')

a,b = b,c #NameError as c is not defined
print(a,b)

#Deleting the variables -->del
del a
print(a)
del a,b
print(a,b)

#Punctuators --> [](Lists),()(tuples),{}{Dict,Sets}
name = "Codegnan";age = 7;course = 'Data_Analysis'
print(name,age,course)

#Datatypes --> Numeric (int,float,complex),boolean,None,
           #-->Sequences -->Lists,Tuples,Sets,Strings,Frozensets,mappings(dict)

#Numeric type -->int,float,complex

#int datatype --> auantity,age,
age = 22
print(age)
print(type(age)) #type --> returns the datatypes of object

print(type(234))

#quantity = 03 #it is not allowed
#print(quantity)

#float datatype --> temp,salary,price
price = 750.24;discount = 2.5
print(price,discount)
print(type(price))

#Complex -->combination of real and imag
i2 = 4
data = 5 + i2
print(data)

data = 5+2j #j is imag representation
print(data)
print(type(data))

#Boolean --> True / false

valid = True
print(type(valid))

error = False
print(type(error))


#TypeCasting -->Converting one type to another
#python by default follows implict type (we need not mention the datatype)

#We will go for Explicit Conversation

#Every built-in datatype is a built-in function
#int,float,complex,bool

#TypeCasting --> int -->float,complex,bool

age = 34
print(type(age))
b = float(age)
print(b)
c = complex(age)
print(c)
d = bool (age) #returns True for existing data
print(d)
e = bool(0)
print(e)

price = 34.25
print(type(price))
b = int(price))
print(b)
c = complex(price))
print(c)
d = bool(price) #returns true for existing data,
print(d)


#Complex for TypeCasting -->int,float,bool

ab = 2 + 5j
print(type(data))
b = int(data) #TypeError
print(data)
c = float(data)
print(c)
d = bool(data)
print(d)
print(type(d))

d = 5+4.5
print(d)
'''

e = int(float(bool(45)))
print(e)

f = 45+2.5+2+3j+False
print(f)

a=2.4+3j+True
print(a)
