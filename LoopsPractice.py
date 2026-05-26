print("*Loops Practice*")
def basic_loop():
    for i in range(2,11,2): # Start,Stop,Step
        print("This is loop iteration number", i)

def list_loop():
    fruits = ["apple","banana","mango"]
    for fruit in fruits:
        print("I like", fruit)

def while_loop(): 
    count = 1
    while count <= 5: 
        print("This is while loop iteration number", count)
        count += 1

def loop_break(): # exits the loop when a certain condition is met
    for i in range(1,10):
        if i == 2:
            break
        print("This is loop break iteration number", i)

def loop_continue(): # skips the current iteration and continues with the next one
    for i in range(1,6):
        if i == 3 or i == 4:
            continue
        print("This is loop continue iteration number", i)

def loop_pass(): # does nothing, used as a placeholder until actual name is given
    for i in range(1,6):
        if i == 3:
            pass
        print("This is loop pass iteration number", i)

def nested_loop_rightangle():
    for i in range(1,6):
        for j in range(i):
            print("*", end="")
        print()

def nested_loop_inverted_rightangle():
    for i in range(5,0,-1):
        for j in range(i):
            print("*",end = "")
        print()

def loop_pyramid():
    n = 5
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ", end="")
        for k in range(i):
            print("* ", end="")
        print()

def loop_revpyramid():
    n = 5 
    for i in range(5,0,-1):
        for j in range(n-i):
            print(" ", end ="")
        for k in range(i):
            print("* ", end="")
        print()

def loop_diamond():
    # Upper Part
    n = 5
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ", end="")
        for k in range(i):
            print("* ", end="")
        print()

    # Lower Part
    n = 5 
    for i in range(5,0,-1):
        for j in range(n-i):
            print(" ", end ="")
        for k in range(i):
            print("* ", end="")
        print()

def loop_hollowSquare():
    n = 5 
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                print("* ", end="")
            else:
                print("  ", end="")
        print()

def loop_infinite():
    while True:
        print("This is an infinite loop. Press Ctrl+C to stop it.")


basic_loop()
print("\n")

list_loop()
print("\n")

while_loop()
print("\n")

loop_break()
print("\n")

loop_continue()
print("\n")

loop_pass()
print("\n")

nested_loop_rightangle()
print("\n")

nested_loop_inverted_rightangle()
print("\n")

loop_pyramid()
print("\n")

loop_revpyramid()
print("\n")

loop_diamond()
print("\n")

loop_hollowSquare()
print("\n")

loop_infinite()
print("\n")