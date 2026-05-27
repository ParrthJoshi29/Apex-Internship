print("*Types of Functions in Python*")
print()

def function_without_parameters():
    print("This is a function without parameters.")
    print("Welcome to Python programming!")

def function_with_parameters(name):
    print("This is a function with parameters.")
    print("Hello", name , "!")

def function_with_multiple_parameters(name, age):
    print("This is a function with multiple parameters.")
    print("Hello", name , "!","You are", age, "years old.")

def function_with_return_value(x, y):
    return x + y

#Difference Between print() and return
def using_print():
    print(5)

def using_return():
    return 5

def function_with_default_parameters(Country = "India"):
    print("This is a function with default parameters.")
    print("Hello", Country , "!")

def keyword_arguments(name, age):
    print("This is a function with keyword arguments.")
    print(name , age)

def function_with_conditional_statements(num):
    if num %2 == 0:
        return "Even"
    else:
        return "Odd"
    
def function_with_loop(n):
    print("This is a function with a loop.")
    for i in range(1,6):
        print(n*i)

def pre_defined_functions():
    print("This is a function that uses pre-defined functions.")

    def length():
        name = "Parth"
        print("Length",len(name))

    def typee():
        name = "Parth"
        print("Type",type(name))

    def maxx():
        lst = [1, 2, 3, 4, 5]
        print("Max",max(lst))
    
    def minn():
        lst = [1, 2, 3, 4, 5]
        print("Min",min(lst))
    
    def summ():
        lst = [1, 2, 3, 4, 5]
        print("Sum",sum(lst))

    def sortedd():
        lst = [5, 2, 3, 1, 4]
        print("Sorted",sorted(lst))
    
    def abss():
        num = -111
        print("Absolute",abs(num))
    
    def roundd():
        num = 3.14159
        print("Rounded",round(num,2))
    
    def poww():
        base = 2
        exponent = 3
        print("Power",pow(base,exponent))

    length()
    typee()
    maxx()
    minn()
    summ()
    sortedd()
    abss()
    roundd()
    poww()

def recursive_function(n):
    if n > 5:
        print("This is a recursive function.")
        return
    print(n)

    recursive_function(n + 1)

lambda_function = lambda a,b : a+ b

#function_without_parameters()
#print()

#function_with_parameters("Parth")
#print()

#function_with_multiple_parameters("Parth", 20)
#print()

#print("This is a function with a return value.")
#result = function_with_return_value(5, 10)
#print("The result of the function is:", result)
#print()

#x = using_print()
#print(x)

#y = using_return()
#print("\n",y)

#function_with_default_parameters()
#function_with_default_parameters("Japan")
#print()

#keyword_arguments(name = "Parth", age = 20)
#print()

#n = int(input("Enter a number to check if it is even or odd: "))
#print("The number is:", function_with_conditional_statements(n))
#print()

#function_with_loop(5)
#print()

#pre_defined_functions()
#print()

#recursive_function(1)
#print()

#Syntax- lambda parameters : expression
print("This is a lambda function.")
print(lambda_function(5, 10))
print()



