
mixed_list = ["melon", "apple", "banana","durian","mango"]
choice = input("sort or reverse :")

if choice == 'sort':
    mixed_list.sort(key=str)
    print("Alphabetically:", mixed_list)
elif choice == 'reverse':
    mixed_list.reverse
    print("Reversed:", mixed_list)
else:
    print("sort or reverse")
