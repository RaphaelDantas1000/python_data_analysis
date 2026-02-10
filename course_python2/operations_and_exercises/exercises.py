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



## 7. Write a program that receives something typed by the user and checks if they typed anything, returning True if they did and False if they didn't.

user = input("Type something: ")

tf = bool(user)

print(tf)



## 8. Write a program that receives the following data from an employee: name, age, and salary. At the company where this employee works, their salary increases by $ 800.90 each year.

name = input("Please tell us your name: ")

age = int(input("Please tell us your age: "))

salary = float(input("Please tell us your salary: "))

new_salary = salary + 800.90

new_age = age + 1

print(f"Employee {name}, in 1 year, will be {new_age} years old, and will be receiving a salary equal to ${new_salary:.2f} next year")


## 9. Write a program that asks the user to enter two numbers and displays on the screen the result of the sum, subtraction, multiplication, division, and remainder of the division of those numbers.

first_number = float(input("Please write a number: "))

second_number = float(input("Please write another number: "))

addition = first_number + second_number
print(f"{addition:.2f}")

subtraction = first_number - second_number
print(f"{subtraction:.2f}")

multi = first_number * second_number
print(f"{multi:.2f}")

division = first_number / second_number
print(f"{division:.2f}")

remainder = first_number % second_number
print(f"{remainder}")


## 10. Write a program that asks the user for the radius of a circle and displays the area and perimeter of that circle on the screen (consider pi = 3.14). Round to 2 decimal places.

circle_radius = float(input("What is the radius of a circle? "))


pi = 3.14
area = pi * circle_radius ** 2 
perimeter = 2 * pi * circle_radius

print(f"{area:.2f}")
print(f"{perimeter:.2f}")


## 11. Write a program that asks the user for the price of a product and displays the price with a 10% discount.

price = float(input("Could you please tell me the price of an egg: "))

egg_discount = price * 0.9
print(f"{egg_discount:.2f}")


## 12. Write a program that reads the temperature in degrees Celsius and displays the temperature in degrees Fahrenheit. The formula to convert from Celsius to Fahrenheit is: F = (9/5)*C + 32.

celsius = float(input("what is today's temparature in celsius?: "))

fahrenheit = (9/5) * celsius + 32

print(f"{fahrenheit:.2f}")


## 13. Write a program that asks the user to enter 3 integers and displays the arithmetic mean of those numbers. Round to 1 decimal place.

number_one = int(input("enter a number: "))

number_two = int(input("enter a number: "))

number_three = int(input("enter a number: "))

addition = number_one + number_two + number_three

arithmetic = addition / 3

print(f"{arithmetic:.1f}")



## 14. Write a program that reads a person's weight and height and displays their body mass index (BMI). The formula for calculating BMI is: BMI = weight/height², rounded to 3 decimal places.

height = float(input("What's your height?: "))

weight = float(input("Tell us your weight: "))

bmi = weight / height ** 2

print(f"Your BMI is {bmi:.3f}")



## 15. Write a program that reads two integers from the user and swaps their values; that is, if the first number is 5 and the second number is 7, the program should make the first number equal to 7 and the second number equal to 5.

entry1 = int(input("please enter a number from 1 to 9: "))

entry2 = int(input("please enter a number from 1 to 9: "))

temp = entry1
entry1 = entry2
entry2 = temp

print(entry1)
print(entry2)


##  16. Write a Python program that reads an integer and checks if it is even or odd.

entry = int(input("Enter a number: "))

if entry % 2 == 0:
    print("The number is even")
else:
    print("The number is odd") 


## 17. Write a Python program that reads a number and returns its square, square root, and cube root, rounded to 2 decimal places.

number = int(input("Enter a number: "))

number_squared = number ** 2

square_root = number ** 0.5 

cube_root = number ** (1/3)  

print(f"{number_squared:.2f}")

print(f"{square_root:.2f}")

print(f"{cube_root:.2f}")



## 18. Write a Python program that reads the value of two legs of a right triangle and returns the value of the hypotenuse, assuming that it is possible to form a triangle.

first_side = int(input("Enter a number:"))

second_side = int(input("Enter a number:"))

hypotenuse = (second_side ** 2 + first_side ** 2) ** 0.5

print (f"{hypotenuse:.2f}")