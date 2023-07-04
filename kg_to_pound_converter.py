
# 1. Define a function named `kg_to_pounds` that takes a weight in kilograms (`kg`) as input.
def kg_to_pounds(kg):
# 2. Inside the `kg_to_pounds` function, multiply the weight (`kg`) by the conversion factor `2.20462`. This will give you the equivalent weight in pounds.

# 3. Return the calculated weight in pounds.
    return kg * 2.20462
# 4. In the main part of your program, prompt the user to enter a weight in kilograms.

# 5. Use the `input` function to read the user's input and convert it to a float using the `float` function.
weight_in_kg = float(input("Enter your weight in kg: "))
# 6. Call the `kg_to_pounds` function with the entered weight as the argument, and assign the result to a variable named `converted_weight`.

converted_weight = kg_to_pounds(weight_in_kg)

# 7. Print the converted weight using the `print` function, with an appropriate message.
print(f"Your weight in pounds is: {converted_weight}")
# Here's an example implementation of the program:
# python