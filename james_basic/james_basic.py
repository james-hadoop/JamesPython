import random
import sys
import os

# Comment

'''
Multi comments
'''
# Numbers Strings Lists Tuples Dictionaries
# + - * / % ** //

print("Hello World")

myName = "James"
print(myName)

print("1+2-3*3=", 1 + 2 - 3 * 3)

quote = "\"Always remember you are unique\""
multi_line_quote = '''just
like everyone else'''

new_string = quote + multi_line_quote
print("%s %s %s" % ('I like the quote', quote, multi_line_quote))

# List
grocery_list = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']
print('First Item', grocery_list[0])
grocery_list[0] = "Green Juice"
print('First Item', grocery_list[0])

print(grocery_list[1:3])

other_event = ['Wash Car', 'Pick Up Kids', 'Cash Check']
to_do_list = [other_event, grocery_list]
print((to_do_list[1][1]))

grocery_list.append('Onions')
print(to_do_list)

grocery_list.insert(1, 'Pickle')
grocery_list.remove('Pickle')
grocery_list.sort()
grocery_list.reverse()

del grocery_list[4]
print(to_do_list)

to_do_list2 = other_event + grocery_list
print(len(to_do_list2))
print(max(to_do_list2))

# Tuple
pi_tuple = (3, 1, 4, 1, 5, 9)
new_tuple = list(pi_tuple)
new_list = tuple(new_tuple)

# Dictionary
super_villains = {'Fiddler': 'Isaac Bowin', 'Captain cold': 'Leonard Snart', 'Weather Wizard': 'Mark Mardon',
                  'Mirror Master': 'Sam Scudder', 'Pied Piper': 'Thomas Peterson'}
print(super_villains['Captain cold'])
del super_villains['Fiddler']
super_villains['Pied Piper'] = 'Hartley Rathaway'
print(len(super_villains))
print(super_villains.get('Pied Piper'))
print(super_villains.keys())
print(super_villains.values())

# if else elif == != > < >= <= and or not
age = 21

if age > 16:
    print('You are old enough to drive')
else:
    print('You are not enough to drive')

if age >= 21:
    print('You are old enough to drive a tractor tailor')
elif age >= 16:
    print('You are old enough to drive a car')
else:
    print('You are not old enough to drive a car')

age = 30
if ((age >= 1) and (age <= 18)):
    print('You get a birthday')
elif ((age == 21) or (age >= 65)):
    print('You get a birthday')
elif not (age == 30):
    print("You don't get a birthday")
else:
    print("You get a birthday party yeah")

# loop
for x in range(0, 10):
    print(x, ' ')

print('\n')

for y in grocery_list:
    print(y)

for x in [2, 4, 6, 8, 10]:
    print(x)

num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]
for x in range(0, 3):
    for y in range(0, 3):
        print(num_list[x][y])

random_num = random.randrange(0, 100)
while (random_num != 15):
    print(random_num)
    random_num = 15

i = 0;
while (i <= 20):
    if (i % 2 == 0):
        print(i)
    elif (i == 9):
        break
    else:
        i += 1
        continue
    i += 1


# funciton
def addNumber(fNum, lNum):
    sumNum = fNum + lNum
    return sumNum


print(addNumber(4, 400))

print('What is your name?')
# name=sys.stdin.readline()
# print('Hello ',name)

long_string = "I'll catch you if you fall down to the floor."
print(long_string[0:4])
print(long_string[-5:])
print(long_string[:-5])
print(long_string[:4] + " be there")
print("%c is my %s letter and my number %d number is %.5f" % ('X', 'favorite', 1, 0.14))

print(long_string.capitalize())
print(long_string.find("Floor"))
print(long_string.isalpha())
print(len(long_string))
print(long_string.replace("Floor", "Ground"))

quote_list = long_string.split(" ")
print(quote_list)

# io
test_file = open("test.txt", "w")
print(test_file.mode)
print(test_file.name)
test_file.write("Write me to the file\n")
test_file.close()

test_file = open("test.txt", "r+")
text_in_file = test_file.read()
print(text_in_file)
test_file.close()
os.remove("test.txt")


# object
class Animal:
    __name = ""
    __height = 0
    __weight = 0
    __sound = 0

    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_height(self):
        return self.__height


    def get_weight(self):
        return self.__weight

    def get_sound(self):
        return self.__sound

    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} is {}cm tall and {}kilograms and sya {}".format(self.__name, self.__height, self.__weight,
                                                                   self.__sound)


cat = Animal('Whiskers', 33, 10, 'Meow')
print(cat.toString())


# inherit
class Dog(Animal):
    __owner = ""

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        super(Dog, self).__init__(name, height, weight, sound)

    def get_type(self):
        print("Dog")

    def toString(self):
        return "{} is {}cm tall and {}kilograms and sya {} whose owner is {}".format(self.get_name(), self.get_height(),
                                                                                     self.get_weight(),
                                                                                     self.get_sound(), self.__owner)

    def multiple_sounds(self, how_many=None):
        if how_many is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many)


spot = Dog("Spot", 53, 27, "Ruff", "Derek")
print(spot.toString())


class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()


test_animals = AnimalTesting()
test_animals.get_type(cat)
test_animals.get_type(spot)

spot.multiple_sounds(4)
spot.multiple_sounds()
