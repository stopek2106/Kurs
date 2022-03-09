"""
dish = "gzik"
if dish =="gzik":
    print("WLKP")
else:
    print("inny region")
"""
"""
reg= "d"
dish ="gzik"
if dish == "pyzy":
    reg = "WLKP"
print(reg)
"""
# Poproś użytkownika o podanie liczby. Sprawdź czy liczba podana przez użytkownika
# jest podzielna przez 3 bez reszty i wyświetl komunikat “Twoja liczba jest podzielna przez 3

"""
a = input('Wpisz liczbę')

a = int(a)
if a % 3 ==0:
    print("Liczba ok")
else:
    print("blad")
    
"""
# Stwórz skrypt, który przyjmuje 3 opinie użytkownika o książce. Oblicz średnią opinię o książce. W zależności od wyniku dodaj komunikaty. Jeśli uzytkownik ocenił książkę na ponad 7 -
# bardzo dobry, ocena 5-7 przeciętna, 4 i mniej - nie warta uwagi
"""
a = int(input("ocena1"))
b = int(input("ocena2"))
c = int(input("ocena3"))

rank = ((a+b+c)/3)
if rank >= 7 :
    print("b.dobry")
if rank >= 3 and \
   rank <= 6 :
    print ("dobry")
else:
    print("słaby")
"""
#Stwórz zmienną password. Hasło powinno składać z liter i cyfr,
# zwierać conajmniej 1 dużą literę i mieć długość conajmniej 8 znaków.
# Poinformuj użytkownika, jeśli wpisane hasło jest nie poprawne.
# Wyświetl różne komunikaty w zależności od rodzaju błędu.

haslo = input("Wpisz haslo: ")

if len(haslo) < 8:
     print("haslo musi miec min 8 znakow")
elif haslo.islower():
    print("Hasło musi zawierać conajmniej 1 duza literę")

elif haslo.isupper():
    print ("Hało musi zawierać co najmiej 1 małą literkę")
else:
    print("Halo prawidlowe")