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