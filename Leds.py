
zero=[[],[],[],[],[]]
zero[0]=['#','#','#']
zero[1]=['#',chr(32),'#']
zero[2]=['#',chr(32),'#']
zero[3]=['#',chr(32),'#']
zero[4]=['#','#','#']
one=[[],[],[],[],[]]
one[0]=[chr(32),chr(32),'#']
one[1]=[chr(32),chr(32),'#']
one[2]=[chr(32),chr(32),'#']
one[3]=[chr(32),chr(32),'#']
one[4]=[chr(32),chr(32),'#']
two=[[],[],[],[],[]]
two[0]=['#','#','#']
two[1]=[chr(32),chr(32),'#']
two[2]=['#','#','#']
two[3]=['#',chr(32),chr(32)]
two[4]=['#','#','#']
three=[[],[],[],[],[]]
three[0]=['#','#','#']
three[1]=[chr(32),chr(32),'#']
three[2]=['#','#','#']
three[3]=[chr(32),chr(32),'#']
three[4]=['#','#','#']
four=[[],[],[],[],[]]
four[0]=['#',chr(32),'#']
four[1]=['#',chr(32),'#']
four[2]=['#','#','#']
four[3]=[chr(32),chr(32),'#']
four[4]=[chr(32),chr(32),'#']
five=[[],[],[],[],[]]
five[0]=['#','#','#']
five[1]=['#',chr(32),chr(32)]
five[2]=['#','#','#']
five[3]=[chr(32),chr(32),'#']
five[4]=['#','#','#']
six=[[],[],[],[],[]]
six[0]=['#','#','#']
six[1]=['#',chr(32),chr(32)]
six[2]=['#','#','#']
six[3]=['#',chr(32),'#']
six[4]=['#','#','#']
seven=[[],[],[],[],[]]
seven[0]=['#','#','#']
seven[1]=[chr(32),chr(32),'#']
seven[2]=[chr(32),chr(32),'#']
seven[3]=[chr(32),chr(32),'#']
seven[4]=[chr(32),chr(32),'#']
eight=[[],[],[],[],[]]
eight[0]=['#','#','#']
eight[1]=['#',chr(32),'#']
eight[2]=['#','#','#']
eight[3]=['#',chr(32),'#']
eight[4]=['#','#','#']
nine=[[],[],[],[],[]]
nine[0]=['#','#','#']
nine[1]=['#',chr(32),'#']
nine[2]=['#','#','#']
nine[3]=[chr(32),chr(32),'#']
nine[4]=['#','#','#']

def getNumber(num):
    if num==0:
        return zero
    if num==1:
        return one
    if num==2:
        return two
    if num==3:
        return three
    if num==4:
        return four
    if num==5:
        return five
    if num==6:
        return six
    if num==7:
        return seven
    if num==8:
        return eight
    if num==9:
        return nine
