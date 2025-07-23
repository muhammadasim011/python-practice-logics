n = int(input("Enter a number: "))

factorial = 1
for k in range(1, n+1):
    factorial = factorial * k
print(f"The factorial of {n} is: {factorial}")