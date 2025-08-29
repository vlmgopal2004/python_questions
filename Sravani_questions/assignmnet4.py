def first_repeated_word():
    print("""\
# Find first repeated word in sentence
words = input("Enter sentence: ").split()
seen = set()
result = "No repeated word"
for w in words:
    if w in seen:
        result = w
        break
    seen.add(w)
print(result)
""")
    print("Test Case 1:\nInput: 'this is a test this'\nOutput: 'this'\n")
    print("Test Case 2:\nInput: 'no repeat here'\nOutput: 'No repeated word'\n")
    print("Logic: Track seen words, stop when a repeat is found.")

def two_letter_combinations():
    print("""\
# Generate all two-letter combinations from a word
word = input("Enter word: ")
combinations = []
for i in range(len(word)):
    for j in range(i+1, len(word)):
        combinations.append(word[i] + word[j])
print(combinations)
""")
    print("Test Case 1:\nInput: 'abc'\nOutput: ['ab', 'ac', 'bc']\n")
    print("Test Case 2:\nInput: 'abcd'\nOutput: ['ab', 'ac', 'ad', 'bc', 'bd', 'cd']\n")
    print("Logic: Nested loops to form letter pairs.")

def replace_digits_with_squares():
    print("""\
# Replace digits with their squares
text = input("Enter text: ")
result = ""
for c in text:
    if c.isdigit():
        result += str(int(c)**2)
    else:
        result += c
print(result)
""")
    print("Test Case 1:\nInput: 'a2b3'\nOutput: 'a4b9'\n")
    print("Test Case 2:\nInput: 'x5y0'\nOutput: 'x25y0'\n")
    print("Logic: Check if character is digit, replace with its square.")

def group_words_by_first_letter():
    print("""\
# Group words by first letter
words = input("Enter words: ").split()
groups = {}
for w in words:
    first = w[0]
    groups.setdefault(first, []).append(w)
print(groups)
""")
    print("Test Case 1:\nInput: 'apple ant bat'\nOutput: {'a': ['apple', 'ant'], 'b': ['bat']}\n")
    print("Test Case 2:\nInput: 'dog deer cat'\nOutput: {'d': ['dog', 'deer'], 'c': ['cat']}\n")
    print("Logic: Use dictionary to group words by starting letter.")

def reverse_only_vowels():
    print("""\
# Reverse only vowels in a string
s = list(input("Enter string: "))
vowel_indices = [i for i, c in enumerate(s) if c.lower() in 'aeiou']
vowels = [s[i] for i in vowel_indices][::-1]
for idx, vi in enumerate(vowel_indices):
    s[vi] = vowels[idx]
print("".join(s))
""")
    print("Test Case 1:\nInput: 'education'\nOutput: 'odacutien'\n")
    print("Test Case 2:\nInput: 'hello'\nOutput: 'holle'\n")
    print("Logic: Reverse the order of vowels, keep consonants in place.")

def duplicate_consonants():
    print("""\
# Duplicate each consonant twice
s = input("Enter string: ")
result = ""
for c in s:
    if c.lower() not in 'aeiou':
        result += c*2
    else:
        result += c
print(result)
""")
    print("Test Case 1:\nInput: 'cat'\nOutput: 'ccaatt'\n")
    print("Test Case 2:\nInput: 'dog'\nOutput: 'ddoog'\n")
    print("Logic: Double consonants, keep vowels as they are.")

def words_from_given_letters():
    print("""\
# Find words made only from given letters
sentence = input("Enter sentence: ").split()
letters = set(input("Enter allowed letters: "))
valid_words = [w for w in sentence if set(w) <= letters]
print(valid_words)
""")
    print("Test Case 1:\nInput: 'bat cat rat', 'atc'\nOutput: ['cat']\n")
    print("Test Case 2:\nInput: 'see bee', 'esb'\nOutput: ['see', 'bee']\n")
    print("Logic: Check if all letters in word are from allowed set.")

def alternate_case_by_word():
    print("""\
# Alternate case by word
words = input("Enter sentence: ").split()
for i in range(len(words)):
    if i % 2 == 0:
        words[i] = words[i].lower()
    else:
        words[i] = words[i].upper()
print(" ".join(words))
""")
    print("Test Case 1:\nInput: 'one two three four'\nOutput: 'one TWO three FOUR'\n")
    print("Test Case 2:\nInput: 'a b c d'\nOutput: 'a B c D'\n")
    print("Logic: Lowercase even-index words, uppercase odd-index words.")

def sum_digits_until_single():
    print("""\
# Sum digits until single digit
n = int(input("Enter number: "))
while n >= 10:
    n = sum(int(d) for d in str(n))
print(n)
""")
    print("Test Case 1:\nInput: 987\nOutput: 6\n")
    print("Test Case 2:\nInput: 12345\nOutput: 6\n")
    print("Logic: Repeatedly sum digits until one digit remains.")

def same_digit_set():
    print("""\
# Check if two numbers have same set of digits
n1 = input("Enter first number: ")
n2 = input("Enter second number: ")
print(set(n1) == set(n2))
""")
    print("Test Case 1:\nInput: 1123, 3211\nOutput: True\n")
    print("Test Case 2:\nInput: 112, 345\nOutput: False\n")
    print("Logic: Compare sets of digits from both numbers.")