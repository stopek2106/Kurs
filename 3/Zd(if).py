# #Pobierz dwie liczby całkowite od użytkownika i oblicz
# # ich sumę. Jeśli suma jest większa niż 100, wyświetl wynik,
# w przeciwnym wypadku wyświetl “Koniec”.

# a=int(input('Podaj liczbę 1 ='))
# b=int(input('Podaj liczbę 2 ='))
#
# suma = a + b
# if suma > 100:
#     print("Wyniki wynosi:", suma)
# else:
#     print("Koniec")

# Utwórz zmienną przechowującą dowolny ciąg znaków.
# Sprawdź czy utworzony string jest dłuższy niż 5 znaków oraz czy zawiera literę a.
# Jeśli zawiera, wszystkie litery a podmień na z i wyświetl powstały napis.

# zm = input('Wpisz dowolny wyraz: ')
# dl = len(zm)
# if dl > 5:
#     print('ok')
# else:
#     print('no')

# Zapytaj użytkownika o numer od 1 do 100,
# jeśli użytkownik zgadnie liczbę ukrytą przez programistę wyświetl komunikat
# “gratulacje!”, w przeciwnym razie wyświetl “pudło!”.

# a = int(input('Podaj liczbę od 1 do 100 ='))
# b = 99
# if a==b:
#     print('Gratulacje')
# else:
#     print('Guzki z tego')
#

# Sortowanie. Trzy dowolne liczby podane przez użytkownika zapisz do trzech zmiennych.
# Znajdź największą liczbę. Wyświetl liczby od największej do najmniejszej.

a = int(input("Podaj liczbę a = "))
b = int(input("Podaj liczbę b = "))
c = int(input("Podaj liczbę c = "))
x = [a,b,c]
if a > b and a > c:
    print('Największe liczba to', a)
elif b > a and b > c:
    print('Największa liczba to', b)
else:
    print('Największa liczba to', c)
xd=x.sort()

print('Posortowane',x)


