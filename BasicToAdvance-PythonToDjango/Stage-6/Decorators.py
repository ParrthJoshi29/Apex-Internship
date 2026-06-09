print("*Decorators in Python*")

# 1. WHAT IS A DECORATOR? - Decorator adds extra functionality to a function without changing original function.

#------------------------------------------------------------------------------------------------------------------------------

# 2. Understanding :
 
# THIS:

    # @login_required

    # is a decorator.

# WHAT IT DOES

    # Before running function:

    # Checks if user is logged in.

    # If yes:

    # run function

    # If no:

    # redirect to login page

#-----------------------------------------------------------------------------------------------------------------------------------

# 3. MOST IMPORTANT SYNTAX:

    # @decorator_name
    
    # def my_function():
    
    #     pass

#-----------------------------------------------------------------------------------------------------------------------------------

# 4. REAL HIDDEN WORKING

    # @decorator

    # actually means:

    # function = decorator(function)

    # VERY IMPORTANT.

#-----------------------------------------------------------------------------------------------------------------------------------

# 5. BASIC STRUCTURE ONLY:

    # def decorator(func):

    #     def wrapper():

    #         func()

    #     return wrapper

    # This much structure is enough currently.

#-----------------------------------------------------------------------------------------------------------------------------------

# 6. WHY DJANGO USES DECORATORS :

    # Use	                Example
    #_______________________________________________
    # Login checking	    @login_required
    # Permission checking	@permission_required
    # API restrictions	    @api_view
    # Caching	            @cache_page
    
#------------------------------------------------------------------------------------------------------------------------------------    
    
# 7. MOST IMPORTANT THING TO REMEMBER:

    # Decorator = Wrapper around function

    # That single line is enough for now.

#------------------------------------------------------------------------------------------------------------------------------------    

# Example:

def smart(func):
    
    def wrapper():
        
        print("Welcome")
        
        func()
        
        print("Thank You")
        
        return wrapper

@smart
def hello():
    
    print("Parth")
    
hello()