print("************JSON HANDLING***************")
# What is an API? -  API = Application Programming Interface
                     # But this full form confuses beginners 
                     # So understand it in the simplest REAL way.

# Real Life Example — Restaurant

# Imagine:
    # You = Customer
    # Kitchen = Backend / Server
    # Waiter = API

# You do NOT go inside kitchen directly.

# Instead:
    # You tell waiter your order
    # Waiter takes request to kitchen
    # Kitchen prepares food
    # Waiter brings response back

# That waiter is exactly like an API.

# In Software - When two applications want to communicate, they use an API.

# Example:
    # Application	Talks To
    #-------------------------------
    # Instagram App	Instagram Server
    # Weather App	Weather Server
    # Payment App	Bank Server

# Communication happens using APIs.

# Super Simple Definition - API is a messenger that sends data between:
    # frontend ↔ backend
    # app ↔ server
    # website ↔ database/services
#----------------------------------------------------------------------------
#  What is Frontend? - Frontend = what user sees.

# Examples:
    # buttons
    # forms
    # login page
    # colors
    # text
    # UI

# Built using:
    # HTML
    # CSS
    # JavaScript
    # React
#----------------------------------------------------------------------------
#  What is Backend? - Backend = hidden logic.

# Examples:
    # checking password
    # saving user data
    # database operations
    # authentication
    # calculations

# Built using:
    # Python
    # Django
    # Node.js
    # Java
    
#  Django is Mainly Backend

# Django handles:
    # logic
    # database
    # authentication
    # APIs
    # data processing
#----------------------------------------------------------------------
#  Example of API Flow

# Suppose you login into Instagram.

# Step 1 — Frontend Sends Request

# Frontend sends:

# {
#    "username":"parth",
#    "password":"1234"
# }

# This data is sent to backend through API.

#----------------------------------------------------------------------------
# Step 2 — Backend Checks

# Django checks:

# if username == "parth":
#     print("Login Success")

#----------------------------------------------------------------------------
# Step 3 — Backend Sends Response

# Backend returns:

# {
#    "message":"Login Successful"
# }

# Frontend shows:
# Login Successful
#---------------------------------------------------------------------------

# Why JSON is Used Here?

# Because JSON is lightweight and easy for all languages to understand.

# Python understands JSON.
# JavaScript understands JSON.
# Apps understand JSON.

# So JSON became standard.

#--------------------------------------------------------------------------------
# Another Real Example

# Suppose weather app asks server:

# {
#    "city":"Ahmedabad"
# }

# Server responds:

# {
#    "temperature":"38°C",
#    "weather":"Sunny"
# }

# This is API communication using JSON.

#  VERY IMPORTANT TERM
# Request vs Response

# Term	    Meaning
#----------------------------
# Request	Asking for data
# Response	Receiving data

# Example

# You ask:

# {
#    "username":"parth"
# }

# This is REQUEST.


# Server replies:

# {
#    "status":"success"
# }

# This is RESPONSE.

#----------------------------------------------------------------------------

#  What is Server? - Server = powerful computer/program that provides services/data.

# Examples:
    # Instagram server
    # Google server
    # YouTube server

# Your Django app can also become a server.

#----------------------------------------------------------------------------

# What is Database? - Database stores data permanently.

# Examples:
    # users
    # passwords
    # products
    # orders

# Popular databases:
    # MySQL
    # PostgreSQL
    # SQLite

# Django connects with database.

#----------------------------------------------------------------------------

# How JSON Connects to Django

# This is the important chain:

# Frontend
#    ↓
# API Request
#    ↓
# JSON Data
#    ↓
# Django Backend
#    ↓
# Database
#----------------------------------------------------------------------------

#  Real Django API Example

# Later in Django you may write:

# from django.http import JsonResponse

# def home(request):

#     data = {
#         "name":"Parth",
#         "course":"Django"
#     }

#     return JsonResponse(data)

# This sends JSON response.

# Output
# {
#    "name":"Parth",
#    "course":"Django"
# }
#----------------------------------------------------------------------------

# Important Beginner Terms
#---------------------------------------
# Term	            Meaning
# API	            Messenger between apps
# JSON	            Data format
# Frontend	        User interface
# Backend	        Hidden logic
# Server	        Provides data/services
# Database	        Stores data
# Request	        Asking data
# Response	        Receiving data

#----------------------------------------------------------------------------
#  Most Important Thing to Understand

# When learning Django:
    # You are mainly building:
    # Frontend → API → Django → Database
    # This is modern web development.
#----------------------------------------------------------------------------
# Why JSON Handling is Important for YOU

# Because later you’ll:
    # build login systems
    # create APIs
    # send/receive data
    # work with React
    # use mobile apps
    # build real projects

    # ALL of these use JSON.
#----------------------------------------------------------------------------

# BEST WAY TO THINK

# Instead of thinking:

# “JSON is a topic”

# Think:

# “JSON is the language apps use to talk.”

# That understanding changes everything.
#----------------------------------------------------------------------------

# Now Actual JSON Topic Begins

# JSON = JavaScript Object Notation.
        # It is a lightweight format used to store and exchange data.
        # It looks almost like a Python dictionary.

# Example JSON
# {
#     "name": "Parth",
#     "age": 19,
#     "skills": ["Python", "Django"]
# }
# Real Life Django Usage

# When frontend sends data to backend:

# {
#    "username": "parth",
#    "password": "1234"
# }

# Django receives this JSON and processes it.
#------------------------------------------------------------------------------------

#  Python JSON Module

# Python has a built-in module:
    # import json
    # This module helps convert:

# Python → JSON	      JSON → Python
# Encoding	          Decoding

#------------------------------------------------------------------------------------

# MOST IMPORTANT FUNCTIONS
# Function	    Meaning
#_________________________________________
# json.dumps()	Python → JSON string
# json.loads()	JSON string → Python
# json.dump()	Python → JSON file
# json.load()	JSON file → Python

# These 4 are the core.

#------------------------------------------------------------------------------------

# Topic 1 — json.dumps() - Convert Python object into JSON string.

# Example
def json_dumps():
    print("\nJson Dumps Example\n")
    
    import json
    
    data = {
     "name": "Parth",
     "age": 19
     }
    
    print(data)
    print(f"Before Dumps: {type(data)} \n")

    result = json.dumps(data)

    print(result)
    print("After Dumps: ")
    print(type(result))
    
json_dumps()

#--------------------------------------------------------------------------
# Important Observation

# Before conversion:

# type(data)
# # dict

# After conversion:

# type(result)
# # str

# JSON data is usually stored/transferred as string.
#-----------------------------------------------------------------------------

# Topic 2 — json.loads() - Convert JSON string into Python dictionary.

# Example

def json_loads():
    print("\nJson Loads Example")
    import json

    data = '{"name":"Parth","age":19}' #Because we have to convert Python String to Dictionary and Json.load() Directly doesn't work on Python Dictionary.
    
    print("\n",data)
    print(f"Before Loads {type(data)}\n")
    
    result = json.loads(data)

    print(result)
    print("After Loads")
    print(type(result))

json_loads()

#--------------------------------------------------------------------------------------- 

#  Easy Memory Trick
# Function	Full Form
#___________________________
# loads()	Load String
# dumps()	Dump String
#----------------------------------------------------------------------------------------

# #Topic 3 — json.dump() - Store Python data into JSON file.

# Example

def json_dump():
    print("\nJson Dump Example")
    import json

    data = {
     "name": "Parth",
     "course": "Django"
    }

    file = open("data.json", "w")

    json.dump(data, file)

    file.close()

    print("JSON File Created")

json_dump()
    
#------------------------------------------------------------------------------------------------
#  Result
    # A file named: data.json gets created.
#------------------------------------------------------------------------------------------------

# Topic 4 — json.load() - Read JSON file and convert into Python object.

# Example
def json_load():
    print("\nJson Load Example")
    import json

    file = open("data.json", "r")

    data = json.load(file)

    print(data)
    print(type(data))

    file.close()
    
json_load()

#-------------------------------------------------------------------------------------------------

# Output
# {'name': 'Parth', 'course': 'Django'}
# <class 'dict'>
#-------------------------------------------------------------------------------------------------

# NOW THE MAGIC FORMULA
# s = STRING
# no s = FILE

# That’s the biggest shortcut.

# THE COMPLETE MEMORY TABLE

# Function	Meaning	                Works With
#_____________________________________________
# dumps()	Python → JSON String	STRING
# loads()	JSON String → Python	STRING
# dump()	Python → JSON File	    FILE
# load()	JSON File → Python	    FILE

# dump = Python → JSON
# load = JSON → Python

#----------------------------------------------------------------------------------------------------