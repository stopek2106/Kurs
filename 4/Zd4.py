# ZADANIA Z LIST
# 2▹ Pobierz od użytkownika 10 liczb, wyświetl tylko te, które są nieparzyste.

# lista=[10,1,2,4,5,1,5,1]
# lista=[i for i in lista if i % 2 == 0 ]
# print(lista)

# generowanie listy

# lista=[i for i in range(10)]
# print(lista)

# 3▹ Dla podanej przez użytkownika liście
# liczb całkowitych sprawdź czy pierwszy i ostatni element są takie same.

# lista=[1,4,1,2,2]
# a=lista[0]
# l_elem=len(lista) # !!!!!!!!!!WAZNE
# b=lista[l_elem-1]
#
# if a==b:
#     print("ok")
# else:
#     print("nie są równe")

# KROTKI

#2▹ Stwórz krotkę. Znajdź powtarzające się elementy krotki. Wyświetl je

# tup=(1,4,2,1,5,5,1,2)
# tmp_list=list(tup)
# new_lista=[i for i in tmp_list if tmp_list.count(i) > 1]
# print(new_lista)

# tup=(1,4,2,1,5,5,1,2)
# tmp_list=list(tup)
# new_lista=[i for i in tmp_list if tmp_list.count(i) > 1]
# print(new_lista)


# tup=(1,4,2,1,5,5,1,2)
# tmp_list=list(tup)
# num=0
# for i in tmp_list:
#     if i/2 >2:
#         print("ok")
#         break
#     num +=1
#     print(num)


# SLOWNIKI

# 6▹ Utwórz listę zawierającą wartości poniższego słownika, bez duplikatów.

days = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sept': 30}
lista1=list(days.values())
set1=set(lista1)
# lista2=[i for i in lista1 if lista1.count(i)  =1]
lista2=list(set1)
print(lista2)
