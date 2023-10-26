import random
arr_of_members = [
"Giorgi Lobzhanidze", 
"Tinatin Zuzadze", 
"Aleksandre Tordia", 
"Beka Berashvili", 
"Beqa Giorgobiani",
"Davit Janashia",
"Gio Abuladze",
"Gio kacitadze",
"Goglichadze Nini",
"Guri Ko",
"Lucas Vishtekaliuki",
"Mirian Gelashvili",
"Rati Murgulia",
"Rezi Neparidze",
"Salome Miladze",
"Tekla Papava",
"Temuri Solomonishvili",
"Tsotne Sartania",
"Vano Motiashvili",
"Giorgi Chkhetiani",
"Davit Tchilashvili",
"Temo Labadze",
"Nino Solomonia"
]

arr_of_scores = ["5", "10"]

for i in range(len(arr_of_members)):
    student = random.choice(arr_of_members)


answer = input("Did the student answer the question correctly? ")
if answer == "yes":
    print("Good Job ", student, "you got yourself a sweet +10 points!!!")
elif answer == "no":
    print("BOOO HOOO", student, "you have just lost -5 points!")