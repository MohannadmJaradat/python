num = int(input("Enter a number: "))
half=num//2
for i in range(1,half+1):
    if num%i==0:
        print (i)
else:
    print (num)