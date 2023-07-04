# calling_functions_in_Python
Exercise to practice writing and calling functions in Python

Here's a step-by-step guide to help you write the program:
1. Define a function named `is_prime` that takes a positive integer `num` as input.
2. Inside the `is_prime` function, check if `num` is less than or equal to 1. If so, return `False` because prime numbers are greater than 1.
3. Use a for loop to iterate from 2 to (num // 2) + 1. You can use the `range` function for this.
4. Inside the loop, check if `num` is divisible evenly by any number between 2 and (num // 2) + 1. If it is, return `False` because `num` is not prime.
5. If the loop completes without finding any divisors, return `True` because `num` is prime.
6. In the main part of your program, prompt the user to enter a positive integer.
7. Use the `input` function to read the user's input and convert it to an integer using the `int` function.
8. Call the `is_prime` function with the entered number as the argument, and assign the result to a variable named `result`.
9. Use an `if` statement to check if `result` is `True`. If it is, print "The number is prime!". Otherwise, print "The number is not prime.".
That's it! Follow these steps to implement the program, and it should be able to check whether a given number is prime or not. Let me know if you have any questions!