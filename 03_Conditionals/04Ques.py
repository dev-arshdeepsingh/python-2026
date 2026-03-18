fruit = str(input("Enter Fruit name: "))
color = str(input("Enter Color of fruit: "))


# if fruit == "Banana" or "banana" or "BANANA":
#     if color == "Yellow" or "yellow" or "YELLOW":
#         print(fruit, "is Ripe")
#     elif color == "Green" or "green" or 'GREEN':
#         print(fruit, "is Unripe")
#     else:
#         print(fruit, "is Overripe")
# else:
#     print("Sorry, we don't have that fruit option yet")


'''Ah, the classic Python logic trap! Don't worry, almost every programmer hits this wall when 
they first start working with or statements.

The issue is how Python evaluates if fruit == "Banana" or "banana". You might expect
 it to check if fruit is one of those three things, but Python actually reads it as:

Is fruit == "Banana"?

OR is the string "banana" a "truthy" value? (In Python, any non-empty string is always considered True).

Because "banana" is always True, your first if statement will always trigger, regardless of what the user actually types.'''

#Correct way
if fruit == "Banana" or fruit =="banana" or fruit == "BANANA":
    if color == "Yellow" or color == "yellow" or color == "YELLOW":
        print(fruit, "is Ripe")
    elif color == "Green" or color == "green" or color == 'GREEN':
        print(fruit, "is Unripe")
    else:
        print(fruit, "is Overripe")
else:
    print("Sorry, we don't have that fruit option yet")
