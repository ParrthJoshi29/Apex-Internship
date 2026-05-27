print("*Armstrong Number Checker*")

# For eg: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

num = int(input("Enter a number to check if it is an Armstrong number: "))

temp = num
sum = 0

while temp > 0:

    digit = temp % 10
    sum = sum + digit ** 3
    temp = temp // 10

if sum == num:
    print("Armstrong Number")

else:
    print("Not Armstrong")