print("                                  *Calculator           *")

opt = "NULL"
print("                     Options: add, sub, mul, div, pow, mod\n")

def add():
    num1 = int(input("Enter first number to add: "))
    num2 = int(input("Enter second number to add: "))
    print("Sum: ", num1 + num2)
    
def sub():
    num1 = int(input("Enter first number to subtract: "))
    num2 = int(input("Enter second number to subtract: "))
    print("Subtraction: ", num1 - num2)

def mul():
    num1 = int(input("Enter first number to multiply: "))
    num2 = int(input("Enter second number to multiply: "))
    print("Multiplication: ", num1 * num2)

def div():
    num1 = int(input("Enter first number to divide: "))
    num2 = int(input("Enter second number to divide: "))
    if num2 != 0:
        print("Division: ", num1 / num2)
    else:
        print("Error: Division by zero is not allowed.")

def poww():
        base = int(input("Enter base number for power: "))
        exponent = int(input("Enter exponent: "))
        print("Power: ",pow(base,exponent))

def mod():
    num1 = int(input("Enter first number for modulus: "))
    num2 = int(input("Enter second number for modulus: "))
    if num2 != 0:
        print("Modulus: ", num1 % num2)
    else:
        print("Error: Modulus by zero is not allowed.")

while True:

    print("\nOptions: add, sub, mul, div, pow, mod")
    print("Type 'esc' to exit\n")

    opt = input("Enter operation: ").lower()
    print("You chose: ", opt)

    if opt == "esc":
        print("Calculator Closed")
        break

    match opt:
    
        case "add":
            add()
        
        case "sub":
            sub()
    
        case "mul":
            mul()       
    
        case "div":
            div()
    
        case "pow":
            poww()
    
        case "mod":
             mod()
    
        case _:
         print("Invalid option. Please choose a valid operation.")
        
    
    


    

