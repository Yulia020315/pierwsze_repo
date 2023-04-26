# def silnia (liczba):
#     if liczba== 0:
#         return 1
#     else:
#         return liczba*silnia(liczba-1)
# wynik=silnia(5)
# print(wynik)



# def sumowanie (listaLiczb):
#     if len(listaLiczb) > 0:
#         return listaLiczb[0]+sumowanie(listaLiczb[1:])
#     else:
#         return 0
# lista=[1 ,2 ,3 ,4 ,5]
# wynik=sumowanie(lista)
# print(wynik)
repo_editing


## zadan1e
# def dlugosc(x):
#     if x==[]:
#         return 0
#     else:
#         return 1+dlugosc(x[1:])
# lista=[1,2,3,4,5,6]
# print("Lista: ",lista)
# print("Długość listy to ",dlugosc(lista))

## za2anie
# def ostatni(x):
#     if x==[]:
#         return 0
#     elif len(x)==1:
#         return x[0]
#     else:
#         return ostatni(x[1:])
# lista=[1,2,3,4,5,6]
# print("Lista wygląda tak: ",lista)
# print("Ostatni element listy to: ",ostatni(lista))

# def ostatni(lista):
#     if len(lista)>0:
#         if len(lista)==1:
#             return lista[0]
#         else:
#             print(lista)
#             return ostatni(lista[1:])

## zadani3
# def znajduje_sie_na_liscie(lista,elem):
#     if len(lista)==[]:
#         return False
#     elif lista[0]==elem:
#         return True
#     else:
#         return znajduje_sie_na_liscie,(lista[1],elem)
# lista1=[1,2,3,4,5,6]
# print("Lista wygląda ta: ",lista1)
# wynik=znajduje_sie_na_liscie(lista1,7)
# print=(znajduje_sie_na_liscie(lista1,7))

# def czy_na_liscie(lista,liczba):
#     if len(lista)==0:
#         return False
#     elif lista[0]==liczba:
#         #print (lista)
#         return True
#     else:
#         #print(lista)
#         return czy_na_liscie(lista[1:],liczba)
# lista3=[98,97,96,95]






# def dzialanie(liczba1,liczba2):
#     suma=liczba1+liczba2
#     kwadrat=suma**2
#     wynik=kwadrat-1
#     return suma, kwadrat, wynik

# licz1=float(input("Podaj liczbę 1\n"))
# licz2=int(input("Podaj liczbę 2\n"))
# #print(type(licz1))
# #suma, kwadrat, wynik=dzialanie(licz1, licz2)
# dodawanie, potega, rezultat=dzialanie(licz1, licz2)
# print("Wynikiem dodawnia", dodawanie, "potęgi", potega,"a wynikiem całego działania", rezultat)




# licz=7
# def dzialanie():
#     licz=8
#     return licz
# licz=dzialanie()
# print(licz)

# licz2=8
# def glob():
#     #global licz2
#     licz2=10
# glob()
# print(licz2)

# def rysujProstokat (dl=3, sz=4, symbol='&'):
#     for i in range(dl):
#         for j in range(sz):
#             print(symbol, end='')
#         print()
# rysujProstokat(7)



# def silnia(liczba):
#     if liczba==0:
#         return 1
#     else: 
#         print(liczba)
#         return liczba * silnia(liczba-1)
    
# wynik=silnia(4)
# print(wynik)


# def suma(lista):
#     if len(lista)>0:
#         print(lista)
#         return lista[0]+suma(lista[1:]) ### zaczynamy od lista[0], bo to pierwsza "warstwa" matrioszki, którą musimy zdjąć, inaczej nie dostaniemy się do pozostałych
#     else:
#         print(lista)
#         return 0

# listaNew=[1, 2, 3, 4, 5]
# wynik=suma(listaNew)
# print(wynik)

## zadanie1
# def dlugosc(lista):
#     if lista==[]:
#     #if len(lista) == 0:
#         return 0
#     else:
#         print(lista)
#         return 1 + dlugosc(lista[1:])

# lista2=[12, 13, 14, 15]
# wynik=dlugosc(lista2)
# print(wynik)

### zadanie2
# def ostatni(lista):
#     if len(lista)>0:
#         if len(lista) == 1:
#             return lista[0]
#         else:
#             print(lista)
#             return ostatni(lista[1:])
    
# lista2=[12, 13, 14, 15]
# wynik=ostatni(lista2)
# print(wynik)

### zadanie3
# def czy_na_liscie(lista, liczba):
#     if len(lista) == 0:
#         return False
#     elif lista[0] == liczba:
#         print(lista)
#         return True
#     else:
#         print(lista)
#         return czy_na_liscie(lista[1:], liczba)

# lista3=[98, 97, 96 ,95]
# element=int(input("Jakiej liczby szukasz?\n"))
# wynik=czy_na_liscie(lista3, element)
# print(wynik)

### zadanie 4
# def nta(lista, n):
#     if n == 0:
#         return lista[0]
#     else:
#         #print(n)
#         #print(n)
#         return nta(lista[1:], n-1)
# lista3=[98, 97, 96 ,95]
# element=int(input("Element o jakim indeksie zwrócić?\n"))
# wynik=nta(lista3, element)
# print(wynik)

### zadanie 5
# def potega(liczba, wykladnik):
#     if wykladnik == 1:
#         return liczba
#     else:
#         #print(wykladnik)
#         return liczba * potega(liczba, wykladnik-1)

# liczba=int(input("Podaj liczbę\n"))
# wykladnik=int(input("Do której potęgi chcesz ją podnieść?\n"))
# wynik=potega(liczba, wykladnik)
# print(wynik)

### zadanie 6

# def maksimum(lista):
#     if len(lista)==1:
#         return lista[0]
#     else:
#         if lista[0] > maksimum(lista[1:]): #<
#             return lista[0]
#         else:
#             return maksimum(lista[1:])

# lista4=[2, 4, 7, 1, 3]
# wynik=maksimum(lista4)
# print(wynik)

### zadanie 7

# def ogon(lista):
#     if len(lista) == 1:
#         return []
#     else:
#         #print(lista)
#         return [lista[1]] + ogon(lista[1:])  
# lista5=[23, 25, 27, 29, 28, 26, 24]
# wynik=ogon(lista5)
# print(wynik)



### ZADANIE 1
# def sumowanie_ujemnych(lista):
#     if len(lista)>0:
#         if lista[0]<0:
#             return lista[0]+sumowanie_ujemnych(lista[1:])
#         else:
#             return sumowanie_ujemnych(lista[1:])
#     else:
#         return 0

# lista1=[-1,-3,4,-5,6]
# wynik1=sumowanie_ujemnych(lista1)
# print(wynik1)

# lista2=[1,3,4,5,-5,-6]
# wynik2=sumowanie_ujemnych(lista2)
# print(wynik2)

# lista3=[-8,-6,-4,2,4,-1,6]
# wynik3=sumowanie_ujemnych(lista3)
# print(wynik3)



### ZADANIE 2
# def porownaj_tekst(wyraz1,wyraz2):
#     if len(wyraz1)>0 and len(wyraz2)>0:
#         if wyraz1[0]!=wyraz2[0]:
#             return wyraz1[0],wyraz2[0],porownaj_tekst(wyraz1[1:],wyraz2[1:])
#         else:
#             return porownaj_tekst(wyraz1[1:],wyraz2[1:])
#     else:
#         return 0

# wyraz1=["K","o","n","s","t","a","n","t","y","n","o","p","o","l"]
# wyraz2=["K","o","n","n","t","a","n","f","y","n","o","l","o","l"]
# porownanie=porownaj_tekst(wyraz1,wyraz2)
# print(porownanie)

print(siemaneczko)
