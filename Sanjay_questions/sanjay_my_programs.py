def automorphic_number():
    print("Program: Automorphic Number")
    print('''\
def automorphic(n):
    return str(n * n).endswith(str(n))

# Test Cases
print(automorphic(5))   # Output: True
print(automorphic(76))  # Output: True
print(automorphic(7))   # Output: False
''')
    print("Explanation: A number is Automorphic if its square ends with the number itself.\n")


def roman_to_integer():
    print("Program: Roman Numeral to Integer")
    print('''\
def roman_to_int(s):
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    prev = 0
    for char in reversed(s):
        if values[char] < prev:
            total -= values[char]
        else:
            total += values[char]
        prev = values[char]
    return total

# Test Cases
print(roman_to_int("III"))   # Output: 3
print(roman_to_int("IX"))    # Output: 9
print(roman_to_int("LVIII")) # Output: 58
print(roman_to_int("MCMXCIV")) # Output: 1994
''')
    print("Explanation: Converts a Roman numeral into an integer using subtraction rules.\n")


def symmetric_matrix():
    print("Program: Symmetric Matrix Check")
    print('''\
def is_symmetric(matrix):
    rows = len(matrix)
    for i in range(rows):
        for j in range(rows):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

# Test Cases
print(is_symmetric([[1,2,3],[2,1,4],[3,4,1]])) # Output: True
print(is_symmetric([[1,0],[1,1]])) # Output: False
''')
    print("Explanation: A square matrix is symmetric if it's equal to its transpose.\n")


def caesar_cipher():
    print("Program: Caesar Cipher Encryption")
    print('''\
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

# Test Cases
print(caesar_encrypt("Hello World", 3)) # Output: Khoor Zruog
''')
    print("Explanation: Shifts each letter in the string by the given number of positions.\n")


def harshad_number():
    print("Program: Harshad Number")
    print('''\
def harshad(n):
    return n % sum(int(d) for d in str(n)) == 0

# Test Cases
print(harshad(18))  # Output: True
print(harshad(21))  # Output: True
print(harshad(19))  # Output: False
''')
    print("Explanation: A number is Harshad if it is divisible by the sum of its digits.\n")


def char_frequency():
    print("Program: Character Frequency in a String")
    print('''\
def char_freq(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

# Test Cases
print(char_freq("hello")) # Output: {'h':1,'e':1,'l':2,'o':1}
''')
    print("Explanation: Counts how many times each character appears in the string.\n")


def extract_domain():
    print("Program: Extract Domain from Email")
    print('''\
def extract_domain(email):
    return email.split('@')[-1]

# Test Cases
print(extract_domain("user@example.com")) # Output: example.com
''')
    print("Explanation: Splits the email at '@' and returns the domain part.\n")


def rectangle_overlap():
    print("Program: Rectangle Overlap Check")
    print('''\
def rectangles_overlap(r1, r2):
    # r1 and r2 are tuples: (x1, y1, x2, y2)
    if r1[0] >= r2[2] or r2[0] >= r1[2]:
        return False
    if r1[1] >= r2[3] or r2[1] >= r1[3]:
        return False
    return True

# Test Cases
print(rectangles_overlap((0,0,2,2),(1,1,3,3))) # Output: True
print(rectangles_overlap((0,0,1,1),(2,2,3,3))) # Output: False
''')
    print("Explanation: Two rectangles overlap if they share any area.\n")


def flatten_list():
    print("Program: Flatten Nested List")
    print('''\
def flatten(nested_list):
    flat = []
    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten(item))
        else:
            flat.append(item)
    return flat

# Test Cases
print(flatten([1, [2, [3, 4], 5], 6])) # Output: [1, 2, 3, 4, 5, 6]
''')
    print("Explanation: Recursively flattens any nested lists into a single list.\n")


def count_pos_neg_zero():
    print("Program: Count Positive, Negative, Zero in List")
    print('''\
def count_numbers(lst):
    pos = sum(1 for x in lst if x > 0)
    neg = sum(1 for x in lst if x < 0)
    zero = sum(1 for x in lst if x == 0)
    return pos, neg, zero

# Test Cases
print(count_numbers([1, -2, 0, 4, -5])) # Output: (2, 2, 1)
''')
    print("Explanation: Counts how many numbers are positive, negative, or zero.\n")
