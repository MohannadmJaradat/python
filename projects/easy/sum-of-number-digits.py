num = int(input("Please enter a number: "))
temp = num
i=0
while num > 0:
    i+=num%10
    num//=10
print("The sum of the digits of ",temp,"is ",i)