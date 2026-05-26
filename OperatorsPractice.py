print("**Operators Practice**")
def arithmetic_operators():
    a = 10
    b = 20
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    print("Division:", (a / b))
    print("Floor Division:", a // b)
    print("Modulus:", a % b)
    print("Exponentiation:", a ** b)

def assignment_operators():
    a = 10
    print("Initial value of a:", a)
    a += 5
    print("After addition assignment (a += 5):", a)
    a -= 3
    print("After subtraction assignment (a -= 3):", a)
    a *= 2
    print("After multiplication assignment (a *= 2):", a)
    a /= 4
    print("After division assignment (a /= 4):", a)

def logical_operators():
    x = True
    y = False

    print("Logical AND (x and y):", x and y) # both operands must be true for the result to be true, so the result is false
    print("Logical AND (y and x):", y and x) # both operands must be true for the result to be true, so the result is false
    print("Logical OR (x or y):", x or y) # if either operand is true, the result is true, so the result is true
    print("Logical OR (y or x):", y or x) # if either operand is true, the result is true, so the result is true
    print("Logical NOT (not x):", not x) # if x is true, not x is false, so the result is false
    print("Logical NOT (not y):", not y) # if y is false, not y is true, so the result is true

def comparison_operators():
    a = 10
    b = 20

    print("Equal to (a == b):", a == b) # checks if a is equal to b, so the result is false
    print("Not equal to (a != b):", a != b) # checks if a is not equal to b, so the result is true
    print("Greater than (a > b):", a > b) # checks if a is greater than b, so the result is false
    print("Less than (a < b):", a < b) # checks if a is less than b, so the result is true
    print("Greater than or equal to (a >= b):", a >= b) # checks if a is greater than or equal to b, so the result is false
    print("Less than or equal to (a <= b):", a <= b) # checks if a is less than or equal to b, so the result is true

def membership_operators():
    my_list = [1, 2, 3, 4, 5]
    print("Membership operator (3 in my_list):", 3 in my_list) # checks if 3 is in my_list, so the result is true
    print("Membership operator (6 in my_list):", 6 in my_list) # checks if 6 is in my_list, so the result is false
    print("Membership operator (3 not in my_list):", 3 not in my_list) # checks if 3 is not in my_list, so the result is false
    print("Membership operator (6 not in my_list):", 6 not in my_list) # checks if 6 is not in my_list, so the result is true

def identity_operators():
    a = [1, 2, 3]
    b = a
    c = [1, 2, 3]

    print("Identity operator (a is b):", a is b) # checks if a and b refer to the same object in memory, so the result is true
    print("Indentity operator (b is a)",b is a) # checks if b and a refer to the same object in memory, so the result is true
    print("Identity operator (a is c):", a is c) # checks if a and c refer to the same object in memory, so the result is false
    print("Identity operator (a == c):", a == c) # checks if a and c have the same value, so the result is true


arithmetic_operators()
print()

assignment_operators()
print()

logical_operators()
print()

comparison_operators()
print()

membership_operators()
print()

identity_operators()
print()