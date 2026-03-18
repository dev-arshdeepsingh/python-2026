age = int(input("Enter age: "))
day = "Thurs"

'''
if age>=18 and day != "wednesday":
    print("Price is $12")
elif age>=18 and day=="wednesday":
    print('price is $10')
elif age<18 and day!="wednesday":
    print('Price is $8')
else:
    print("Price is $6")

'''

price = 12 if age >=18 else 8 #A way to store 2 values in a var

if day == "wednesday":
    price = price - 2   #or price -= 2

print("Ticket price for you is $",price)