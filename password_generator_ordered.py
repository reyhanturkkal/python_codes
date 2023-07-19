import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")

nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

len_of_password = nr_letters + nr_numbers + nr_symbols
password = []

for location_of_pass_char in range(0,len_of_password):

    if location_of_pass_char < nr_letters:
        rand_letter_index = random.randint(0, len(letters)-1)
        password.append(letters[rand_letter_index])
    elif location_of_pass_char >= nr_letters and location_of_pass_char <nr_letters + nr_symbols:
        rand_symbol_index = random.randint(0, len(symbols)-1)
        password.append(symbols[rand_symbol_index])
    elif location_of_pass_char >= nr_letters + nr_symbols:
        rand_number_index = random.randint(0, len(numbers)-1)
        password.append(numbers[rand_number_index])

final_password = ''.join(str(x) for x in password)
print(f"Here is your password: {final_password}")
