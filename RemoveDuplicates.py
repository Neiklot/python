myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
listWithoutDuplicates=[]

for i in myList:
    if i not in listWithoutDuplicates:
        listWithoutDuplicates.append(i)
myList=listWithoutDuplicates[:]
print("The list with unique elements only:")
print(myList)