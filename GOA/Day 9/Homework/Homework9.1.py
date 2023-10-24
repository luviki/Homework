sentence = input("Please enter a sentence here: ")
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
consonant_count = 0
for char in sentence:
    if char in consonants:
        consonant_count += 1
print("In this sentence are", " " , consonant_count, " " , "consonants")