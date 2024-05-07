import random

# print("Welcome to the PyPassword Generator!")
print("How many letters would you like in your password?")
letter_choice = int(input())
print("How many symbols would you like in your password?")
symbols_choice = int(input())
print("How many numbers would you like in your password?")
numbers_choice = int(input())

let_output = ""
sym_output = ""
num_output = ""


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']




for let in range(0, letter_choice):
    let_output = str(let_output + letters[random.randint(0,numbers_choice)])

for sym in range(0, symbols_choice):
    sym_output = str(sym_output + symbols[random.randint(0,symbols_choice)])

for num in range(0, numbers_choice):
    num_output = str(num_output + numbers[random.randint(0,numbers_choice)])

print(let_output)
print(sym_output)
print(num_output)

pw = let_output + sym_output + num_output

print(pw)

password_list = []

for let in range(0, letter_choice):
    password_list += random.choice(letters)

for sym in range(0, symbols_choice):
    password_list += random.choice(symbols)

for num in range(0, numbers_choice):
    password_list += random.choice(numbers)

print(password_list)



print(password_list)

password = ""
for char in password_list:
    password += char

print(f"your password is {password}")
