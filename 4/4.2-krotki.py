# pet = ('pies', 'nova scotia', 'Fala')
# # teraz przypisanie zmiennych do elementów tuple
# (animal, breed, first_name) = pet
# print(f'Mój {pet[0]}, rasy {pet[1]} ma na imię {pet[2]}.')
# print(f'Mój {animal}, rasy {breed} ma na imię {first_name}.')

# Zestawy - krotka do seta

# krotka=(1,4,5,1,3,5,1,2,5,1,4)
# tmp_list=list(krotka)
# set_1=set(tmp_list)
# print(set_1)

# tuple1=tuple(range(10))
# tuple2=('a','b','c','d')
# tmp_list=list(tuple1[::2]+tuple2[1::2])
# print(tmp_list)
# # przekształcenie w set
# tmp_set=set(tmp_list)
# print(tmp_set)

# Słowniki !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#1
# lists_to_dict = [(1, 'jeden'),(2,'dwa')]
# dict_from_list = dict(lists_to_dict)
# print(dict_from_list)
# for i in dict_from_list.items():
#   print(i)

# lista=[
#     ['jablko','apple'],
#     ['grusza','pear'],
#     ['melon', 'melon']
# ]
# dict_from_list = dict(lista)
# #print(dict_from_list)
#Zadanie 3

# lista=[
#     ['* ','* ','* '],
#     ['* ','* ','* '],
# ]
#
# for row in lista:
#     for elem in row:
#         print(elem, end='  ')
#     print()
#Zadanie 5
txt = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""


txt = txt.replace(',', '')
txt = txt.lower()
words = txt.split()
# print(words)

counting_dict = {}

for word in words:
  if word in counting_dict:
    counting_dict[word] += 1
  else: #jeszcze słowa nie ma w słowniku
    counting_dict[word] = 1 # dodaj klucz do słownika po raz pierwszy - wartość 1

# print(counting_dict)

for k, v in counting_dict.items():
  print(k, '---->', v)

