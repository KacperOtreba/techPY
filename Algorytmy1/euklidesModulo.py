a, b = int(input()), int(input())
while b > 0 :
    # print(f"{a} \t\t {b} \t\t{a%b}")
    a, b = b, a % b
print(a)