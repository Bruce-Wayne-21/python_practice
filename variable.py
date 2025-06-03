from practiceFuntion import newfuntion

# age_input=input("enter your name")
# age=int(input("Enter your age "))
#
# if age <0:
#     print("plese enter the valid value")
# elif age <10:
#     print(" you are minor")
# elif age < 20:
#     print("You are major")
# else:
#     print("hi i am ssajilan ")
from operator import truediv

# x,y=input("Enter two values").split()
# print("number of boys",x)
# print("number of the girls",y)


#
# a = "hello world"
# b = 10
# c = 11.22
# d = ("sajilan",) * 3
# e = ["saji"] * 2
# f = {"geeks", 1, "saji"}
#
# print(type(a),
#       type(b),
#       type(c),
#       type(d),
#       type(e),
#       type(f))


#  ###################################################  ( string interpolation) #####################################################
# amount = 150.75
# print("Amount: ${:.2f}".format(amount))
#
# print("geeks for geeks : %2d portal : %5.2f" % (1, 4.5))
# print("hello %s" % "sajilan")
#
# print("hello %s %d" % ("sajilan", 10))
#
# print("my name is {0} and my age is {1}".format("sajilan", 10))
# print ("my dog name is {} and my name is {}".format("dog", "sajilan"))
#
# template="Number is {0},{1},and {saj}"
# print(template.format(1,2,saj=3))


############################################# Formatting Output using String Methods ####################################

# cstr = "I love geeksforgeeks"
#
# # Printing the center aligned string with fillchr
# print("Center aligned: ")
# print(cstr.center(40, '#'))
#
# # Printing the left aligned string with "-" padding
# print("left aligned: ")
# print(cstr.ljust(40, '-'))
#
# # Printing the right aligned string with "-" padding
# print("right aligned: ")
# print(cstr.rjust(40, '-'))


###############################################  (Python build in function ) #####################################################

# value = 10
# formated=format(value, 'b')
# print(formated)   #######	Binary format.
# fprmat=format(value, 'd')
# print(fprmat)   #######		Decimal format.
# formated=format(value, 'e')
# print(formated)   #######	Scientific format.
# formated=format(value, 'f')
# print(formated)   #######	Floating point format.`
# formated=format(value, 'o')
# print(formated)   #######	Octal format.
# formated=format(value, 'x')
# print(formated)   #######	Hexadecimal format.
# formated=format(value, 'X')
# print(formated)   #######	Uppercase Hexadecimal format.
# formated=format(value, 'n')
# print(formated)   #######	Number format.
#
# str_value = 2.00
# formated = format(str_value,'2f')  # No format spec needed for a string
# print(formated)#######	Character format.
#
# varible=[1,2,3,4,5]
# for i in varible:
#     print(i)
#
# variable = [1, 2, 3, 4, 5]
# print(*variable)
#
# names=["saijilan","saj","saji"]
# for i in names:
#     print(i)
#
# print(*names)

############################################# ( loop ) #############

# numbers = [1, 2, 3, 4, 5]
# for i in numbers:
#     if i == 3:
#         variable = True
#     else:
#         variable = False
#     while variable:
#         saji = ["saji", "saijilan", "saj"]
#         for name in saji:
#             if name == "saji":
#                 print("hello sajilan parameswaran ")
#                 break
#         variable = False  # To prevent infinite loop
#
#
# groups = [["Jobs", "Gates"], ["Newton", "Euclid"], ["Einstein", "Feynman"]]
#
# for data in groups:
#     for i in data:
#         print(i)
#
# ############################################ Pattern printing######################
#
# rows = 5  # Number of rows for the pattern
# for i in range(1, rows + 1):
#     print('*' * i)
#
# numbers = [0, 254, 2, -1, 3]
#
# for num in numbers:
#     if (num <0):
#         print("negative number")
#         break
#     print(num)
#
# # Nested loop with a placeholder for incomplete logic
# for i in range(3):
#   for j in range(3):
#     if i == j:
#       # Placeholder for future implementations
#       pass
#     else:
#       print(f"i: {i}, j:{j}")


########################### ternary operator ##########################

# age = 18
# message ="you are very smart" if age > 18 else "you are not smart"
# print(message)

# price = 100
# if price >=100:
#     pass
# else:
#     print("price is less than 50")

# point = (0, 2)
#
# match point:
#     case (0, y):
#         print(f"Y axis at {y}")
#     case (x, 0):
#         print(f"X axis at {x}")
#     case (x, y):
#         print(f"Point at {x}, {y}")
#
#
# command ="start"
# match command:
#     case "start":
#         print("Starting the process")
#     case "stop":
#         print("Stopping the process")
#     case _:
#         print("Unknown command")


########################## loop #############

for i in range(3, 10, 1):
    print(i)

names = ["sajilan", "saji", "saj"]
[print(names) for names in names]


def function(num):
    for item in num:
        if item % 2 == 0:
            return f"{item} is even"
        elif item % 2 != 0:
            return f"{item} is odd"
        else:
            return f" {num}not a number"


var = function
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(var(number))


def function1(num):
    if num % 2 == 0:
        return f"{num} is even"
    elif num % 2 != 0:
        return f"{num} is odd"
    else:
        return "not a number"


var = function1
print(var(10))

# What happens:
# You call function(number), with number = [1, 2, 3, 4, 5, 6, 7, 8, 9].
# The function iterates through the list. The first item is 1.
# 1 % 2 == 0 → False
# 1 % 2 != 0 → True
# So it returns "1 is odd"
# Because you use return, the function exits after returning for the first item.


# def function2(num):
#     if num % 2 == 0:
#         return f"{num} is even"
#     elif num % 2 != 0:
#         return f"{num} is odd"
#     else:
#         return "not a number"
#
# var =function2
# input=input("Enter a number: ")
# print(var(int(input)))

ara_1 = [1, 2, 3, 4, 5, 6]
target = 7
try:
    response2 = newfuntion().twosum(ara_1, target)
    print(response2)
except Exception as e:
    print(f"{e}")

my_list = [1, 2, 3, 4, 5]
var =all(my_list)
print(var)  # True if all elements are truthy, otherwise False

my_list1 = [1, 2, 3, 4, 0]
var1 = all(my_list1)
print(var1)  # False because 0 is falsy


my_list2 = [1, 2, 3, 4, 5]
def check_all_elements(lst):
    return all(lst)
result = check_all_elements(my_list2)
print(result)  # True if all elements are truthy, otherwise False

my_list3 = [1, 2, 3, 4, 0]
def check_all_elements(lst):
    return all(lst)
result1 = check_all_elements(my_list3)
print(result1)  # False because 0 is falsy

my_list4 = [2,4,6,8,10]
def check_all_elements(lst):
    return all(x % 2 == 0 for x in lst)
result2 = check_all_elements(my_list4)
print(result2)  # True because all elements are even


filled = ['john', 'john@email.com', 1234]
print(all(filled))  # True

condition1 = True
condition2 = True
print(all([condition1, condition2]))  # true

numbers=[1, 2, 3, 4, 5]
if any(num % 2 == 0 for num in numbers):
      print("At least one element is truthy")  # This will print because all numbers are truthy
else:
        print("No elements are truthy")

results = [True, True, False]
if not all(results):
    print("Some operations failed")
if any(not r for r in results):
    print("At least one operation failed")

# Using any() to check if any element in a list is greater than 10
numbers = [1, 2, 3, 4, 5, 11]
if any(num > 10 for num in numbers):
    print("At least one number is greater than 10")
# Using any() to check if any element in a list is a string


x=10
y=2
numbers= [1, 2, 3, 4, 5, 6, 7, 8, 9]
names= ["sajilan", "saji", "saj"]

if x > y and x==10:
    length=len(numbers)
    for i in range(length):
        if numbers[i] % 2 ==0:
            print(f"{numbers[i]} is even")
        else:
            print(f"{numbers[i]} is odd")
elif y>x and y==20:
    for name in names:
        if name == "sajilan":
            print(f"Hello {name}, you are a great person!")
        else:
            print(f"Hello {name}, keep up the good work!")
else:
    print("No conditions met, please check your inputs.")
