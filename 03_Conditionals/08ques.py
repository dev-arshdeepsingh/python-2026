password = input("Enter Password: ")

if len(password) < 6:
    strength = 'Weak'
elif len(password)<= 10:
    strength = "Medium"
else:
    strength = "Strong"

print("Password Entered is: ", strength)

#For optimisation, use pass_length = len(password) at line no.2 to avoid calculating len of password again and again in if-else