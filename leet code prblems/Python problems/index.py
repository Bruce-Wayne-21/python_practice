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