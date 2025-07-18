num = int(input("Enter a number please: "))
temp = num
i=0
while num>0:
    num//=10
    i+=1
print(temp,"has ",i,"digits")