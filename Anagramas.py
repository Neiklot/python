word=input("Enter the first word:")
second_word=input("Enter the second word:")
word=word.replace(" ","")
second_word=second_word.replace(" ","")

if len(word)<=0 or not word.isalpha():
    print("Not Anagrama")
else:
    for c in word.upper():
        if c not in second_word.upper():
            print("Not Anagrama")
            break
    else:
       print("Anagrama")