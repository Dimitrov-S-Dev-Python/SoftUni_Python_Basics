eggs_size = input()
eggs_color = input()
partition = int(input())
price = 0

if eggs_size == "Large":
    if eggs_color == "Red":
        price = 16
    elif eggs_color == "Green":
        price = 12
    elif eggs_color == "Yellow":
        price = 9
elif eggs_size == "Medium":
    if eggs_color == "Red":
        price = 13
    elif eggs_color == "Green":
        price = 9
    elif eggs_color == "Yellow":
        price = 7
elif eggs_size == "Small":
    if eggs_color == "Red":
        price = 9
    elif eggs_color == "Green":
        price = 8
    elif eggs_color == "Yellow":
        price = 5

total = price * partition * 0.65
print(f"{total:.2f} leva.")
