# Zad.1▹ Skorzystaj ze swojego kodu bmi.py.
# Rozbij liczenie bmi na funkcję obliczającą bmi na podstawie danych użytkownika
# oraz zwracającą odpowiednią wartość (niedowaga, waga normalna, nadwaga, otyłość)
# w zależności od otrzymanego parametru.
#
# def bmi():
#     m = float(input("Wpisz mase: "))
#     w = float(input("Wpisz wzrost: "))
#     return m/(w**2)
# # --------------------------------
# if bmi() > 25:
#     print("Nadwaga")
#
# elif bmi() < 25 and bmi() >= 18:
#     print("Waga ok")
#
# else:
#     print("Niedowaga")

# Zadanie z choinką

# lst = list(range(1, 5))
#
# for i in lst:
#     for e in range(1,5):
#         print("*"*e)
# jako choinka

# Zad. 2. Nie korzystając z funkcji wbudowanej min(),
# napisz funkcję znajdującą minimalną wartość z 3 liczb. minimum_of(a, b, c).

# def min_of(x,y):
#     return x if x<y else y
#
# def minimum_of(a,b,c):
#     result = min_of(a,b)
#     min_value = min_of(result, c)
#     return min_value
#
# print(minimum_of(1,2,3))
# ZAD. 3▹Nie korzystając z funkcji wbudowanej max(),
# napisz funkcję znajdującą minimalną wartość z 3 liczb. minimum_of(a, b, c).

# def max_of(x,y):
#     # if x > y:
#     #     return x
#     # else:
#     #     return y
#     return x if x>y else y # argument trojwartosciowy
#
# def maximum_of(a,b,c):
#     result = max_of(a, b)
#     max_value = max_of(result, c)
#     return max_value
#
#
# # --- main
# print("Największa wartość to",  maximum_of(4, 3, 2) )

# lub z FOR

# def maximum_of(a,b,c):
#     pool = [a, b, c]
#     maximum = pool[0]
#
#     for value in pool:
#         if value > maximum:
#             maximum = value
#     return maximum
#
# # --- main ---
# print(maximum_of(23,1,4))



# ZAD 4▹ Napisz funkcję, która sprawdzi, czy liczba występuje w podanym przez użytkownika zakresie.
# Powinna zwrócić komunikat: “tak, liczba x znajduje się w zadanym zakresie”, “nie, liczba x jest z poza zakresu”.

# Zakres=[1,2,3,4,5,6,7]
#
# def check(x):
#     if x in list(Zakres):
#         return "tak, liczba x znajduje się w zadanym zakresie"
#     else:
#         return "nie, liczba x jest z poza zakresu"
# #***********************************
# Lb=int(input("Wpisz liczbę"))
#
# print(check(Lb))


# ZAD 5. 5▹ Napisz grę ciepło - zimno tak, aby korzystać z funkcji. - Do modyfikacji!!!!!!!!!!!!!!!!!!!!!!!



# def wynik_losowania():
#     import random
#     zakres = list(range(1,11))
#     return random.choice(zakres)
# def kryterium(a,b):
#     a = wynik_losowania()
#     b = Num
#     return (abs(a-b)/b)*100
#
# #***************************************
#
# for i in range(10):
#     Num = int(input("Podaj liczbe = "))
#     if kryterium(wynik_losowania(),Num)==0: #wynik w procentach
#         print("Bingo", wynik_losowania())
#         break
#     elif kryterium(wynik_losowania(),Num)<25:
#         print("ciepło", wynik_losowania())
#     else:
#         print("zimno", wynik_losowania())



#ZAD 6▹ Napisz grę kamień-papier-nożyce tak, aby korzystać z funkcji.


# def wynik_losowania():
#     import random
#     lista = ['ka', 'pa', 'na']
#     return random.choice(lista)
# # #$$$$$$$$$$$$$$$$$$$$$$$$$$$ main $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# l_rund=int(input("Wpisz liczbę rund = "))
# for i in range(l_rund):
#     word = str(input("Wpisz slowo: ka, pa lub no: "))
#     if wynik_losowania() == word:
#         print ("Wygrana:", "wynik losowania to = ", wynik_losowania())
#         break
#     else:
#         print ("Przegrana", wynik_losowania())








# 7▹ Napisz program, który na podstawie numeru karty odpowie czy ma doczynienia z Visą,
# MasterCard, a może AmericanExpress. Co wiemy o tych numerach tych kart?
#
#     All Visa card numbers start with a 4. New cards have 16 digits. Old cards have 13.
#
#     MasterCard numbers either start with the numbers 51 through 55 or with the numbers 2221 through 2720. All have 16 digits.
#
#     American Express card numbers start with 34 or 37 and have 15 digits.

# Karty kredytowe mogę miec dlugosci - 13, 15, 16
# Tylko numery
# card_lenghts = [13,15,16]
# card_number=input("Podaj nr karty")
# if not card_number.isdigit():
#     print('TO nie jest nr karty')
# if len(card_number) not in card_lenghts:
#     print('Długość nieprawidłowa')
# else:
#     print('To moze byc karta')

# def is_american_express(card_number):
#     card_length = len(card_number)
#     return card_length == 15 and (card_number[0:2] == '34' or card_number[0:2] == '37')
#
#
# def is_visa(card_number):
#     card_length = len(card_number)
#     return card_length in [13, 16] and card_number[0] == '4'
#
#
# def is_mastercard(card_number):
#     card_length = len(card_number)
#     starts_with_51_55 = 51 <= int(card_number[0:2]) <= 55
#     starts_with_2221_2720 = 2221 <= int(card_number[0:4]) <= 2720
#
#     return card_length == 16 and (starts_with_51_55 or starts_with_2221_2720)
#
# def get_card_number():
#     cards_lengths = [13, 15, 16]
#     while(True):
#         card_number = input('Podaj numer karty: ')
#         card_number = card_number.replace(' ', '')
#
#         if card_number.isdigit() and len(card_number) in cards_lengths:
#             break
#         else:
#             print('To nie jest nr karty, spróbuj jeszcze raz ')
#
#     return card_number
#
#
# #--- main code
#
# card_number = get_card_number()
# print('Numer karty użytkownika -->', card_number)
#
# if is_visa(card_number):
#     print("To jest visa")
# elif is_mastercard(card_number):
#     print("To jest master card")
# elif is_american_express(card_number):
#     print("To jest american express")
# else:
#     print("To może być inna karta")




