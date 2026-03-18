order_size = input("Enter size of cofee small/medium/large: ").lower().strip()
extras = input("Do you want extra shot of Espresso: Yes/No: ").lower().strip()
extra_shot = True if extras == 'yes' else False
#extra_shot is just faltu variable it would have workde directly with yes and no

if extra_shot:
    coffee = order_size + " Coffee with extra shot"
else:
    coffee = order_size + " coffee"

print("Order: ", coffee)