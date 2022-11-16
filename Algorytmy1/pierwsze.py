# 1.Algorytm sprawdzający czy liczba jest pierwsza
temp = 0
n = int(input())
for i in range(1,n+1):
  if n % i == 0:
    temp += 1
if temp == 2:
  print("Liczba jest pierwsza")
else:
  print("Liczba nie jest pierwsza")

# pan by tak chciał
from math import sqrt
n = int(input())
for i in range(2, int(sqrt(n)) + 1):
  if n % i == 0:
    print("Liczba nie jest pierwsza")
    exit(0)
print("Liczba jest pierwsza")