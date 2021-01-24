'''
if CONDITION:
    PROCESS A
else:
    PROCESS B

'''
print("if basics")
student = ['Tanaka', 'Suzuki', 'Nakata']
searchStudent = 'Suzuki'
print(student)
print("if " + searchStudent + " in student:")
if searchStudent in student:
    print('there is Tanaka in variable student')
    if 'Nakata' in student:
        print('Nakata is also in the variable student')
    else:
        print('Nakata is not in the variable student')
else:
    print(searchStudent+ ' is not in the variable student')
print("******")


'''
function A and function B:  assert both functions are true
function A or function B:  assert either functions are true
not function A:  assert the function are false

variable with list--- if it is blank variable, it will assert as false
ex) 
    numA = []
    if numA:
        print("hi")
    else:
        print("numA is false")
'''
print("if basics: multiple assertion")
num1 = [1,2,3,4]
if 1 in num1 and 5 in num1:
    print("if 1 in num1 and 5 in num1:")
    print("there is 1 and 5")
elif 6 in num1 or 100 in num1:
    print('6 or 100 is in the num')
elif not 5 in num1:
    print('5 is not in the num')
else:
    print('unique num')
print("******")

numA = []
print(numA)
print('if numA:')
if numA:
    print("hi")
else:
    print("numA is false")
print("******")

'''
for variableA in setOfData:
    Process A
'''

print("for basics")
professorNames = ['Jeff', 'Adam', 'Miles']
i = 1
for professor in professorNames:
    message = '{0} is {1}'.format(i, professor)
    print(message)
    i += 1
print("******")

'''
for i in range(NUMBER)--- repeat NUMBER
for i in range(NUMBER, NUMBER 2, NUMBER 3)--- repeat from NUMBER to NUMBER2 with NUBMER3 skips
'''

print("for basics: range")
print('for i2 in range(1,10,2)')
for i2 in range(1,10,2):
    print(i2)
else:
    print('failed to proceed')
print('completed')
print("******")

'''
Quick intro'''
print("for basics: tips")
foods = ['Salad','hamburger','rice with baked salted salmon','pizza','many more!']
for index, food in enumerate(foods):
    message='{0} th food is {1}'.format(index,food)
    print(message)
print('**********')
drinks = ['japanese tea', 'ginger ale', 'Japanese tea', 'coffee', ]

for food, drink in zip(foods,drinks):
    print(food,drink)

print("******")