class Person:
    def __init__(self, name):
        self.name = name


maria = Person("Maria")

age = getattr(maria, "age", "Not specified")
print(age)

# Output: Not specified
