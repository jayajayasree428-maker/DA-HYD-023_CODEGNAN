'''
Strings --> CaseConservations,Searching & Finding,String testing methods,
Replace,space removal

#Searching,Finding,Replacing,Joining...
a ="Codegnan"
print(len(a))
print(min(a))
print(max(a))

b = a.index('g') #it returns the index position
print(b)
c = a.index('n') #it returns the only the first accurance
print(c)
d = a.index('n',6) #it retuns the next accurance
print(d)
#e = a.index('n',8) #ValueError
#print(e) 
#f = a.index('t') #ValueError
#print(f)
g = a.index('n',1,4)
print(g)

#rindex() --> returns last occurance
b = a.rindex('g')
print(b)         
c = a.rindex('n') #here 'n' is occuring at 7th index
print(c)
#d = a.rindex('n',8) #it returns ValueError
#print(d)

#count() --> returns the number of items object is repeating

print('Codegnan'.count('n'))
print('code'.count('w')) #it returns 0 as we dont have 'w' in 'Code'
print('Jayasree'.count('a'))

#find() --> first occurance but it avoid error returns -1 if substring is
#not found
print('Codegnan'.find('f')) #it returns -1

print('Codegnan'.find('n'))

print('Codegnan'.rfind('n'))

a = "DataS"
print(len(a))
for i in a:
    #print(i)
    print(a.count(i),a.index(i))

  
# Replacing,splitting,Joining

# Strings are Immutable
a = 'Codegnan'
#a[4] = 's'
print(a.replace('g','s'))
print(a)
a = (a.replace('g','s'))
print(a)
print('jayaree#jayasree#jayasree'.replace('#',''))
print(a.replace('x','jayasree'))

a = 'code jayasree python'
print(len(a))
b = a.split() #by default if we have space it splits
print(b)
print(len(b))
c = 'code,jayasree,python'
d = c.split()
print(d)
e = c.split(',')
print(e)

#join()

a ='code'
b ='gnan'
print(a.join(b))
print(b.join(a))
print('#'.join('jaya'))
print(' '.join('jaya'))

# String testing methods (boolean)
# isalpha(),isalnum(),isdigit(),isupper(),islower().....

a = 'Codegnan123'
print(a.isalpha()) #it returns True for alphanumeric strings alse false
b = 'Codegnan'
print(b.isalnum()) 
print(a.isalpha()) #returns True only for alphabets
print(a.isdigit()) #returns True onlt for digit string
print('1234567890'.isdigit())
print('9876'.isnumeric) #this has upper edge (numbers,fractions,romans)
# Startswith() -->how its starting
print('codegnan'.startswith('c'))
print('codegnan'.startswith('g',4))
print('codegnan'.startswith('f'))

print('Codegnan'.islower()) #returns True for all lowercase
print('Codegnan'.isupper()) #returns True for all uppercase
print('Codegnan Python'.istitle())

#Space removal --> strip() (removes leading and trailing spaces)

a =' Codegnan '
print(a.strip())
b = input("Enter the string:").strip().lower()
print(b)
'''
# zfill() filling with zeros as per the given numeric string
print('456'.zfill(4))
print('456'.zfill(7))

print('hai'.center(6))
print('hai'.center(6,'#'))

print('hai'.ljust(6,'#'))
print('hai'.rjust(6,'#'))

