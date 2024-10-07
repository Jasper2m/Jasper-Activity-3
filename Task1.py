user_numbers = []
user = int(input("Numbers that you want to add in hte append "))

for i in range(user):
    number = int(input(f"Enter number {i+1}: "))
    user_numbers.append(number)
print(user_numbers)
