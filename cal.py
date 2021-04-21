import math

a = int(input('Enter value of a: '))
b = int(input('Enter value of b: '))

#Addition

#Subtraction

#Multiplication
def multiply():
    result = int
    result = a*b
    print(result)

#Division

print("Enter your choice: ")
print("a. Add")
print("b. Subtract")
print("c. Multiplication")
print("d. Division")

choice = input("Enter choice: ")

if choice == 'a':
    print("add")
    
elif choice == 'b':
    print("subtract")

elif choice == 'c':
    multiply()

elif choice == 'd':
    print("divide")

else:
    print("Invalid choice")
