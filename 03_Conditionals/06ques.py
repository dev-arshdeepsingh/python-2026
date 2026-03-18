distance = int(input("Enter distance in KMs: "))

if distance < 3:
    activity = "Walk"
elif distance >= 3 and distance <= 15:
    activity = "Use Bike"
else:
    activity = "Use Car"

print(activity)