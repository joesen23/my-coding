
numbers = [20,19,18,5,6,7,8]

username = input("do you want to delete your array ? :")

if username == "yes":
    numbers.clear()
elif username == "no":
    userdata = input("add new data : ")
    numbers.append(userdata)

print(numbers)