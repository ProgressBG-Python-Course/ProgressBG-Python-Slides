# Map letters to its uppercase
letters = ['a', 'b', 'c']
upper_letters = [l.upper() for l in letters]
print(upper_letters) # ['A', 'B', 'C']

# Converting temperatures from Celsius to Fahrenheit
celsius = [0, 20, 37, 100]
fahrenheit = [((temp * 9/5) + 32) for temp in celsius]
print(fahrenheit) # [32.0, 68.0, 98.6, 212.0]

# Filtering Even Numbers:
numbers = [1,2,3,4,5]
evens = [num for num in numbers if num % 2 == 0]
print(evens) # [2, 4]

# Filtering email addresses
emails = ["user1@gmail.com", "user2@yahoo.com", "user3@gmail.com"]
gmail_users = [email for email in emails if "@gmail.com" in email]
print(gmail_users) # ['user1@gmail.com', 'user3@gmail.com']

# Flattening a nested list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_list = [num for row in matrix for num in row]
print(flat_list) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
