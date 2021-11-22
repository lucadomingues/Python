n1 = float(input('First segment: '))
n2 = float(input('Second segment: '))
n3 = float(input('Third segment: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('The segments above CAN FORM a triangle!')
else:
    print('The segments above CANNOT FORM a triangle!')