a, b = int(input("Podaj pierwszą liczbe: ")), int(input("Podaj drugą liczbe: "))
temp = a * b
while a != b :
  if   a > b : a = a - b  # a -= b
  if   b > a : b = b - a  # b -= a
print("NWD tych liczb to:", a)
NWD = a
NWW = temp // a
print(f"NWD = {a}, NWW = {temp // a}")


# a * b = NWD(a,b) * NWW(a,b) <-- wzór
# NWW(a,b) = a * b / NWD(a,b)