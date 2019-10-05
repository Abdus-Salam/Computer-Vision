'''
# Mutable and Immutable type
==================================================================
# mutable type(list) : value is not change
# immutable type(int / string / tuple) : value is change
'''
# exmple of immutable type

# example of mutable type

list1 = [1, 2, 3, 4]

print(id(list1))

list1.append(4)

print(id(list1))  # value is not change, so list is mutable type


x = 1
print(id(x))

x = x + 1

print(id(x))  # value is change so int is immutable type.


'''
String
===============================================================
'''

string = "Python programming"

print(string[0])  # first character
print(string[-1])  # from reverse position
print(string[0:3])  # from 0 to 2
print(string[:3])  # from 0 to 2
print(string[0:])  # from 0 to n
print(string[:])  # from 0 to n


'''
Escape sequence
===============================================================
\\
\"
\'
\n
'''

message = """Python
      Programming
"""

print(message)


'''
String formatting and some usefull method
===============================================================
'''

firstname = "Abdus"
lastname = "Salam"

# fullname = firstname + " " + lastname
fullname = f"{firstname} {lastname}"

print(fullname)


course = " Python Programming"

print(course.upper())
print(course.lower())
print(course.split())
print(course.strip())
print(course.find("Pro"))
print(course.replace("P", "-"))
print("Programming" in course)
print("Programming" not in course)


'''
Numbers
===============================================================
'''

x = 0b10  # binary representation
y = 0x12c  # hexa representation
z = 2 + 1j  # here j is the imaginary number in python
print(bin(x))
print(hex(y))
print(z)


'''
Conditional operator and logical opertator
===============================================================
'''

x = 22
if x == 0:
    pass  # nothing
if x == 22:
    print("Yes")


if x >= 18 and x < 65:
    print("Eligible")

if 18 <= x < 65:
    print("Eligible")


'''
Ternary operator
===============================================================
'''
age = 18

# work in other language not in python
# message = age >= 18 ? "Eligible": "Not eligible"
message = "Eligible" if age >= 18 else "Not eligible"
print(message)


'''
for loop
for else
===============================================================
'''
print(type(range))
for i in range(5):
    print(i)


# for else
found = False
for i in range(5):
    if i == 6:
        print("Found")
        found = True
        break
if not found:
    print("Not found")


# for else , not need found flag !
for i in range(5):
    if i == 6:
        print("Found")
        break
else:
    print("Not found")


'''
Functions
===============================================================
'''


def increment(number, by=1):
    return (number, number + by)

# use of annotation


def increment2(number: int, by: int = 1) -> tuple:
    return (number, number + by)


print(increment(2, 3))  # return tuple. tuple is list.
print(increment2(3))


'''
*args : return tuples
**args : return js object
===============================================================
'''


def multiply(*list):
    total = 1
    for number in list:
        total *= number

    return total


def save_user(**user):
    print(user)
    print(user['id'])


print(multiply(2, 3, 4, 5))
save_user(id=1, name='Admin')


'''
Local variable and global variable
===============================================================
'''
message = 'a'


def greet():
    # if you want to effect to this global variable then give the reference with global keyword
    global message

    message = 'b'


greet()

print(message)


'''
Remove duplicate element from list
===============================================================
'''

numbers = [2, 2, 5, 5, 3, 4, 6, 1, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)

uniques.sort()
print(uniques)


'''
Tuple / Unpacking : tuple is look like list which is not changed
===============================================================
Only two method : count, index
Type is unpacking
'''

# unpacking feature

coordinates = (1, 2, 3)
x, y, z = coordinates  # also works in list
print(x * y * z)


coordinates = [1, 2, 3]
x, y, z = coordinates  # also works in list
print(x * y * z)


'''
Dictionary
=========================================================
Duplicate key is not supported.
'''

customers = {
    "name": 'Abdus Salam',
    'age': 26,
    'is_verified': True
}

customers['dateOfBirth'] = '03/01/1993'  # add new keys value

print(customers['name'])
# print(customers['newKey'])  # occured error
print(customers.get('name'))
print(customers.get('newKey'))
print(customers.get('newKey', 'Assign new value'))


# examples
# phone : 123 -> one two three

phones = input('Enter numbers')

digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Five",
    "5": "Six"
}

output = ""
for ch in phones:
    output += digits_mapping.get(ch, "!") + " "
print(output)
