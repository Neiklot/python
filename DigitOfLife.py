date=input("Enter your birth date: ")

def calculateDigitOfLife(date):
    sum=0
    for n in str(date):
        sum += int(n)
    if len(str(sum))>1:
        sum=calculateDigitOfLife(sum)
    return sum

if date.isdigit():
    print(calculateDigitOfLife(date))


