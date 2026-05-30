print("*Exception Handling*")

# Think of Exception Handling as: “Handling errors gracefully instead of crashing the program.”


#Without exception handling:
    #num = int(input("Enter number: "))
    #print(num)

#If user enters:
    #abc

#Python crashes:
    #ValueError

#That crash = Exception.

#Why Exception Handling is VERY Important in Django

#In Django:
    #User enters wrong data
    #Database connection fails
    #File/image missing
    #Form validation fails
    #API fails
    #Login errors happen

#If exceptions are not handled:
    #Website crashes
    #User sees ugly error page
    #App becomes unstable

#So Django developers use exception handling A LOT.
#-----------------------------------------------------------------------------------------------
# Basic Structure
#try:
    # risky code
#except:
    # error handling code

def normal_ex():
    try:
        print("\nBasic Example")
        num = int(input("Enter a number: ")) #use float if needed decimal values too.
        print(num)

    except: # if you enter "10abc" then also Python raises ValueError as int cannot convert string to int.
        print("Invalid Input")
        
normal_ex()
    
#Now if user enters:
    #abc

#Output:
    #Invalid Input

#Program does NOT crash.

#How It Works Internally

#Python says:
    #TRY this code.
    #If error happens,
    #jump to EXCEPT block.

#------------------------------------------------------
#1. ValueError:-

def Value_error():
    try:
        print("\nValueError Example")
        num = int(input("Enter only numbers: "))
        print(f"Your Number: {num}")
        
    except ValueError:
        print("Oops..Please enter only numbers!")

Value_error()
#------------------------------------------------------
#2. ZeroDivisionError:

def div_Zero_error():
    try:
        print("\nDivideByZero Example")
        num1 = int(input("Enter first number to divide: "))
        num2 = int(input("Enter second number to divide: "))
        div = num1 / num2
        print(f"Divsiion:  {div}")
        
    except ZeroDivisionError:
        print("Not Divisible by 0")
        
div_Zero_error()

#-------------------------------------------------------
# 3. IndexError

def index_error():
    print("\nIndex Error Example")
    mylist = [10, 20, 30]

    try:
        print(mylist[5])

    except IndexError:
        print("Index does not exist")

index_error()

#--------------------------------------------------------
# 4. FileNotFound Error - VERY IMPORTANT for Django/media/files.

def file_not_found_error():
    print("\nFileNotFound Error Example")
    try:
        file = open("data.txt", "r")

    except FileNotFoundError:
        print("File not found")

file_not_found_error()

#---------------------------------------------------------

#5. What is e ? e is an exception object.

# It stores:
    # actual error message
    # error information
    # error details

# Think of it like:
    # e = error information
    
# Without as e

def e_exception():
    print("\nExpection 'e' Example ")
    
#---------------
    # try:
    #     print("Without as 'e' ")
    #     num = int(input("Enter: "))

    # except ValueError:
    #     print("Invalid Input")

# Output:

# Invalid Input # You only see your custom message.

# With as e
    
#---------------
try:
    print("\nWith as 'e' ")
    num = int(input("Enter: "))

except ValueError as e:
    print(e)

e_exception()

# If user enters:
    # 10abc

# Output:
    # invalid literal for int() with base 10: '10abc'
    # Now Python gives REAL error details.
    # Real Meaning
    
# except ValueError as e:  means: “Catch the ValueError and store its information inside variable e”

#---------------------------------------------------------

#6 Finally Block → VERY IMPORTANT.Runs ALWAYS.

#Used for:
    # closing files
    # database cleanup
    # resource cleanup
    
def finally_exception():
    try:
        print("\nFinally Block Example")
        file = open("data.txt")

    except FileNotFoundError:
        print("File missing")

    finally:
        print("Program ended")

finally_exception()

#Even if error happens: finally still runs.

#----------------------------------------------------------

#7. Raise Exception - Raising Exceptions (raise) . Important for Django later. You can create your own error.

def raise_exception():
    print("\nRaise Excepiton Example") 
    age = -5

    if age < 0:
        raise ValueError("Age cannot be negative")

raise_exception()

# Output:

# ValueError: Age cannot be negative

# Django internally raises MANY exceptions.


#-----------------------------------------------------------

#MOST IMPORTANT Exceptions: These are enough for strong foundation + Django.
 

# Exception     	Meaning
#-------------------------------------------
# ValueError	    Wrong value type
# TypeError	        Wrong datatype operation
# NameError	        Variable not defined
# IndexError	    Invalid list index
# KeyError	        Invalid dictionary key
# FileNotFoundError	File missing
# ZeroDivisionError	Divide by 0
# ImportError	    Module import failed
#--------------------------------------------

