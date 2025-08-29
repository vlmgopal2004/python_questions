def Find_the_Runner_UpScore():
    print("🧠 Program: Find the Runner-Up Score\n")
    print("📄 Code:")
    print('''\

n = int(input())
scores= list(map(int, input().split()))
unique_scores=list(set(scores))
unique_scores.sort(reverse=True)
print(unique_scores[1])

🧪 Test Cases:
Input : 7
        4 7 5 7 6 8 2
Output : 7
Input : 5
        3 4 5 5 2
Output : 4

📝 Explanation:This program takes no.of students marks as list and from list takes unique values in descending order based on index value gives output.
''')

def strong_number():
    print("🧠 Program: To find the number is Strong number \n")
    print("📄 Code:")
    print('''

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def is_strong(num):
    total = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        total += factorial(digit)
        temp //= 10
    return total == num

n = int(input("Enter a number: "))
if is_strong(n):
    print(f"{n} is a Strong Number")
else:
    print(f"{n} is NOT a Strong Number")

🧪 Test Cases:
Input : Enter the number : 145
Output : 145 is Strong Number.

Input : Enter the number : 172
Output : 145 is NOT a Strong Number.

📝 Explanation :This Program checks a number that equals the sum of the factorials of its digits then it returns as Strong Number.

''')

def Finding_the_percentage():
    print("🧠 Program: Finding the percentage \n")
    print("📄 Code:")
    print('''
    
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_scores = student_marks[query_name]
    average = sum(query_scores)/len(query_scores)
    
    print(f"{average:.2f}")

🧪 Test Cases:
Input: 3
       Raj 75 86 65
       Veer 78 89 57
       Shilpa 40 70 95
Output: Shilpa 68.33

📝 Explanation:This program takes marks and Uses Average Formula and returns percentage.
''')

def number_of_factors():
    print("🧠 Program: Count the number of factors of a number \n")
    print("📄 Code:")
    print('''

def count_factors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:   # if i divides n perfectly
            count += 1
    return count

# Main program
num = int(input("Enter a number: "))
print(f"Total factors of {num}: {count_factors(num)}")

🧪 Test Cases:
Input : Enter a number: 7
Output : Total factors of 7: 2

Input : Enter a number: 36
Output : Total factors of 36: 9

📝 Explanation:This program takes a number and Counts the noof factors of that number.

''')

def Calculate_Age_from_DOB():
    print("🧠 Program: Calculate Age from DOB\n")
    print("📄 Code:")
    print('''

from datetime import datetime

dob = input("Enter your DOB (dd-mm-yyyy): ")
dob_date = datetime.strptime(dob, "%d-%m-%Y")
today = datetime.today()

age = today.year - dob_date.year
if (today.month, today.day) < (dob_date.month, dob_date.day):
    age -= 1

print("Your age is:", age)

🧪 Test Cases:
Input : Enter your DOB (dd-mm-yyyy): 26-06-2004
Output : Your age is: 21

Input : Enter your DOB (dd-mm-yyyy): 01-04-1998
Output : Your age is: 27

📝 Explanation :This program takes date of birth as input and finds your age by importing datetime.
''')

def Find_MOD():
    print("🧠 Program: Find to find MOD(remainder) of two numbers\n")
    print("📄 Code:")
    print('''

# Function to find MOD (remainder) of two numbers
def mod(a, b):
    return a % b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = mod(num1, num2)
print(f"MOD({num1}, {num2}) = {result}")

🧪 Test Cases:
Input: 72, 4 → Output: MOD is 0
Input: 98, 4 → Output: MOD is 2

📝 Explanation:
This program uses the Euclidean algorithm. It repeatedly replaces a with b and b with a % b until b becomes 0. The remaining value in a is the GCD.

''')

def title_case():
    print("🧠 Program: Convert sentence to Title Case \n")
    print("📄 Code:")
    print('''
text = input("Enter a sentence: ")
title_case = text.title()
print("Title Case:", title_case)

🧪 Test Cases:
Input : Enter a sentence: PyThOn Is FuN
Output : Title Case: Python Is Fun

Input : PYTHON learn IN codegnan
Output : Title Case: Python Learn In Codegnan

📝 Explanation: This program takes the sentence with Capital and small and converts the sentence into Title.
''')

def square_root():
    print("🧠 Program: Find the Square root of the problem \n")
    print("📄 Code:")
    print('''
import math

def find_square_root(num):
    return math.sqrt(num)

# Input
n = float(input("Enter a number: "))

# Function call & Output
print(f"Square root of {n} is {find_square_root(n):.2f}")

🧪 Test Cases:
Input : Enter a number: 14
Output : Square root of 14.0 is 3.74
Input : Enter a number: 73
Output : Square root of 73.0 is 8.54

📝 Explanation:This program Finds the square root of a number upto 2 decimals
''')

def is_abundant():
    print("🧠 Program: Find the whether the number is Abundant or not \n")
    print("📄 Code:")
    print('''
def is_abundant(num):
    total = 0
    for i in range(1, num):
        if num % i == 0:
            total += i
    return total > num

number = int(input("Enter a number: "))

if is_abundant(number):
    print(f"{number} is an Abundant Number")
else:
    print(f"{number} is NOT an Abundant Number")


🧪 Test Cases:
Input : Enter a number: 55
Output : 8 is NOT an Abundant Number
Input : Enter a number: 12
Output : 25 is an Abundant Number

📝 Explanation: This program detects whether the input number and output end number is same
''')

def diagonal_sum():
    print("🧠 Program: Find the sum of the diagonal in a matrix \n")
    print("📄 Code:")
    print('''
def diagonal_sum(matrix):
    total = 0
    for i in range(len(matrix)):
        total += matrix[i][i]
    return total

n = int(input("Enter size of square matrix: "))
matrix = []
print("Enter matrix elements:")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

print(f"Sum of main diagonal: {diagonal_sum(matrix)}")

🧪 Test Cases:
Input :Enter size of square matrix: 3
       Enter matrix elements:
       1 5 6
       7 3 4
       9 2 8
Output :Sum of main diagonal: 12

Input :Enter size of square matrix: 5
       Enter matrix elements:
       1 4 7 9 2
       4 3 7 5 6
       7 2 8 3 6
       3 8 2 9 4
       8 3 9 2 1
Output :Sum of main diagonal: 22

📝 Explanation:This program takes the diagonal of a matrix and calculates the sum of the diagonal.

''')


    
