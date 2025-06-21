import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = []

for letter in range(nr_letters):
    password.append(random.choice(letters))

for letter in range(nr_symbols):
    password.append(random.choice(symbols))

for letter in range(nr_numbers):
    password.append(random.choice(numbers))

print(password)
for i in range(len(password)):
    temporary = password[i]
    random_item_number = random.randint(0, len(password) - 1)
    password[i] = password[random_item_number]
    password[random_item_number] = temporary
    
    # Can use the random.shuffle(password) as well.
print(password)
password_name = ''

for letters in password:
    password_name += letters

print(f"Here is your password: {password_name}")


