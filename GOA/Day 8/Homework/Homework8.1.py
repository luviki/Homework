#შექმენით სია, ამ სიაში ჩაწერეთ სხვადასხვა ციფრები (1, 2, 3, 4, ასე არა, რამე მაგ: 45, 23, 87, 55,) 
#და გამოიტანეთ ამ სიაში ყველა რიცხვის ჯამი, ასევე ამავე სიიდან უნდა დაპრინტოთ ყველა რიცხვი ცალ ცალკე, და მიუწეროთ ლუწია თუ კენტი.

#ეს შეჯამება
my_list = [15, 27, 8, 116, 2, 61, 33, 84]
sum_result = 0
for number in my_list:
    sum_result += number
print("ლისტში მოცემული რიცხვების ჯამია", sum_result)

#ეს ლუწია თუ კენტი
my_list = [15, 27, 8, 116, 2, 61, 33, 84]
for number in my_list:
    if number % 2 == 0:
        print(f"{number} even")
    else:
        print(f"{number} odd")