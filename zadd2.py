import math

x1 = int(input('Podaj współrzędna x pierwszego punktu: '))
y1 = int(input('Podaj współrzędna y pierwszego punktu: '))
x2 = int(input('Podaj współrzędna x drugiego punktu: '))
y2 = int(input('Podaj współrzędna y drugiego punktu: '))

d = math.sqrt((math.pow((x2-x1), 2))+(math.pow((y2-y1), 2)))
print(d)