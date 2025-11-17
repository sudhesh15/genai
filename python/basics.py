#printing in python
print("Hello Sudhesh");

#checking python version
import sys
print(sys.version)

#indentation example
if 5 > 2:
  print("Five is greater than two!")

#variables - Python has no command for declaring a variable. A variable is created the moment you first assign a value to it.
x = 5
y = "Hello, World!"

#Casting. If you want to specify the data type of a variable, this can be done with casting.
x = str(3)    # x will be '3'
y = int(3)    # y will be 3 
z = float(3)  # z will be 3.0

#Case-Sensitive Variables
a = 4
A = "Sally"
#A will not overwrite a. Which means that a and A are two different variables.

#Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"

#One Value to Multiple Variables
x = y = z = "Orange"

#Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)    
print(z)

#In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
age = 36
# print("My name is John, I am " + age) # This will give an error
#The correct way is to convert the number to a string:
print("My name is John, I am " + str(age))

#Global Variables
x = "awesome"
def myfunc():
  print("Python is " + x)

myfunc()

#If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#The global Keyword

def myfunc():
  global x
  x = "fantastic"

myfunc()
print("Python is " + x)

#Python Data Types
x = "Hello World"    #str
x = 20               #int
x = 20.5             #float
x = 1j               #complex
x = ["apple", "banana", "cherry"]    #list
x = ("apple", "banana", "cherry")    #tuple
x = range(6)                        #range
x = {"name" : "John", "age" : 36}    #dict
x = {"apple", "banana", "cherry"}    #set
x = frozenset({"apple", "banana", "cherry"})  #frozenset
x = True            #bool
x = b"Hello"       #bytes
x = bytearray(5)   #bytearray
x = memoryview(bytes(5))  #memoryview

#Python Numbers
x = 1    #int
y = 2.8  #float
z = 1j   #complex

#Type Conversion
a = float(x)    #convert from int to float
b = int(y)      #convert from float to int
c = complex(x)  #convert from int to complex

#Random Number
import random
print(random.randrange(1, 10))

#Python Strings
a = "Hello, World!"

#Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

#String Methods
a = " Hello, World! "
print(a[1])      #returns "H"

#looping Through a String
for x in "banana":
  print(x)

#String Length
a = "Hello, World!"
print(len(a))

#Check String
txt = "The best things in life are free!"
print("free" in txt)

#Using "not in"
txt = "The best things in life are free!"
print("expensive" not in txt)

#Slicing
b = "Hello, World!"
print(b[2:5])    #returns "llo" Get the characters from position 2 to position 5 (not included)

b = "Hello, World!"
print(b[:5])   #returns "Hello" Get the characters from the start to position 5 (not included)

b = "Hello, World!"
print(b[2:])   #returns "llo, World!" Get the characters from position

#Negative Indexing
b = "Hello, World!"
print(b[-5:-2])   #returns "orl" Get the characters from position -5 to position -2 (not included)

#upper() Method
a = "Hello, World!"
print(a.upper())   #returns "HELLO, WORLD!"

#lower() Method
a = "Hello, World!"
print(a.lower())   #returns "hello, world!"

#strip() Method
a = " Hello, World! "
print(a.strip())   #returns "Hello, World!" Remove whitespace from the beginning or the end

#replace() Method
a = "Hello, World!"
print(a.replace("H", "J"))   #returns "Jello, World!" Replace "H" with "J"

#split() Method
a = "Hello, World!"
print(a.split(","))   #returns ['Hello', ' World!'] Split the string into a list

#String Concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)   #returns "Hello World"

#String Format
#F-Strings
name = "John"
age = 36
txt = f"My name is {name}, and I am {age}"
print(txt)   #returns "My name is John, and I am 36"

#Escape Character
txt = "We are the so-called \"Vikings\" from the north."
print(txt)   #returns 'We are the so-called "Vikings" from the north.'

#Python Booleans
print(10 > 9)   #returns True
print(10 == 9)  #returns False 
print(10 < 9)   #returns False

#Python Operators
#Arithmetic Operators
x = 5
y = 2
print(x + y)   #Addition, returns 7
print(x - y)   #Subtraction, returns 3
print(x * y)   #Multiplication, returns 10
print(x / y)   #Division, returns 2.5
print(x % y)   #Modulus, returns 1
print(x ** y)  #Exponentiation, returns 25
print(x // y)  #Floor Division, returns 2

#Comparison Operators
x = 5
y = 2
print(x == y)  #Equal, returns False
print(x != y)  #Not Equal, returns True
print(x > y)   #Greater than, returns True
print(x < y)   #Less than, returns False
print(x >= y)  #Greater than or Equal to, returns True
print(x <= y)  #Less than or Equal to, returns False

#Logical Operators
x = 5
print(x > 3 and x < 10)  #and, returns True
print(x > 3 or x < 4)    #or, returns True
print(not(x > 3 and x < 10))  #not, returns False

#Identity Operators Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

#Membership Operators
x = ["apple", "banana"]
print("banana" in x)   #returns True
print("pineapple" not in x)  #returns True

#bitwise Operators
x = 5  # 0101
y = 3  # 0011
print(x & y)  #AND, returns 1 (0001)
print(x | y)  #OR, returns 7 (0111)

#Python Operator Precedence
x = 5 + 3 * 2
print(x)  #returns 11
y = (5 + 3) * 2
print(y)  #returns 16

#Python Lists - Lists are used to store multiple items in a single variable.
mylist = ["apple", "banana", "cherry"]
print(mylist)

#List items are ordered, changeable, and allow duplicate values.
#List items are indexed, the first item has index [0], the second item has index [1] etc.

#List Length
print(len(mylist))

#List Items - Data Types
list1 = ["apple", "banana", "cherry"]   #str
list2 = [1, 5, 7, 9, 3]                 #int
list3 = [True, False, False]            #bool
list4 = ["apple", 3, True, 40.5]  #mixed data types

#type()
print(type(mylist))

#The list() Constructor
thislist = list(("apple", "banana", "cherry")) #note the double round brackets
print(thislist)

#Access List Items
print(thislist[1])   #returns "banana"
print(thislist[-1])  #returns "cherry"

#Python Collections (Arrays)
#There are four collection data types in the Python programming language:

#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#Dictionary is a collection which is ordered** and changeable. No duplicate members.

#*Set items are unchangeable, but you can remove and/or add items whenever you like.

#Access List Items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])   #returns "banana"
print(thislist[-1])  #returns "cherry"
#Range of Indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])   #returns ['cherry', 'orange', 'kiwi']
print(thislist[:4])    #returns ['apple', 'banana', 'cherry', 'orange']
print(thislist[2:])    #returns ['cherry', 'orange', 'kiwi', 'melon', 'mango']

#Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#Change List Items
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)   #returns ['apple', 'blackcurrant', 'cherry']

#Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]

#insert() Method
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)   #returns ['apple', 'banana', 'watermelon', 'cherry']

#Append() Method
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)   #returns ['apple', 'banana', 'cherry', 'orange']

#Extend() Method
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)   #returns ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

#Remove() Method
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")

#Remove Specified Index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)   #returns ['apple', 'cherry']

#The del Keyword
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)   #returns ['banana', 'cherry']

#Clear() Method
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)   #returns []

#Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

#Loop Through the Index Numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

#List Comprehension - List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
thislist = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in thislist if "a" in x]

#Sort Lists
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)   #returns ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

#Sort Descending
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)   #returns ['pineapple', 'orange', 'mango', 'kiwi', 'banana']

#Custom Sort Function
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)   #returns [50, 65, 82, 23, 100]

#Reverse Order
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)   #returns ['cherry', 'Kiwi', 'Orange', 'banana']

#Copy a List
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)   #returns ['apple', 'banana', 'cherry']
#Another way to make a copy is to use the built-in method list().
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)   #returns ['apple', 'banana', 'cherry']
#use slice operator to make a copy of a list
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]

#Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)   #returns ['a', 'b', 'c', 1, 2, 3]

#Append list2 into list1
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)   #returns ['a', 'b', 'c', 1, 2, 3]

#Extend list1 by list2
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)   #returns ['a', 'b', 'c', 1, 2, 3]

#Python Tuples - A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
thistuple = ("apple", "banana", "cherry")
print(thistuple)   #returns ('apple', 'banana', 'cherry')

#Tuple Items - Allow Duplicates
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)   #returns ('apple', 'banana', 'cherry', 'apple', 'cherry')

#Tuple Length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))   #returns 3

#Create Tuple With One Item
thistuple = ("apple",)   #note the comma

#tuple items - Data Types
tuple1 = ("apple", "banana", "cherry")   #str
tuple2 = (1, 5, 7, 9, 3)                #int
tuple3 = (True, False, False)            #bool
tuple4 = ("apple", 3, True, 40.5)  #mixed data types

#type()
thistuple = ("apple", "banana", "cherry")
print(type(thistuple))   #returns <class 'tuple'>

#The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry")) #note the double round brackets
print(thistuple)   #returns ('apple', 'banana', 'cherry')

#Access Tuple Items
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])   #returns 'banana'
print(thistuple[-1])  #returns 'cherry'

#Range of Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])   #returns ('cherry', 'orange', 'kiwi')
print(thistuple[:4])    #returns ('apple', 'banana', 'cherry', 'orange')
print(thistuple[2:])    #returns ('cherry', 'orange', 'kiwi', 'melon', 'mango')

#Check if Item Exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#Change Tuple Values - Tuples are unchangeable, so you cannot change, add, or remove items once the tuple is created.
#But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y[1] = "kiwi"
thistuple = tuple(y)
print(thistuple)   #returns ('apple', 'kiwi', 'cherry')

#unpack a Tuple
thistuple = ("apple", "banana", "cherry")
(green, yellow, red) = thistuple
print(green)   #returns 'apple'
print(yellow)  #returns 'banana'
print(red)     #returns 'cherry'

#Using Asterisk*
thistuple = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = thistuple
print(green)   #returns 'apple'
print(yellow)  #returns 'banana'
print(red)     #returns ['cherry', 'strawberry', 'raspberry']

#Loop Through a Tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#Join Two Tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)   #returns ('a', 'b', 'c', 1, 2, 3)

#Multiply Tuples
tuple1 = ("a", "b", "c")
tuple2 = tuple1 * 3
print(tuple2)   #returns ('a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c')

#Python Sets - A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
thisset = {"apple", "banana", "cherry"}
print(thisset)   #returns {'banana', 'cherry', 'apple'}

#Set Items - Allow Duplicates
thisset = {"apple", "banana", "cherry", "apple"}

#Set items are unordered, unchangeable, and do not allow duplicate values.

#Duplicate values will be ignored
print(thisset)   #returns {'banana', 'cherry', 'apple'}

#The values True and 1 are considered the same value in sets, and are treated as duplicates
#The values False and 0 are considered the same value in sets, and are treated as duplicates

#Set Length
thisset = {"apple", "banana", "cherry"}
print(len(thisset))   #returns 3

#Data Types in Sets
set1 = {"apple", "banana", "cherry"}   #str
set2 = {1, 5, 7, 9, 3}                #int
set3 = {True, False, False}            #bool
set4 = {"apple", 3, True, 40.5}  #mixed data types

#type()
thisset = {"apple", "banana", "cherry"}
print(type(thisset))   #returns <class 'set'>

#The set() Constructor
thisset = set(("apple", "banana", "cherry")) #note the double round brackets
print(thisset)   #returns {'banana', 'cherry', 'apple'}

#Access Set Items - You cannot access items in a set by referring to an index or a key.
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#Check if Item Exists
thisset = {"apple", "banana", "cherry"}
if "banana" in thisset:
  print("Yes, 'banana' is in the fruits set")

#Add Items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)   #returns {'banana', 'cherry', 'orange', 'apple'}
#Add Multiple Items
thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])
print(thisset)   #returns {'banana', 'cherry', 'orange', 'apple', 'mango', 'grapes'}

#Remove Items
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)   #returns {'cherry', 'apple'}

#pop Method
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)   #returns 'banana' (or another random item)
print(thisset)   #returns the set without the popped item

#The del Keyword
thisset = {"apple", "banana", "cherry"}
del thisset
#print(thisset)   #this will raise an error because the set no longer exists

#Clear Method
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)   #returns set()

#Loop Through a Set
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#Join Two Sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)   #returns {'a', 1, 2, 3, 'c', 'b'}

#Update set1 with set2
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)   #returns {1, 2, 3, 'a', 'c', 'b'}

#Join a Set and a Tuple
set1 = {"a", "b", "c"}
tuple1 = (1, 2, 3)
set1.update(tuple1)
print(set1)   #returns {1, 2, 3, 'a', 'c', 'b'}

#Intersection of Two Sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)   #returns {'apple'}

#intersection_update() Method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)   #returns {'apple'}

#The values True and 1 are considered the same value. The same goes for False and 0.

#Difference of Two Sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)   #returns {'banana', 'cherry'}

#symmetric_difference() Method - method will keep only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)   #returns {'banana', 'cherry', 'microsoft', 'google'}

#Python Dictionaries - A dictionary is a collection which is ordered** and changeable. In Python dictionaries are written with curly brackets, and they have keys and values.

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}

#Dictionary items are ordered, changeable, and do not allow duplicates.
#Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

#Length of a Dictionary
print(len(thisdict))   #returns 3

#Dictionary Items - Data Types
dict1 = {"brand": "Ford", "model": "Mustang", "year": 1964}   #str
dict2 = {1: "apple", 2: "banana", 3: "cherry"}                #int
dict3 = {True: "yes", False: "no"}                            #bool
dict4 = {"name": "John", 1: [2, 4, 3]}                        #mixed data types

#type()
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(type(thisdict))   #returns <class 'dict'>

#The dict() Constructor
thisdict = dict(brand="Ford", model="Mustang", year=1964)
print(thisdict)   #returns {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

#Access Dictionary Items
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict["brand"])   #returns 'Ford'
print(thisdict.get("model"))  #returns 'Mustang'    

#Get Values
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = thisdict.values()
print(x)   #returns dict_values(['Ford', 'Mustang', 1964])

#Get Items
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = thisdict.items()
print(x)   #returns dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

#Check if Key Exists
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

#Change Dictionary Items
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict["year"] = 2018
print(thisdict)   #returns {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}

#Update Dictionary
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.update({"year": 2020})
print(thisdict)   #returns {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

#Add Dictionary Items
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict["color"] = "red"
print(thisdict)   #returns {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

#update() Method
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.update({"color": "white"})
print(thisdict)   #returns {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'white'}

#Remove Dictionary Items
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.pop("model")
print(thisdict)   #returns {'brand': 'Ford', 'year': 1964}

#The del Keyword
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
del thisdict["year"]
print(thisdict)   #returns {'brand': 'Ford', 'model': 'Mustang'}

#Clear() Method
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.clear()
print(thisdict)   #returns {}   

#Loop Through a Dictionary
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
for x in thisdict:
  print(x)   #prints the keys

for x in thisdict.values():
  print(x)   #prints the values 

for x, y in thisdict.items():
  print(x, y)   #prints both keys and values

#Copy a Dictionary
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
mydict = thisdict.copy()
print(mydict)   #returns {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

#Another way to make a copy is to use the built-in dict() function.
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
mydict = dict(thisdict)
print(mydict)   #returns {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

#Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)   #returns the nested dictionary

#Accessing Items in Nested Dictionaries
print(myfamily["child1"]["name"])   #returns 'Emil'
print(myfamily["child2"]["year"])   #returns 2007

#Python Conditions and If Statements
a = 33
b = 200
if b > a:
  print("b is greater than a")

#Elif
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#Else
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Short Hand If
a = 200
b = 33
if a > b: print("a is greater than b")

#Short Hand If ... Else
a = 2
b = 330
print("A") if a > b else print("B")

#Logical Operators
#and
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#or
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#Nested If
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#The pass Statement
a = 33
b = 200
if b > a:
  pass

#Match Statement
x = 2
match x:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Something else") #returns "Two"

#While Loops
i = 1
while i < 6:
  print(i)
  i += 1

#Break Statement
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#Continue Statement
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#Else Statement
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

#For Loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Looping Through a String
for x in "banana":
  print(x)

#The break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#The continue Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#The range() Function
for x in range(6):
  print(x)

#Else in For Loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#Functions in Python
def my_function():
  print("Hello from a function")

my_function()

#Function Arguments
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")

#*args - this function will receive a tuple of arguments
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#**kwargs - this function will receive a dictionary of arguments
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#Scope of Variables in Functions
#Local Scope
def my_function():
  x = 300
  print(x)
my_function() #returns 300

#Global Scope
x = 300
def my_function():
  print(x)
my_function()
print(x) #returns 300

#Lamda - A lambda function is a small anonymous function.
x = lambda a : a + 10
print(x(5)) #returns 15
