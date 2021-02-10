'''
Text Type (String)
'''
# s = "This is a single line string"
# print(s)
# print(type(s))


#===============================

# s = ''' this is a multiline
# string example'''
# print(s)

#===============================

# find a character by  index 
# s =  'string sample' 
# print(s[5])

# slicing
# s ='string sample'
# print(s[7:])

# s ='string sample'
# print(s[0:6])

#===============================
#immutable

# s ='string sample'
# s[2] = 'o'
# print(s)


'''
Numeric  Type  (Integer, Float, Complex)
'''
#  x = 1234534567459586
#  print(type(x))

# accurate up to 15 - 16  decimal  places 
# x = 0.1234567898765432123445334
# print(type(x))
# print(x)

# x = 1+2j
#print(type(x))

'''
Sequence Type (list, Tuple, Range)
'''
# homogeneous  
# x = []
# List
# x = [10,2.5,'hello']
# print(x[2])
# print(x[1:3])

# mutable
# x[2] = 'Python'
# print(x)

# Tuple
# heterogeneous
# tuple = ()
# tuple =  ("cat", [4,3,2] , (1,2,3))

#===============================
# both examples below are type of tuples, without comma makes it a string.
# tuple =  ("hello")
# tuple = "hello",
# print(type(tuple))

# tuple =  ("cat", [4,3,2] , (1,2,3))
# print(tuple[2])

#===============================

# immutable
# tuple =  ("cat", [4,3,2] , (1,2,3))
# tuple[2] = 10
# print(tuple)

# Range 

# x = range(20)
# for n  in x:
# print(n)

'''
Mapping Type (dictionary)
'''
# dict = {}
# print (type (dict))

#===============================
# dict  is mutable 
#dict =  {'name': 'Victor', 'age': 40}
# print(dict['name'])
#print(dict['age'])
#print(dict.get('name'))

# dict['age'] = 26
# print(dict)

'''
Set Types
'''
# empty  set  having set  =  {} is an empty  dict
# set = {1,2,3}
# print(type(set))
# TypeError: 'set' object is not subscriptable
# print(set(0))

#===============================
# no duplicates

# set = {3.2, "hi", (1,2,3), "hi"}
# print(set)
#===============================

# we cannot have mutable (list) in  a set 
# set = {3.2, "hi", (1,2,3), [1,2,3]}
# print(set)


'''
Boolean  Types (True or false)
'''

# print(type(True))
# print(True == 1)
# print(False == 0)

# interesting logic
# print(True + True)

# not boolean  operator 
# print(not True)
# print(not False)

# and boolean operator 
# print(True and False)
# print(True and True)
# print(False and False)

# or boolean  operator
print(True or False)
print(True or False)
print(False or False)