import random
arr_of_symbols = ["!", "@", "#", "$", "%", "&", "*", "?"]
arr_of_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
arr_of_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
password = random.choice(arr_of_symbols) + random.choice(arr_of_numbers) + random.choice(arr_of_letters) + random.choice(arr_of_letters) + random.choice(arr_of_letters) + random.choice(arr_of_letters) + random.choice(arr_of_numbers) + random.choice(arr_of_symbols)
print("Your generated password is: " + password)