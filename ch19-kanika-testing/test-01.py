
# Python Tutorial Link: https://www.youtube.com/watch?v=38svC3U7hVo&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=30

# --------------------------------------

print ('Hello Kanika. This is your first test file!')
print("Hey Kanika, let goooo and learn python !")

# --------------------------------------
# Convert Celsius input to Fahrenheit
try:
    c = float(input("Enter temperature in Celsius: "))
    f = c * 9/5 + 32
    print(f"{c}°C = {f}°F")
except ValueError:
    print("Please enter a valid number.")

# --------------------------------------
# Print all prime numbers between 1 and 50
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    import math
    limit = int(math.sqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True

# --------------------------------------
# Calculate factorial of a number

def factorial(n):
    if n < 0:
        return "Undefined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result  
    
# --------------------------------------  
    # Check if a number is palindrome
def is_palindrome(s):
    s = str(s)
    return s == s[::-1]

# --------------------------------------
# Fibonacci sequence up to n terms
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence     

# --------------------------------------
# Find the largest number in a list
def find_largest(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# --------------------------------------
# Reverse a string
def reverse_string(s):
    return s[::-1]

# --------------------------------------
# Calculate the sum of digits of a number
def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

# --------------------------------------
# Check if a year is a leap year
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
year_input = int(input("Enter a year to check if it's a leap year: "))
if is_leap_year(year_input):
    print(f"{year_input} is a leap year.")
else:
    print(f"{year_input} is not a leap year.")

# --------------------------------------
# Generate a multiplication table for a number
def multiplication_table(n, upto=10):
    table = []
    for i in range(1, upto + 1):
        table.append(f"{n} x {i} = {n * i}")
    return table


# --------------------------------------        
# Check if a string is a pangram
import string
def is_pangram(s):
    alphabet = set(string.ascii_lowercase)
    return alphabet.issubset(set(s.lower()))
test_sentence = input("Enter a sentence to check if it's a pangram: ")
if is_pangram(test_sentence):
    print("It's a pangram.")
else:
    print("It's not a pangram.")

# --------------------------------------
# Find the second largest number in a list
def second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.sort()
    if len(unique_numbers) < 2:
        return None
    return unique_numbers[-2]


# --------------------------------------
# Count vowels in a string
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

# --------------------------------------
# Find the length of a string without using len()
def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

# --------------------------------------
# Check if two strings are anagrams
def are_anagrams(str1, str2):
    return sorted(str1.replace(" ", "").lower()) == sorted(str2.replace(" ", "").lower())
string1 = input("Enter first string for anagram check: ")
string2 = input("Enter second string for anagram check: ")
if are_anagrams(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

# --------------------------------------
# Find the average of a list of numbers
def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


# --------------------------------------
# Check if a number is even or odd
def is_even(n):
    return n % 2 == 0
number_to_check = int(input("Enter a number to check if it's even or odd: "))
if is_even(number_to_check):
    print(f"{number_to_check} is even.")
else:
    print(f"{number_to_check} is odd.")  

# --------------------------------------
# Find the sum of all even numbers in a list
def sum_of_evens(numbers):
    return sum(num for num in numbers if num % 2 == 0)

# --------------------------------------    
# Find the mode of a list of numbers
from collections import Counter
def mode(numbers):
    if not numbers:
        return None
    count = Counter(numbers)
    max_freq = max(count.values())
    modes = [num for num, freq in count.items() if freq == max_freq]
    return modes
num_list_for_mode = [1, 2, 2, 3, 4, 4, 4, 5]
print("Mode(s) of the list:", mode(num_list_for_mode))

# --------------------------------------    
# Check if a number is Armstrong number
def is_armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    total = sum(int(digit) ** num_digits for digit in num_str)
    return total == n
armstrong_number = int(input("Enter a number to check if it's an Armstrong number: "))                  
if is_armstrong(armstrong_number):
    print(f"{armstrong_number} is an Armstrong number.")
else:
    print(f"{armstrong_number} is not an Armstrong number.")

# -------------------------------------- 
    

# Define main function 
if __name__ == "__main__":

    primes = [n for n in range(1, 51) if is_prime(n)]
    print("Primes between 1 and 50:", primes)

    num = int(input("Enter a number to calculate its factorial: "))
    print(f"Factorial of {num} is:", factorial(num)) 

    test_str = input("Enter a string or number to check for palindrome: ")
    if is_palindrome(test_str):
        print(f"{test_str} is a palindrome.")
    else:
        print(f"{test_str} is not a palindrome.")

    terms = int(input("Enter number of terms for Fibonacci sequence: "))
    print("Fibonacci sequence:", fibonacci(terms))    

    num_list = [34, 67, 23, 89, 2, 90, 45]
    print("Largest number in the list:", find_largest(num_list))

    input_str = input("Enter a string to reverse: ")
    print("Reversed string:", reverse_string(input_str))

    number = int(input("Enter a number to sum its digits: "))
    print("Sum of digits:", sum_of_digits(number))

    num_for_table = int(input("Enter a number to generate its multiplication table: "))
    for line in multiplication_table(num_for_table):
        print(line)

    num_list_for_second = [34, 67, 23, 89, 2, 90, 45]
    print("Second largest number in the list:", second_largest(num_list_for_second))  

    input_string_for_vowels = input("Enter a string to count vowels: ")
    print("Number of vowels:", count_vowels(input_string_for_vowels))
  
    input_str_length = input("Enter a string to find its length: ")
    print("Length of the string:", string_length(input_str_length))

    num_list_for_avg = [34, 67, 23, 89, 2, 90, 45]
    print("Average of the list:", average(num_list_for_avg))

    num_list_for_even_sum = [34, 67, 23, 89, 2, 90, 45]
    print("Sum of even numbers in the list:", sum_of_evens(num_list_for_even_sum))
