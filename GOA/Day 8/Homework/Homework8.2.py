#ბილეთი ღირს 25 ლარი, მაგრამ ბავშვებისთვის უფასოა,გვყავს 13 ადამიანი, აქედან 10 დიდი და 3 ბავშვი, გამოთვალეთ ჯამში რამდენი ლარი დასჭირდებათ

age = int(input("Enter your age"))
if age <= 18:
    print("ბავშვო, შენთვის შესვლა უფასოა")
elif age >= 18:
    print("შენთვის შესვლა ფასიანია, 25 ლარი გადაიხადე")

ticket_price = 25
number_of_adults = 10
number_of_children = 3

print(str(ticket_price * number_of_adults) + "GEL")

