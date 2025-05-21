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

varible=[1,2,3,4,5]
for i in varible:
    print(i)

variable = [1, 2, 3, 4, 5]
print(*variable)

names=["saijilan","saj","saji"]
for i in names:
    print(i)

print(*names)





