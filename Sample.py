name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("\nHello", name + "!")
print("Welcome to Python 🚀")


if age >= 18:
    print("You are an adult.")
else:
    print("You are a teenager.")


tasks = []


for i in range(3):
    task = input(f"Enter task {i + 1}: ")
    tasks.append(task)


print("\nYour Tasks for Today:")
for number, task in enumerate(tasks, start=1):
    print(number, "-", task)



study_hours = int(input("\nHow many hours did you study today? "))

remaining = 24 - study_hours

if remaining <= 0:
    print("You have exceeded the number of hours in a day!")
else:
     print("You still have", remaining, "hours left in the day.")   

print("\nThank you for using Student Daily Helper,", name + "!")
print("Have an amazing day 😊")