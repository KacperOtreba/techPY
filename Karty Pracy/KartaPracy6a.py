# print("Zadanie 1")
# n = int(input("Podaj liczbe: "))
# wynik = 0
# while n > 0:
#   wynik += n % 10
#   n = n // 10
# print("Suma cyfr tej liczby to: ", wynik)

# print("Zadanie 2")
# n = int(input())
# suma = 0
# for i in range(1, n+1):
#   if n % i == 0:
#     suma += 1
# if suma == 2:
#   print("TAK")
# else:
#   print("NIE")

# print("Zadanie 3")
# n = int(input("Podaj liczbe: "))
# suma = 0
# for i in range(1,n):
#   if n % i == 0:
#     suma += i
# if suma == n:
#   print("Liczba jest doskonała")
# else:
#   print("Liczba nie jest doskonała")

# print("Zadanie 4")
# a = int(input("Podaj 1 liczbe: "))
# b = int(input("Podaj 2 liczbe: "))
# temp = a * b
# while b > 0:
#   a, b = b, a % b
# nwd = a
# if nwd == 1:
#   print("Liczby są względnie pierwsze")
# else:
#   print("Liczby nie są względnie pierwsze")

# print("Zadanie 5")
# n = int(input())
# for i in range(10,20):
#   x = n
#   y = i
#   while y > 0:
#     x, y = y, x % y
#   nwd = x 
#   if x == 1:
#     print(n,i)

# print("Zadanie 6")
# a = int(input("Podaj licznik: "))
# b = int(input("Podaj mianownik: "))
# x = a
# y = b
# while y > 0:
#   x, y = y, x % y
# nwd = x

# print(a // nwd)
# print("---")
# print(b // nwd)