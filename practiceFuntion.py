def age_category(my_age, friend_age):
    def categorize(age):
        if age < 3:
            return f"Age {age} is a toddler"
        elif age < 13:
            return f"Age {age} is a child"
        elif age < 20:
            return f"Age {age} is a teenager"
        else:
            return f"Age {age} is an adult"

    print("You:", categorize(my_age))
    print("Your friend:", categorize(friend_age))


age_category(5, 16)


def calculatenumber(num1,num2):
    def cal(number):
        if number * 10 ==100 :
            return f" this number is {number} is coorect"
        elif number * 10 ==200:
            return  f" {number} this number is h=the coorct answer"
        else:
            return "unexpecterd outcome"

    # print("this is ",cal(num1))
    # print("this is a ",cal(num2))
    var1=cal(num1)
    var2=cal(num2)
    print(var1,var2)


calculatenumber(10,25)







