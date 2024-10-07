numbers = [20,19,18,17,16,3,2,1]

username = input("do you want to delete your array ? :")

if username == "yes":
    numbers.clear()
elif username == "no":
    userdata = input("add new data : ")
    numbers.append(userdata)

print(numbers)