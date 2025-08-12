# my_programs.py

def is_inside_circle():
    print("""
def is_inside_circle(x, y, center_x, center_y, radius):
    distance_squared = (x - center_x)**2 + (y - center_y)**2
    return distance_squared <= radius**2
""")
    print("Test Case 1: is_inside_circle(1, 1, 0, 0, 2) => True")
    print("Test Case 2: is_inside_circle(3, 3, 0, 0, 2) => False")
    print("This function uses the distance formula to check if the point lies within the given circle.")


def perimeter_of_rectangle():
    print("""
def perimeter_of_rectangle(length, width):
    return 2 * (length + width)
""")
    print("Test Case 1: perimeter_of_rectangle(5, 3) => 16")
    print("Test Case 2: perimeter_of_rectangle(10, 10) => 40")
    print("The perimeter of a rectangle is calculated using the formula 2*(length + width).")


def to_camel_case():
    print("""
def to_camel_case(s):
    parts = s.strip().split()
    return parts[0].lower() + ''.join(word.capitalize() for word in parts[1:])
""")
    print("Test Case 1: to_camel_case('hello world') => 'helloWorld'")
    print("Test Case 2: to_camel_case('Convert THIS string') => 'convertThisString'")
    print("This function splits the string into words, capitalizes the inner ones, and joins them in camelCase.")


def remove_whitespace():
    print("""
def remove_whitespace(s):
    return ''.join(s.split())
""")
    print("Test Case 1: remove_whitespace('Hello World') => 'HelloWorld'")
    print("Test Case 2: remove_whitespace('  Python  Code ') => 'PythonCode'")
    print("It removes all whitespace characters by splitting the string and joining it back without spaces.")


def divisible_by_3_and_5():
    print("""
def divisible_by_3_and_5(n):
    return n % 3 == 0 and n % 5 == 0
""")
    print("Test Case 1: divisible_by_3_and_5(15) => True")
    print("Test Case 2: divisible_by_3_and_5(10) => False")
    print("This function checks if a number is divisible by both 3 and 5 using modulo operator.")


def generate_random_password():
    print("""
import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))
""")
    print("Test Case 1: generate_password(8) => e.g. 'a8#G2k@1'")
    print("Test Case 2: generate_password(16) => e.g. 'D3@kLm#9vWx$1bZ5'")
    print("Generates a random password of specified length using letters, digits, and symbols.")


def average_of_numbers():
    print("""
def average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0
""")
    print("Test Case 1: average([10, 20, 30]) => 20.0")
    print("Test Case 2: average([5, 15]) => 10.0")
    print("Calculates the average by dividing the sum of numbers by the count of items.")


def check_substring():
    print("""
def contains_substring(main_str, sub_str):
    return sub_str in main_str
""")
    print("Test Case 1: contains_substring('hello world', 'world') => True")
    print("Test Case 2: contains_substring('python', 'java') => False")
    print("Checks if the substring exists in the main string using the `in` operator.")


def replace_vowels():
    print("""
def replace_vowels(s, replacement_char):
    vowels = 'aeiouAEIOU'
    return ''.join(replacement_char if c in vowels else c for c in s)
""")
    print("Test Case 1: replace_vowels('hello', '*') => 'h*ll*'")
    print("Test Case 2: replace_vowels('AEIOU', '-') => '-----'")
    print("Replaces all vowels in the string with a given character using a list comprehension.")


def basic_stopwatch():
    print("""
import time

def stopwatch():
    input("Press Enter to start...")
    start = time.time()
    input("Press Enter to stop...")
    end = time.time()
    print(f"Elapsed time: {end - start:.2f} seconds")
""")
    print("Sample Test 1: Wait 2 seconds before stopping → ~2.00 seconds")
    print("Sample Test 2: Wait 5 seconds before stopping → ~5.00 seconds")
    print("Logic: Measures elapsed time between two Enter key presses using time module.")
