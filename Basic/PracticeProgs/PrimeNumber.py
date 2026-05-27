print("*Prime Number Checker*")

num = int(input("Enter a number to check if it is a prime number: "))

flag = True

if num <= 1:
    flag = False

else:

    for i in range(2, num):

        if num % i == 0:
            flag = False
            break

if flag:
    print("Prime Number")

else:
    print("Not Prime")