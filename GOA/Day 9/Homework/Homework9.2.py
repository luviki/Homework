first_full_name = input("Please enter the fisrt fullname: ")
second_full_name = input("Please enter the second fullname: ")
first_a_count = first_full_name.lower().count('a')
second_a_count = second_full_name.lower().count('a')
if first_a_count > second_a_count:
    print("The fullname with the most 'Aa' characters is:", first_full_name)
    print("Count of 'Aa' characters in the first fullname:", first_a_count)
elif second_a_count > first_a_count:
    print("The fullname with the most 'Aa' characters is:", second_full_name)
    print("Count of 'Aa' characters in the second fullname:", second_a_count)