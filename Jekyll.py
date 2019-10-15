class StudentsDataException(Exception):
    pass

class BadLine(StudentsDataException):
    def __init__(self):
        print("Bad line in the file")

class FileEmpty(StudentsDataException):
    def __init__(self):
        print("This file is empty!")

fileName = input("Enter the file name: ")

students={}
try:
    file = open("C:\\cryptographer\\" + fileName + ".txt", mode="r+t", encoding="UTF-8")
    lines=file.readlines()
    if len(lines) == 0:
        raise FileEmpty()
    for student in lines:
        if student == "":
            raise BadLine()
        studentData=student.split()
        studentName=studentData[0]+" "+studentData[1]
        if studentName not in students.keys():
            students[studentName]=float(studentData[2])
        else:
            students.update({studentName:students[studentName]+float(studentData[2])})
    file.close()
    for key,value in sorted(students.items(),key=lambda kv:kv[0]):
        print(key,value,sep=" ")
except Exception as e:
    print("Exception ",e)