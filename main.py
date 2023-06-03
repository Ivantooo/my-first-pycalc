math_exp = input('Введите математическое выражение: ')
new_math_exp = math_exp.split()
calculating = ''
math_sign = ''
result = 0
for elem in new_math_exp:
    if(elem.isalnum()):
        calculating += elem + ' '
    elif(elem == '+' or elem == '-' or elem == '*' or elem == '/'):
        math_sign += elem
if(math_sign == '+'):
    result = int(calculating[0]) + int(calculating[2])
elif(math_sign == '-'):
    result = int(calculating[0]) - int(calculating[2])
elif(math_sign == '*'):
    result = int(calculating[0]) * int(calculating[2])   
elif(math_sign == '/'):
    result = int(calculating[0]) / int(calculating[2])
print(result)

