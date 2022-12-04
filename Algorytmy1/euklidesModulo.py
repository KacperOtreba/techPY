a = int(input("Podaj pierwszą liczbe: "))
b = int(input("Podaj drugą liczbe: "))
while b > 0 :
    print(f"{a} \t\t {b} \t\t{a%b}")
    a, b = b, a % b  #<-- to musi być w jednej lini!
print("Największy wspólny dzielnik tych liczb to: ", a)
