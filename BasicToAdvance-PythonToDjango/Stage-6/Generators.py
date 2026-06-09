print("*Generators in Python*")

# Generators are very important in Python because they help handle large data efficiently without using too much memory.

# Django internally uses generator-like behavior in many places (querysets, streaming responses, etc.), so understanding the concept is useful.

#-----------------------------------------------------------------------------------------------------------------------------------------------

# 1. What is a Generator? - A generator is a special function that:
    # returns values one by one
    # uses yield
    # remembers its previous state

# Normal function → gives everything at once
# Generator → gives values slowly when needed

#-----------------------------------------------------------------------------------------------------------------------------------------------

# 2. Normal Function vs Generator

# Normal Function

def normal_fun():
    
    print("\nNormal Function Example")
    return [1,2,3]

print(normal_fun())

    # Output:

    # [1, 2, 3]

    # Everything comes together.

#normal_fun()


# Generator Function

def gen_fun():
    
    print("\nGenerator Function Example")
    yield 1
    yield 2
    yield 3

for i in gen_fun():
    print(i)

print("\n",gen_fun())

    # Output:

    # <generator object ...>

    # Because generator stores values lazily.

#gen_fun()

#-----------------------------------------------------------------------------------------------------------------------------------------------------

# 3. Getting Values from Generator

# Using loop
# def nums():
#     yield 1
#     yield 2
#     yield 3

# for i in nums():
#     print(i)

# Output:

# 1
# 2
# 3

#-----------------------------------------------------------------------------------------------------------------------------------------------

# 2. yield in Python — yield is used inside a function to make it a generator.

# Instead of:
    # giving all values together (return)
    # it gives values one-by-one
    # and pauses the function.

# (a). Simplest Definition

    # yield = “Give value now, but continue later from same place.”


# (b). Syntax

    # def function_name():
    #     yield value

    # Example:

        # def nums():
        #     yield 1
        #     yield 2
        #     yield 3
        

# (c). How yield Works Internally

    # When Python sees yield:
        #  function pauses
        #  state gets saved
        #  next time it continues from same line
        

# (d). Step-by-Step Example 

    # def test():
    #     print("A")
    #     yield 1

    #     print("B")
    #     yield 2

    # g = test()

    # print(next(g))
    # print(next(g))
    
    
# (e). What Happens Here Internally
    # Step 1
    # g = test()

    # Function does NOT run yet.

    # Generator object created.

    # Step 2
    # next(g)

    # Function starts.

    # print("A")

    # runs.

    # Then:

    # yield 1

    # gives value 1

    # Function PAUSES there.

    # Output:

    # A
    # 1
    # Step 3

    # Again:

    # next(g)

    # Now function resumes AFTER previous yield.

    # print("B")

    # runs.

    # Then:

    # yield 2

    # Output:

    # B
    # 2
    
    
# (f). Visual Flow
    # yield → pause → save position → continue later


# (g). return vs yield
    # return	yield
    # Ends function completely	Pauses function
    # Gives all result	Gives one-by-one
    # Function forgotten	Function remembered
    # Example with return
    # def test():
    #     return 1
    #     return 2

    # Second return never runs.

    # Function ended.

    # Example with yield
    # def test():
    #     yield 1
    #     yield 2

    # Both values come one-by-one.


# (h). Why yield is Useful

    # Suppose huge data:

    # 1 crore numbers

    # Using list:

    # huge memory

    # Using yield:

    # one-by-one values
    # very memory efficient


# (i). Real-Life Analogy 
    # return

    # Teacher gives whole book at once.

    # yield

    # Teacher gives one page at a time.


# (j). Most Important Example
    # def counter():
    #     yield 1
    #     yield 2
    #     yield 3

    # g = counter()

    # print(next(g))
    # print(next(g))
    # print(next(g))

    # Output:

    # 1
    # 2
    # 3


# (k). Using for Loop

    # Usually generators used with loops.

    # def nums():
    #     yield 10
    #     yield 20
    #     yield 30

    # for i in nums():
    #     print(i)

    # Output:

    # 10
    # 20
    # 30


# (l). VERY IMPORTANT THING 

    # After all yields finish:

    # next(g)

    # gives error:

    # StopIteration

    # because generator ended.


# (m). Memory Concept 
    # Without yield
    # x = [i for i in range(1000000)]

    # Stores everything in memory.

    # With yield
    # def nums():
    #     for i in range(1000000):
    #         yield i

    # Only one value generated at a time.

    # Much better.



# (n). Super Important Django Connection 

    # Django QuerySets behave lazily.

    # Example:

    # users = User.objects.all()

    # Data isn’t fully loaded immediately.

    # This lazy behavior is conceptually similar to generators.


# (o). MOST IMPORTANT THINGS TO REMEMBER 
    # yield

    # pauses function
    # saves state
    # gives values one-by-one
    # creates generator
    # memory efficient


# (p). Ultra Short Revision 
    # yield = pause + save + continue later


# (q). Final Beginner-Level Understanding

    # When function has:

    # yield

    # it becomes:

    # special function
    # called generator
    # values come slowly one-by-one instead of together

    # That’s the core idea.