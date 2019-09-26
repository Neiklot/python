num=int(input("Enter your number: "))
steps=0

while num!=1:
    steps+=1
    if num%2==0:
        #even
        num=num//2
    else:
        #odd
        num=3*num+1
    print(num)
else:
    print("steps",str(steps),sep=" = ")
    