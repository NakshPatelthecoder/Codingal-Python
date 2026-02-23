base = float(input(" Enter the base: "))
exponent = int(input(" Enter the exponent (must be an integer or whole number): "))

result = 1

for _ in range(exponent):
    result *= base


print(f" {base} raised to the power of {exponent} is:{result}")
