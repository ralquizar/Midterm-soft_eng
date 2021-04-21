import math

a = int(input('Enter value of a: '))
b = int(input('Enter value of b: '))

#Addition
def Addition():
    sum= a + b
    print (sum)

#Subtraction

#Multiplication

#Division

print("Enter your choice: ")
print("a. Add")
print("b. Subtract")
print("c. Multiplication")
print("d. Division")

choice = input("Enter choice: ")

if choice == 'a':
    Addition()

elif choice == 'b':
    print("subtract")

elif choice == 'c':
    print("multiply")

elif choice == 'd':
    print("divide")
	
else:
    print("Invalid choice")

    #good luck guys!
