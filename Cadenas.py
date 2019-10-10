def mysplit(strng):
    if strng=='' or strng.isspace():
        return []
    stringsSpliteds=[]
    stringSplited=""
    for c in strng:
       if c == chr(32):
           if stringsSpliteds!=chr(32) and len(stringSplited)>1:
            stringsSpliteds.append(stringSplited)
            stringSplited=""
       else:
           stringSplited+=c
    return stringsSpliteds

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))