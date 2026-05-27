print("*Palindrome Checker*")

text = input("Enter a number to check if it is a palindrome: ")
reverse = ""

for i in text:
    reverse = i + reverse

if text == reverse:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")