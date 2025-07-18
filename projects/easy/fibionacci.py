num = int(input("Please enter a number: "))
a=0
b=1
c=0
for i in range(num):
    c=a+b
    a=b
    b=c
print("The answer is ",a)