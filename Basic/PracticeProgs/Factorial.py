print("*Factorial Calculator*")

n = int(input("Enter a number to calculate its factorial: "))
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("The factorial of", n, "is", fact)
