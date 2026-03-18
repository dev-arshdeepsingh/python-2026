pet = str(input("Enter your pet species: ")).lower().strip()
age = int(input('Enter age: '))

if pet == "dog":
    if age<=2:
        print("Give Puppy Food!")
    else:
        print("Give Dog Food!")
elif pet == "cat":
    if age <= 5:
        print("Give kitten food!")
    else:
        print("Give senior Cat Food!")
else:
    print("pet not found!")

