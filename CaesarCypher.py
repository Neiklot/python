string=input("Enter you word:")

if not string.isalnum():
    print("Error in characters:")

shift=input("Enter you shift:")

try:
    shift=int(shift)
except ValueError:
    print("Error in shift")

cipher=''
for char in string:
    if char.isalpha():
        code = ord(char)+shift
        if char.isupper():
            first=ord('A')
        else:
            first=ord('a')
        code-=first
        code%=26
        cipher+=chr(first+code)
    else:
        cipher+=char

print(cipher)
