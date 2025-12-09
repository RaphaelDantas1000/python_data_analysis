## Exercises 

## 1. Write a program that prints "I'm learning Python!" on the screen.

print("I'm learning Python!")


## 2. Write a program that asks the user to enter a number and then prints the message "The number entered was <number>" to the screen.

number = input("Please enter a number here: ")

print(f"The number entered was {number}")

## 3. Write a program that asks the user to enter their name and then prints the message "Hello, <name>!" on the screen.

greeting = input("Tell us your name: ")
print(f"Hello, {greeting}!")

## 4. Write a program that performs the addition and subtraction of two variables, one of type integer and the other of type decimal, displaying the sum and subtraction values ​​in the following format: "The sum is: <sum>" & "The subtraction is: <subtraction>".

a = 1.2
b = 0.4

add = a + b
subtraction = a - b

print(f"The sum is: {add}")
print(f"The subtraction is: {subtraction}")


## 5. Write a program that receives the user's age and returns their age plus 10 years in the following format: Your age in 10 years will be: <age + 10 years>.

age = int(input("Please type your age: "))

decade = age + 10

print(f"Your age in 10 years will be: {decade}")


## 6. Write a program that reads something typed by the user, displays its type, and shows all the information about it (hint: use the `is` function).

user_input = input("Type something: ")

print(f"You typed: {user_input}")
print(f"The type is: {type(user_input)}")

print("Is it only letters?", user_input.isalpha())
print("Is it only numbers?", user_input.isdigit())
print("Is it alphanumeric?", user_input.isalnum())
print("Is it uppercase?", user_input.isupper())
print("Is it lowercase?", user_input.islower())
print("Is it only spaces?", user_input.isspace())
