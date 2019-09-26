blocks = int(input("Enter the number of blocks: "))
level=0

while blocks-level>0:
    level+=1
    blocks=blocks-level

print("The height of the pyramid:", level)