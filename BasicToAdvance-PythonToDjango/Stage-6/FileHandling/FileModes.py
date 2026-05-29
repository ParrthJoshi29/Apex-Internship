print("*FileModes:\n*")

#File Modes in Python:
    #Whenever Python works with files, it needs to know what you want to do with the file.
    # That is called File Mode.You use it inside open().

#Syntax:
    #open("filename.txt", "mode")

#Example:
    #file = open("data.txt", "r")
    
#Here:

    #"data.txt" → file name
    #"r" → mode (read mode)
#------------------------------------------------------------------------------------------------------------------
def f_write():
    file = open("FileModes.txt","w")
    file.write("File Modes Text File.") 
    print("Write Mode Succesfully Executed Suceesfully!")
    file.close()

def f_read():
    file = open("FileModes.txt", "r")

    fr = file.read()
    print("\n Read Mode Successfully Exececuted Succesfully!")
    print(fr)

    file.close()

def f_append():
    file = open("FileModes.txt", "a")

    fa = file.write("\n Append Mode Successfully Exececuted Succesfully!")
    print("\nAppended Data!")

    file.close()

#--------------------------------------------------------------------------------    
#1. w" → Replace Everything

#Before:
    #ABC
    
#After writing:
    #XYZ
    
#Result:
    #XYZ

#Example:
f_write()
#------------------------------------------------------------------------------    
#2. "r" → Read Mode:- Used to read data from a file.

#Important Points

# Default mode
# File must already exist
# Cannot write anything#
# Gives error if file not found

#Example
    #Suppose FileModes.txt contains: File Modes Text File.


#Python:
    #Opens file
    #Reads content
    #Stores in variable
    #Prints it
#Error Example
    #file = open("abc.txt", "r")

#If file does not exist:
    #FileNotFoundError
f_read()
#---------------------------------------------------
#3."a" → Append Mode:- Add Data wihout overwriting the already existing data.
#Before:
    #ABC
#After append:
    #ABC
    #XYZ
f_append()
f_read()
#----------------------------------------------------------------------------