weather = str(input("Enter weather: "))

if weather == "sunny" or weather == "SUNNY" or weather == "Sunny":
    print("Go for a walk")
elif weather in ["Rainy", "RAINY", "rainy"]:
    print("Read a book")
elif weather.lower() == "snowy":
    print("Build a snowman")
else:
    print("Eat 5-Star Do Nothing!")
 
#.lower() is a proffecional way