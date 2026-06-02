print("*Modules & Packages*")

# First Understand the Big Idea

# Think like this:
    # Real Life	Python
    # One notebook	Module
    # One school bag containing notebooks	Package
    
#  WHAT IS A MODULE? - A module = a single Python file (.py) containing code.

# Example:
    # math_utils.py

# Inside it:
    # def add(a, b):
    #     return a + b

    # def sub(a, b):
    #     return a - b

# This file itself is called a module.

# WHY MODULES ARE USED?
    # Without modules:
        # all code becomes huge
        # difficult to manage
        # repeated code
        # confusing debugging

# Modules help in:
    #  Reusability
    #  Clean code
    #  Separation of logic
    #  Large project management
    #  Team collaboration
    
# This is EXACTLY why Django uses them heavily.
#-------------------------------------------------------------------------
# HOW TO IMPORT MODULES

# METHOD 1 — Normal Import
        # File: math_utils.py
            # def add(a, b):
            #     return a + b
            
# File: main.py
def main_py():
    print("\nNormal Import")
    import math_utils
    result = math_utils.add(10, 5)
    print(result)

main_py()
    
# Understand
    # import math_utils
    # means:
# “Bring the whole file into this program.”

# Then:
    # math_utils.add()
    # means:
    # “Use add() function from math_utils file.”
#--------------------------------------------------------------------------
# METHOD 2 — Import Specific Function

def imprt_spec():
    print("\nImporting Specific Function from MOdule.")
    from math_utils import add
    print(add(5, 3))

imprt_spec()
                
            # Meaning
            # from math_utils import add
            
            # means:
                # “Only bring add() function.”
                
            # Now no need to write:
                # math_utils.add()
#----------------------------------------------------------------------------                
# METHOD 3 — Import Multiple Things

def imp_multi():
    print("\nImporting Multiple Functions")
    from math_utils import add, sub
    print(add(10,10))
    print(sub(10,20))

imp_multi()    
#----------------------------------------------------------------------------    
# METHOD 4 — Import Everything

# from math_utils import *
    # NOT recommended in professional coding.

# Why?
    # Because:
        # memory waste
        # confusion
        # name conflicts
        
# Django developers usually avoid this.
#----------------------------------------------------------------------------

# METHOD 5 — Alias Import (VERY IMPORTANT)

def imp_alias():
    print("\nImporting Alias(as) Function")
    import math_utils as mu
    print(mu.add(2, 3))
    
imp_alias()
    
#  Why alias?
    # Used when:
        # module names are long
        # cleaner code needed
# Very common in real projects.

# Example:
    # import pandas as pd
    # import numpy as np
#-------------------------------------------------------------------------------
#Built-in Modules in Python

#  1. Math Module
print("\nBuilt-in Modules in Python")
def math_mod():
    print("\nMath Module")
    import math
    print(math.sqrt(16))
    print(math.pi)

math_mod()
#---------------------------------------------------------------------------------

# 2. Random Module
def random_mod():
    print("\nRandom Module") # prints any random number from 1 to 10.
    import random
    print(random.randint(1,10))

random_mod()
#-----------------------------------------------------------------------------------

# 3. DateTime Module(VERY IMPORTANT FOR DJANGO)
def date_time_mod():
    print("DateTime Module")
    import datetime
    today = datetime.datetime.now()
    print(today)

date_time_mod()
#------------------------------------------------------------------------------------

# USER-DEFINED MODULES in Python - Modules created by YOU.

# Example:
    # student.py
    # calculator.py
    # database.py
#------------------------------------------------------------------------------------

#WHAT IS A PACKAGE? -  A package = folder containing multiple modules.

# Example:

    # myproject/
    # │
    # ├── main.py
    # │
    # └── utils/
    #     ├── __init__.py
    #     ├── math_utils.py
    #     └── string_utils.py
    
# Important
    # __init__.py - This file tells Python: “This folder is a package.”
    # Without it, older Python versions may not recognize the folder properly.
    # In modern Python it's sometimes optional, but in professional development it’s still important.

# IMPORTING FROM PACKAGE

# Suppose:

# math_utils.py
    # def add(a, b):
    #     return a + b
    
# main.py
    # from utils.math_utils import add
    # print(add(5, 4))
    
#  Understand Deeply
# from utils.math_utils import add

# means:

    # Part	        Meaning
    #----------------------
    # utils 	    package(folder)
    # math_utils	module(file)
    # add	        function

    
# PACKAGE VS MODULE
# Module	        Package
#---------------------------------
# Single .py file	Folder
# Contains code	    Contains modules
# Small unit	    Collection of modules
#--------------------------------------------------------------------------------------------

# HOW DJANGO USES MODULES & PACKAGES / Now VERY IMPORTANT PART.

# Example Django Structure
# project/
# │
# ├── manage.py
# │
# ├── project/
# │   ├── settings.py
# │   ├── urls.py
# │   ├── wsgi.py
# │   └── __init__.py
# │
# └── app/
#     ├── models.py
#     ├── views.py
#     ├── admin.py
#     └── urls.py

# Observe Carefully
# File	            Type
#----------------------------
# settings.py	    module
# views.py	        module
# models.py	        module
# app folder	    package
# project folder	package

# Django is basically: “many packages containing many modules”
#------------------------------------------------------------------------------------------------------

#VERY IMPORTANT DJANGO IMPORTS
#  Example 1 - from django.shortcuts import render

# Part	    Meaning
#----------------------------
# django	package
# shortcuts	module
# render	function
#-------------------------------------------------------------------------------------------------------------

#  Example 2 - from django.http import HttpResponse

# Part	     Meaning
#--------------------
# django        package
# http	        module
# HttpResponse	class
#------------------------------------------------------------------------------------------------------------------

#  Example 3 - from .models import Student (VERY IMPORTANT).

# The dot . means: “Current folder/package”.Used heavily in Django apps.
#--------------------------------------------------------------------------------------------------------------------

#ABSOLUTE IMPORT VS RELATIVE IMPORT

# Absolute Import
    # from utils.math_utils import add
    # Full path given.
    # Preferred mostly.

# Relative Import
    # from .math_utils import add
    # Dot means current package or current folder.
    # Used a LOT in Django.
#----------------------------------------------------------------------------------------------------------------------

# SPECIAL MODULES YOU MUST KNOW FOR DJANGO

# os module

# Used for:
    # file paths
    # folders
    # environment variables

# Example:
def os_mod():
    print("\nOS Module Example")
    import os
    print(os.getcwd()) # cwd - get current working directory.
    
os_mod()

# In Django settings:
    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#-------------------------------------------------------------------------------------------------------------------------

# json module - VERY VERY IMPORTANT.

# Used in:
    # APIs
    # frontend-backend communication
    # REST APIs
    # AJAX
    # data exchange

# Example:
def json_mod():
    print("\nJson Module Example")
    import json
    data = {
   "name": "Pj",
    "age": 20 }
    json_data = json.dumps(data) # Returns the data directly as a string object.
    print(json_data)

json_mod()
#------------------------------------------------------------------------------------------------------------------------