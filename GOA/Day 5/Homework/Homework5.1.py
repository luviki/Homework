#მომხმარებელს კითხეთ თავისი და მამამისის ასაკი, დაუპრინტეთ ყოველ წელს რამდენჯერ უფროსი იქნება მამამისი მასზე.

name = input("Please enter your name: ")
fathers_name = input("Please enter name of your father: ")
age = int(input("Please enter your age: "))
fathers_age = int(input("Please enter age of your father: "))

for i in range(30):
    print(name + " when you will be " + str(age + i) + " " + fathers_name + " will be " + str(fathers_age + i))