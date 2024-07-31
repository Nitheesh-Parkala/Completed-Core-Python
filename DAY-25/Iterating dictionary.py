student={
    "name": "rama",
    "age": 23,
    "branch": "cs",
    "mob": 988
}

print(student)

print(type(student))

student["IA_marks"]=90

student["College"]="VTU"

print(student)

for key in student:
    print(key)

for key in student:
    print(student[key])

for value in student.values():
    print(value)

for key,value in student.items():
    print(key,"",value)