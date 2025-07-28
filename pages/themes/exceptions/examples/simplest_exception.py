def get_user_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 1:
                raise ValueError("Age must be between 1 and 99")
            return age
        except ValueError:
            print("Please enter a valid age.")


user_age = get_user_age()

# Continue with the program using the valid age
print(f"You are {user_age} years old.")