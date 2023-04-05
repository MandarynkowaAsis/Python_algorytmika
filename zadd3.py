a = int(input('Podaj wysokość: '))
b = int(input('Podaj szerokość: '))

for i in range(a):
    for j in range(b):
        print("* ", end=" ")
    if i == int(a/2):
        print('a', end=" ")
    print()
print('  ' * int(b/2),'b')