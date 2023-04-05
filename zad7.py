str1 = str(input('Podaj tekst: '))
str2 = "uw"

a = str1.find(str2, len(str1)-2)
if a != -1:
    print('Chyba masz błąd ortograficzny.')