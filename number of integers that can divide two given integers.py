def find_divisors(a, b):
    divisors = []
    for i in range(1, min(a, b)+1):
        if a%i == 0 and b%i == 0:
            divisors.append(i)
    return divisors

a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

divisors = find_divisors(a, b)

print("The common divisors of", a, "and", b, "are:", divisors)
print("The number of common divisors is:", len(divisors))
