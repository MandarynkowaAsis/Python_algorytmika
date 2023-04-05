str1 = str(input("Podaj tekst: "))
str2 = "aut"

a = (str1.find(str2))
if a != -1:
    print('W podanym tekście znajduje się słowo aut.')
else:
    print('W podanym tekście nie znajduje się słowo aut')