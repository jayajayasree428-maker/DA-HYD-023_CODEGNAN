'''
Mapping --> Dictionary --> Collection of key-value pairs used to store
related data --> JSON,APIs,database records
dict() --> data = {k : value}
Dictionary is MUtable,Indexed through keys,Ordered,Heterogeneous,
Keys must be unique
keys must be unique (int,strings,float values...)
'''
datails = {}
print(type(datails))

details = {'id':'CGH3940','Name': 'jaya',
           'Gender':'F','Age':22,
           'Batch':'DA23','Place':'Hyd'}

print(details)
print(len(details))

#Access the data from dictionary
#details[0] #keyError

print(details.keys()) #it returns keys from the dictionary
print(details['id'],details['Name'])
#if key name is not matching / invalid
#print(details['marks']) #keyError as marks is not present
details['marks'] = []
print(details)
print(type(details['marks']))
      
details['marks'].append(20)
print(details)
details['marks'].extend([15,20,25,20,20])
print(details)

#create a key-value pair of practice Session

details['PS'] = ('Tuesday','Thursday','Saturday')

print(details.keys())
#Accessing 3rd day marks of student
print(details['marks'][2])
#Accessing 2nd day of practice session
print(details['PS'][1])
details['MI'] = ('Monday','Wednesday','Friday')
#operations -->mutable,indexing through keys,membership

print('Wednesday')
print('MI' in details) #returns True as we have MI as key
'''for i in details:
    print(i) #returns keys one by one

for i in details.keys():
    print(f'key = {i}')
    print(f'value = {details[i]}')


#keys() --> returns keys from the dictionary

for i in details.values(): #returns value from dictionary
    print(i)

for i in details.items(): #returns a key-value pair
    print(i)

for key,value in details.items():
    print(f'key is{key}')
    print(f'value is {value}')

#update() --> updating the dictionary with key-value pairs
details.update({'marks':[],
                'PS':('Tuesday','Thursday','Saturday')})
print(details)
details['marks'].extend([25,30,25])
print(details)
marks = list(map(int,input("Enter the marks:").split(',')))
print(marks)
details['marks'].extend(marks)
print(details)
'''
print(details.keys())
print(details.get('Name'))
print(details.get('Branch')) #it returns None as we dont have Branch as key
print(details.keys())

details.setdefault('Branch','ECE') #if key is not present it inserts into dict
print(details)
details['Branch'] = 'CSE'
print(details)

print(details.setdefault('Name'))
print(details.keys())

print(details.pop('Branch')) #we need to mention key
print(details.keys())

print(details.popitem()) #removes and return a key,value pair as a 2-tuple
print(details.popitem())

del details['id']
print(details.keys())

details.clear() #it removes all elements from D
print(details)

#fromkeys()

data = ['jaya','sai','data']
b = (dict.fromkeys(data)) #creates a dictionary but value set to none
print(b)
b['jaya'] = 22
print(b)
c = dict.fromkeys(['CGH2345']),(['code','gnan'])
print(c)

#Task: Create a dictionary with your personal details,similar to your
#Codegnan Profile



    

