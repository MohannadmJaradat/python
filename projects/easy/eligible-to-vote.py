age = int(input("Please enter your age: "))
while age != -1:
    if age >= 18:
        print("Eligible to vote.")
    else:
        print("Not eligible to vote.")
    age = int(input("Please enter your age: "))
