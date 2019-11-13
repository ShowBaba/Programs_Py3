import math

for i in range(5):
    print(i, end='')  # end keeps everything on a straight line

for i in range(4):
    print('#'*(i+1))

print("specify number of boxes")
user = int(input())
for i in range(user):
    print('*'*(i + 1))

print('*' * 10)
print('*', '*', sep='        ')
print('*', '*', sep='        ')
print('*' * 10)

height = int(input("Specify a lenght: "))
width = int(input("Specify a width: "))
for i in range(width):
    print('*', '\n -' * (width - 2))

# import math
print("Pi is roughly", math.pi)
print("sin(60)", abs(math.sin(60)))  # abs = absolute value
print("sin30", abs(math.sin(30)))
import math
dir(math)  # get help on the math module, type this in python shell


x = "My name is sammy"
y = "And am  a goodboy"
print(x, end=" --- ")  # the end syntax appends the argument inside of it instead of a new line
print(y)


var1 = input("input a number")
var2 = input("input a string")
command = input()
if command == "deletevar1":
    del var1

print(var2)
print(var1)

list = ['abcd', 786 , 2.23, 'john', 70.2]

print("Here  is a list of jargon", list)
your_jargon = input("add your jargon")

list.append(your_jargon)

print(list)

m = "mofos arena"

m = m.title()  # title method give an uppercase to the first letter of every word in the string

print(m)


print("State and capital search")

dict = {'Abia': 'Umuaya', 'Adamawa': 'Yola', 'Akwa Ibom': 'Uyo', 'Anambra': 'Akwa', 'Bauchi': 'Bauchi', 'Benue': 'Makurdi', 'Bornu': 'Maiduguri', 'Cross river': 'Calabar',
'Delta': 'Asaba', 'Edo': 'Benie', 'Enugu': 'Enugu', 'Gombe': 'Damaturu', 'Imo': 'Owerri', 'Jigawa': 'Dutse', 'Kastina': 'Kastina','Kebbi': 'Benie Kebbi', 'Kwara': 'Ilorin',
'Lagos':'Ikeja', 'Ogun': 'Abeokuta', 'Osun': 'Oshogbo', 'Oyo': 'Ibadan', 'Platue': 'Jos', 'Rivers': 'Port Harcourt'}

print(dict.keys())
print(dict['Ogun'])  # can search for values only with keywords in single quotes

search = ''

while search not in dict:
    search = input("Enter Search: ").title()    # title() Capitalize makes the first letter uppercase
    print("Your search can't be found in the dictionary")
    continue


print(search, "=", dict[search])

print("Convert to binary, octal and hexadecimal")

num = int(input(': '))

print('Binary = ', bin(num))
print('Octal =', oct(num))
print('Hexadecimal = ', hex(num))


count = 0

while count < 10:
    print('The count is:', count)
    count += 2
    print()  # this line adds an empty new line after each values
    print('________________')
    print('----------------')
else:
    print("Count is now equal to", count)

print("Good bye!")


fruits = ['banana', 'apple', 'mango']

for fruit in range(len(fruits)):
    print('Current fruit : ', fruit)
print("Good bye!")

print(len(fruits))
# print(sum(data))  #prints the sum of values in a list


numbers = [11, 33, 55, 39, 55, 75, 37, 21, 23, 41, 13, 14, 20]

for num in numbers:
    if num %2 == 0:
        print('The list contains an even number')
        break  # Terminates the loop statement and transfer execution
    # to the statement immediately following the loop
    # if the break statement is not present the loop will repeat
    # the print statement twice cos there are two even numbers in the list
    # the CONTINUE statement Causes the loop to skip the remainder of its
    # body and immediately retest its condition prior
    # to reiterating.
    # The CONTINUE statement will repeat the print statement twice
else:
    print("The list does not contain an even number")



import sys

for i in range(1,13):
    for j in range(1,13):
        k = i * j
        print(k, end=' ')  # The print() function inner loop has end=' ' which appends a space instead of default
        # newline. Hence, the numbers will appear in one row.
        # Last print() will be executed at the end of inner for loop.+


    print()


# The maketrans() method returns a translation table that maps each character in the
# intabstring into the character at the same position in the outtab string. Then this table is
# passed to the translate() function.

intab = "aeiout"
outtab = "123457"

trantab = str.maketrans(intab, outtab)
str = "this is string example.........wow!!!"
print(str.translate(trantab))  # replace intab elements with its corresponsible outtab value
# could actually be used to make an encrypted messanging script


print("Sign up here")
print("\n")

username = ''
password = ''
while not username:
    username = input("Username: ")
    continue
while not password:
    password = input("Password: ")
    continue

print("\n")
print("Now login")

while True:
    name = input("Username: ")
    if name != username:
        continue
    pass_word = input("Password: ")
    if pass_word == password:
        break
    else:
        print("Username or Password is incorrect")
print('\n')
print("ACCESS GRANTED!")




import sys

# encrypting a message

key_one = str(input("Input key one: "))  # E.g  "aeioutgyls"
key_two = str(input("Input key two: "))  # E.g  "1234567890"

transkeys = str.maketrans(key_one, key_two)
msg = str(input("Write message to be encrypted: "))
print("\n\n")

encrypted_msg = msg.translate(transkeys)
print(encrypted_msg)
print("\n\n\n")
command = input("Enter YES to decrypt messange, NO to exit: ").upper()


# To decrypt the the above
if command == "YES":
    transkeys = encrypted_msg.maketrans(key_two, key_one)
    decrypted_msg = encrypted_msg.translate(transkeys)
    print(decrypted_msg)
elif command == "NO":
    print("Thank you and Good bye!")
    sys.exit()
else:
    print("Good Bye!")
    sys.exit()



import time

print(time.localtime()) # gives the current system time and date
# OR SAY
localtime = time.localtime(time.time())
print("Current local time: ", localtime)
# OR IN A BETTER FORMAT

localtime = time.asctime(time.localtime(time.time())) # time.asctime([tupletime])
# Accepts a time-tuple and returns
# a readable 24-character string such as 'Tue Dec11 18:07:14 2008'.
print("Current local time: ", localtime)


import time

localtime = time.strftime("%B %d %Y %H:%M:%S") # asctime is one of many formatting func
print("Current local time: ", localtime)


import time

t = (1998, 5, 16, 10, 39, 45, 1, 48, 0)
t = time.mktime(t)
print("My date of birth is:", time.strftime("%B %d %Y %H:%M:%S", time.localtime(t)))


def sum_func(n1,n2):  # the parameter here is n1 and n2 that is passed into a function

    sum = n1 + n2
    print("sums of input = ", sum)
    return

# arguments are the values we  pass to a parameter when we call the function

def diff_func(n1,n2):
    diff = n2 - n1
    print("difference of inputs", diff)
    return


# above is a module i made and named summodule.py stored in python PATH
# using the   import summodule
# summodule.sum_func(45, 35)
# OR
# from summodule import *
# #sum_func(33, 66)

# in another python program, i can actually call my custom made module for use
# if you have more then one function name in a module you can call out any of them using
# from summodule import sum_func ..... this only calls the sum_func function
# sum_func(45, 35)......... this is used instead of the previous
# also an entire module can be imported using
# from summodule import  * .....however this statement should be used sparingly
# to maybe prevent cummbersumity ##smiles............


n = str(input("Write something: "))

file = open("test_file.txt", "w")
file.write(n)   # writes to file but deletes any previous data

file.close()


file = open("test_file.txt", "r+")
str = file.read(10)  # specifies the number of byte (letters) to beb read
print(str)

position = file.tell()
print(position)  # returns the number of bytes read



data = [9, 6, 8, 7]
data2 = [1, 2, 2, 3]
ab = []
# to multiply each element in data by there
# corresponding value in data2

for i in range(0, len(data)):
    ab.append(data[i]*data2[i])

print(ab)


# creating a matrix using list func
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]

]

print(matrix)

# to access the indexes in the matrix

print(matrix[0][1]) # this will return the first value of the  first list


def population_count(male, female):
    assert (male  <= 1000), 'Too much of males, kill off some of them' # assertion is a self defined exception
    assert (female <= 2000), 'Too much females, save some for the future'
    print(f'There are as much as {female - male} females to males in the country')
    if female - male < 100:
        print('The population looks unstadey, as there more males than females')
    else:
        print('The population is steady')


male = int(input("Number of males: "))
female = int(input("Number of females: "))

population_count(male, female)


# say we have a tuple
weapons_clips = (43, 56, 34, 23)
# we can assign each of the elements in the tuple to a seperate variable using
# the method called UNPACKING

m16, ak47, cot45, handgun = weapons_clips
# the above line of code assign to each tuple value its corresponding defined variable
# instead of assingning its each seperately
# UNPACKING can also be used with other data type like list


# A number to word system
number_words = {'0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five',
                '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine,', '10': 'Ten'}
phone = input(': ')
phone = str(phone)
# print(phone)

for i in phone:
    print(number_words.get(i, '!'), end=', ')


# here is a simple program to convert a user input into a list
message = input('Input any message here: ')
message_into_list = message.split(' ') # the quote and space in the parentences is to seperate each value of the input
# here the split method is used
print(message_into_list)


# Classes are types or say objects similar to list, dictionaries and others
# they are created by a user with a defined method
# just like list has its own defined method like
# append(), pop() and others
# and the methods defined to a class can be accessed
# just like other python types
# by class_name.method()
# Now lets create a new class


class Ak47:  # define a class and give it a name that starts with uppercase letter
    # Ak47 is an object
    # next define the functions or methods that belong to the class

    def __init__(self, shoot, reload):  # defining a constructor, and adding arguments
        # self here is a reference to the current object
        self.shoot = shoot
        self.reload = reload

    def range(self):  # the self keyword is automatic
        print('Goes 20km in air')

    def damage(self):
        print('Causes a 20% damage on impact')

    def clip(self):
        print('Can hold 20 rounds in one magazine')


# the above class defined a new type
# with the new type we can create new object
# an object is an instance of a class
# the class simply define a template or blueprint for creating object
# and object are the actual instances based on that blueprint

# now lets create an object

gun = Ak47(-20, +100)  # call the object, and store it in a variable
# since we are now using the constructor method we have to pass in arguments
# now use the dot operation to see the list of methods in the class
# the other methods starting with two underscores are called magic methods
# you can then call each methods below

gun.damage()
gun.clip()
gun.range()

# apart from methods objects can also take an attribute outside the block
# this attributes are like variables that belong to a particular object

# gun.shoot = -20  # this are attributes of the the object Ak47 which have been assigned a variable named gun

# gun.reload = +100

# now we can print the attributes
print(gun.shoot)
print(gun.reload)

# a constructor is a function that gets called at the time of creating an object
# a constructor can be used to add an attribute instead of the above way
# to use a constructor we define another function in the class block
# with a function name called __init__


# Another example of classes and object below
# the class below define a Person which has a name attribute and a talk() method
print('\n')


class Person:
    def __init__(self, name):  # add a name attribute using the constructor method
        self.name = name  # self references the current object

    def talk(self):
        print(f'Hi, i am {self.name}')  # to dynamically add the name of the person
        # using formatted string, with self as an argument in this method
        # we can get reference to the current object


# now create a person object
mark = Person('Mark') # pass in the argument
mark.talk()

# now lets create a new person object
ayo = Person('Ayo')
ayo.talk()
# so each object is a different instance of a person class


