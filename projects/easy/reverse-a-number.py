num=int(input("Please enter a number: "))
temp=num
i=0
j=0
while num>0: # count digits of number
    num//=10
    i+=1
while temp>0:
    j+=(temp%10)*(10**(i-1))
    temp//=10
    i-=1
print (j)