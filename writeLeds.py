from Leds import getNumber as getNum

try:
    stringNum=input("Enter your number:")
    for i in range(5):
        line = ""
        for num in stringNum:
            num = int(num)
            for col in range(3):
                line+=getNum(num)[i][col]
                line+=chr(32)+chr(32)
        print(line)

except ValueError:
    print("Incorrect value")


