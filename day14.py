'''
Tokens,Datatypes --> Control Flow Statements -->if,ifelse,else,for,while,break
continue..

procedure Oriented programming

Functions --> A function is a block of code which performs a specific task
Its a reusable group of statements where we define using
def keyword
Advantages --> Code reusability,code maintainability,ease of deburgin,
avoiding code duplication,modularity

def fname(parameters): Function defn
    """Doc String""" Description
    statement(s).....       Function Body
    .........
    return value(s).....
fname(args) Function call    
'''
#To Perform sum of given objects
'''def add(a,b):
    """Sum of objects"""
    c = a+b
    return c
print(add(11,4)) #Addition
print(add('code','gnan')) #concatenation
print(add([11,5],[11,34]))#Merging
c,d = map(int,input("Enter the values:").split(','))
print(c,d)
print(add(c,d))

def add(a,b):
    """Sum of objects without return"""
    print(a+b)
add('code','gnan')
print(add(12,-34)) #it returns along with None

name,age,salary = "Jaya",22,10000
#usage of return

def details():
    #return name,age,salary
    #return "Codegnan"
    #return 23+44+66
    return #it returns None as output
print(details())

--> There are 5 types of arguments

--> POsitional Arguments
--> Default arguments
--> Keyword argumemts
--> Variable length arguments (*args)
--> Keyword variable length arguments (**kwargs)
'''
#Positional Arguments --> Number of arguments in function defn should
#match with function call (order has to be maintained)
#print(len(123,234) this is as per built-in len(obj) will accept one argument
'''
def details(name,place):
    """To store the details"""
    #name = "Codegnan"
    #place = "Hyderabad"
    #return name,place
    print(f'name is{name}')
    print(f'place is {place}')
#print(details("Jaya","Hyderabad"))
#print(details("Sai","vizag"))
#print(details("vizag","syam",34)) #raises a TypeError as only argumrnts to 
c,d = map(str,input("Enter the values:").split(','))
details(c,d)

#Default arguments --> we can make arguments as default but not first argument
#as default

#def grocery(item,price=35):
#def grocery(item="Cheese",price = 100): # we can also make all args as default
#def grocery(item ="Burger",price): #non default always follows default    
    """ usage of default arguments"""
    print(f'The item is {item} and price is {price}')

grocery("Milk",32)
#grocery(32,"Milk")
grocery("Bread") #by default we have given price as 35
grocery() #as both item and price as default arguments
'''

#keyword arguments --> whenever we want to specify the name of  argument
def employee(name,salary,role,place = "codegnan"):
    """keyword arguments usage"""
    print(f'Employee name is {name},role is {role} and salary is {salary}')
employee("sai",20000,"Admin")
employee(salary = 25000,role = "Frontdesk",name = "Jaya")
employee("Akash",25000,"IT","Cognizant")


