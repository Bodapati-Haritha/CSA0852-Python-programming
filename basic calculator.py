def pow(x, n):
    return x ** n

def add(x, n):
    return x + n

def sub(x, n):
    return x - n

def mul(x, n):
    return x * n

def div(x, n):
    return x / n

x = float(input("Enter a value for x: "))
n = float(input("Enter a value for n: "))

print("Choose an operation:")
print("1. Pow(x, n)")
print("2. Add(x, n)")
print("3. Sub(x, n)")
print("4. Mul(x, n)")
print("5. Div(x, n)")

choice = int(input("Enter your choice (1-5): "))

if choice == 1:
    result = pow(x, n)
    print("Result:", result)
elif choice == 2:
    result = add(x, n)
    print("Result:", result)
elif choice == 3:
    result = sub(x, n)
    print("Result:", result)
elif choice == 4:
    result = mul(x, n)
    print("Result:", result)
elif choice == 5:
    result = div(x, n)
    print("Result:", result)
else:
    print("Invalid choice")
