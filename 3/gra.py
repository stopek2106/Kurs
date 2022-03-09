# 4▹ Napisz grę - kamień (k) / papier (p) / nożyce (n).
#
#         Użytkownik podaje jedną z 3 figur.
#
#         Komputer losuje jedną z 3 figur.
#
#         Sprawdź kto wygrał tę rundę.
#
#         Zmień kod tak, by użytkownik mógł podac liczbę rund.
#
#         Wygrana jest podawana jako suma wygranych rund komputer vs użytkownik.
#
#         Zmień tak, by gracz mógł zakończyć grę w dowolnej chwili przez np. hasło ‘koniec’


import random
delta = int(input("Wpisz liczbę rund"))
lista = ['ka', 'pa', 'no']
for i in range (0,delta):
        los=str(random.choice(lista))
        slowo = str(input("Wpisz slowo"))
        if slowo==los:
            print("Wygrałeś",los)
            break
        else:
            print("Przegrałeś",los)




