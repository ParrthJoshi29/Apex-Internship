print("*Iterators in Python*")

# Django internally uses iterators in:
    # Database QuerySets
    # File handling
    # Loops
    # Generators
    # API responses
    # Lazy loading

# So understanding this properly will help a LOT later.
#-------------------------------------------------------------------------------

# 1. What is an Iterator? - An iterator is an object that gives values one by one.

# Instead of giving all data together, it gives:
    # first value
    # then next value
    # then next value
    # until data finishes
    
# Real-Life Example

# Imagine:

    # A TV remote's Next Channel button.

    # You press:

    # next → channel 1
    # next → channel 2
    # next → channel 3

    # You get channels one at a time.

    # That is exactly how iterators work.

#-------------------------------------------------------------------------------

# 2. Why Iterators Exist?

# Suppose you have:
    # 10 numbers → easy
    # 10 lakh records from database → huge memory usage

# Iterator helps by:
    # loading one item at a time
    # saving memory
    # making programs faster
    # This is VERY important in Django.

#--------------------------------------------------------------------------------

# 3. Iterable vs Iterator (MOST IMPORTANT)

# Iterable - An object you can loop through.

# Examples:
    # list
    # tuple
    # string
    # set
    # dictionary

# Example:

def fun_iterable():
    print("\nIterables Example")
    
    nums = [1, 2, 3]

        # This is iterable.

    # Because we can do:
    
    for i in nums:
        print(i)
    
fun_iterable()
    
    
# Iterator  - An object that produces values one-by-one using:

    # next()
    
    # Easy Memory Trick
    
    # Term	        Meaning
    #_____________________________________
    # Iterable	    Collection of data
    # Iterator	    Gives data one by one

#Example

def fun_iterators():
    print("\nIterators Example")
    
    nums = [1 , 2 , 3]
    
    x = iter(nums)
    
    print(next(x))
    print(next(x))
    print(next(x))

fun_iterators()

#----------------------------------------------------------------------------------------

# 4. How to Create Iterator

# We use:

    # iter()

# Example:

    #See the function - fun_iterators()

# Output:
    # 10
    # 20
    # 30
    
# Flow Understanding

# nums = [10,20,30]
# This is iterable.

# Then:

# x = iter(nums)
# Now it becomes iterator.

# Then:

# next(x)
# Gives next value.

#----------------------------------------------------------------------------------------

# 5. What Happens After Data Ends?

# Example:

def stopiterationerror():
    print("\nStop Iteration Error")
    
    nums = [1,2]

    x = iter(nums)

    print(next(x))
    print(next(x))
    print(next(x))
    
#stopiterationerror()

# Output:

# 1
# 2
# StopIteration Error

# IMPORTANT

# Iterator remembers:
    # current position
    # next item

# Once finished:
    # StopIteration comes.
    
#----------------------------------------------------------------------------------------

# 6. For Loop Internally Uses Iterators

# VERY IMPORTANT CONCEPT.

# When you write:

def for_loop_iterators():
    
    print("\nIteratos in For Loop")

    for i in [1,2,3]:
        print(i)
  

for_loop_iterators()

# Python internally does:

# x = iter([1,2,3])

# print(next(x))
# print(next(x))
# print(next(x))

# So:
# for loop is built on iterators.

#------------------------------------------------------------------------------------------

# 7. Iterator Methods

# Mainly 2 important things:

# Function	Work
#___________________________________________
# iter()	Converts iterable to iterator
# next()	Gets next value

# These are MOST important. 

#---------------------------------------------------------------------------------------------

# 8. Iterator Properties

#Property	             Meaning
#______________________________________________
# Memory efficient	    Loads one-by-one
# Faster for huge data	Doesn't load everything
# Used in loops	        Core Python mechanism
# Stateful	            Remembers current position

#----------------------------------------------------------------------------------------------

# 8. StopIteration in Custom Iterator

# Proper iterator should stop.

# Example:
def stop_iterator_custom():
    print("\nStopIteration in Custom Iterator Example")

    class Count:

     def __init__(self):
         self.num = 1

     def __iter__(self):
         return self

     def __next__(self):

        if self.num > 5:
            print("Raised StopIteration")
            raise StopIteration
            

        x = self.num
        self.num += 1

        return x

    obj = Count()

    for i in obj:
        print(i)

stop_iterator_custom()

# Output:

# 1
# 2
# 3
# 4
# 5
# Raised StopIteration

#------------------------------------------------------------------

# 9. Iterator vs List (VERY IMPORTANT)

# List	            Iterator
#____________________________________________________
# Stores all data	Gives one-by-one
# More memory	    Less memory
# Faster access	    Better for huge data
# Reusable	        Gets exhausted

#---------------------------------------------------------------------

# 10. Where Django Uses Iterators (VERY IMPORTANT).

#Django uses iterators in:
    # QuerySets
    # File uploads
    # Streaming responses
    # Database rows
    # API pagination

# Example:

# users = User.objects.all()

# Django lazily fetches records one-by-one.
# Iterator concept behind this.

#-------------------------------------------------------------------------------------

# 11. Django QuerySets are Lazy (MOST IMPORTANT PRACTICAL CONNECTION)

# When Django does:
    # users = User.objects.all()

    # It does NOT load everything immediately.
    # It behaves iterator-like.
    # This is called:
    # Lazy Loading

    # SUPER important concept. 

