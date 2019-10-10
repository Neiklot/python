sentence=input("Enter your word")

sentence=sentence.lower()
sentence=sentence.replace(" ","")
c=0
for i in range(len(sentence)-1,0,-1):
    if sentence[c]!=sentence[i]:
        print("It's not a palindroEleven animals I slam in a netme")
        break
    c+=1
else:
    print("It's  a palindrome")