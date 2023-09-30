name = "Luka"
#name არის ცვლადი
# = არის ცვლადისთვის მნიშვნელობის მიმნიჭებელი სიმბოლო
# "Luka" არის ცვლადისთვის მნიშვნელობა
surname = "Vishtekaliuki"
age = "22"
# print(name)
# print ფუნქციას გადაეცემა ეკრანზე გამოსატანი ობიექტი

name = "Luka" #ეს არის str (string) ტიპის ცვლადი
age = 22 #ეს არის int (integer) მთელი რიცხვი
height = 173.5 #ეს არის float ტიპის ცვლადი (ათწილადი)
#boolean (bool) ტიპის ვცლადი

knows_programming = True #გამოვიყენოთ capslock პირველი ასოსთვის True ან False
is_skinny = False #snakecase (სტანდარტული წერის სტილი)

isSkinny = False #cameLcase (ჯავასკრიპტის სტანდარტული წერის სტილი)

print(name + " " + surname) #Space იწერება ცვლადებს შორის (( + " " + ))

#print(name + age) #name-str და age-int 
#სტრიგნი - ბრჭყალებში მოქცეული სიმბოლოები

#print(type(age))
#print(type(name))
#print(type(surname))
#print(type(height))
#print(type(knows_programming))

print("I am" + " " + name + " " + surname + " " + str(age) + " " + "years old and my height is" + " " + str(height) + " " + "some people might say that I am skinny but it is" + " " + str(is_skinny))
