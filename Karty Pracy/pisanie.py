print("Zadanie 8")
a = float(input("Wartość pocz: "))
b = float(input("Lata inwesty: "))
kon = 0
suma = a
for i in range(0, int(b * 12)):
  kon = suma * 0.06 * (1/12)
  suma += kon
print(round(suma,2))

# TRZEBA BYŁO DAĆ FLOATA A NIE INTA