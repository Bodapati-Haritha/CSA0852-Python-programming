def find_lcm(numbers):
    lcm = numbers[0]
    for i in range(1, len(numbers)):
        lcm = lcm * numbers[i] // find_gcd(lcm, numbers[i])
    return lcm

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(input("Enter the number of numbers: "))
numbers = []
for i in range(n):
    number = int(input("Enter a number: "))
    numbers.append(number)

lcm = find_lcm(numbers)
gcd = find_gcd(numbers[0], numbers[1])
for i in range(2, len(numbers)):
    gcd = find_gcd(gcd, numbers[i])

print("LCM of the numbers:", lcm)
print("GCD of the numbers:", gcd)
