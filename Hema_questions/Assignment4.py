def count_letter_changes():
    print("""\
# Count how many times consecutive letters change
s = input("Enter a string: ")
count = 0
for i in range(1, len(s)):
    if s[i] != s[i-1]:
        count += 1
print(count)
""")
    print("Test Case 1:\nInput: 'aabbca'\nOutput: 3\n")
    print("Test Case 2:\nInput: 'aaaa'\nOutput: 0\n")
    print("Logic: Compare each character with the previous one and count differences.")

def interleave_two_strings():
    print("""\
# Interleave two strings character by character
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
result = ""
for a, b in zip(s1, s2):
    result += a + b
result += s1[len(s2):] + s2[len(s1):]
print(result)
""")
    print("Test Case 1:\nInput: 'abc', '123'\nOutput: 'a1b2c3'\n")
    print("Test Case 2:\nInput: 'hello', '12'\nOutput: 'h1e2llo'\n")
    print("Logic: Alternate characters from both strings, append leftovers.")

def longest_same_char_run():
    print("""\
# Find longest run of same consecutive character
s = input("Enter a string: ")
max_char = s[0]
max_len = curr_len = 1
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        curr_len += 1
    else:
        if curr_len > max_len:
            max_len = curr_len
            max_char = s[i-1]
        curr_len = 1
if curr_len > max_len:
    max_len = curr_len
    max_char = s[-1]
print(max_char, max_len)
""")
    print("Test Case 1:\nInput: 'aaabbccccd'\nOutput: 'c 4'\n")
    print("Test Case 2:\nInput: 'xyz'\nOutput: 'x 1'\n")
    print("Logic: Track length of consecutive identical characters.")

def shift_chars_by_two():
    print("""\
# Shift every character by 2 ASCII values
text = input("Enter text: ")
shifted = ''.join(chr(ord(c) + 2) for c in text)
print(shifted)
""")
    print("Test Case 1:\nInput: 'abc'\nOutput: 'cde'\n")
    print("Test Case 2:\nInput: 'XYZ'\nOutput: 'Z[\\\\'\n")
    print("Logic: Convert to ASCII, add 2, convert back to character.")

def remove_every_third_char():
    print("""\
# Remove every third character
s = input("Enter a string: ")
result = ''.join(c for i, c in enumerate(s) if (i+1) % 3 != 0)
print(result)
""")
    print("Test Case 1:\nInput: 'abcdefghi'\nOutput: 'abdegh'\n")
    print("Test Case 2:\nInput: 'python'\nOutput: 'pyon'\n")
    print("Logic: Keep only characters whose position is not a multiple of 3.")

def reverse_alternate_words():
    print("""\
# Reverse every alternate word in a sentence
sentence = input("Enter a sentence: ").split()
for i in range(len(sentence)):
    if i % 2 != 0:
        sentence[i] = sentence[i][::-1]
print(" ".join(sentence))
""")
    print("Test Case 1:\nInput: 'hello world python code'\nOutput: 'hello dlrow python edoc'\n")
    print("Test Case 2:\nInput: 'one two three four'\nOutput: 'one owt three ruof'\n")
    print("Logic: Reverse words at odd positions in the list.")

def find_substring_indices():
    print("""\
# Find all indices of a substring in text
text = input("Enter text: ")
sub = input("Enter substring: ")
indices = []
start = 0
while True:
    start = text.find(sub, start)
    if start == -1:
        break
    indices.append(start)
    start += 1
print(indices)
""")
    print("Test Case 1:\nInput: 'banana', 'ana'\nOutput: [1, 3]\n")
    print("Test Case 2:\nInput: 'aaaa', 'aa'\nOutput: [0, 1, 2]\n")
    print("Logic: Use find() repeatedly to locate all occurrences.")

def replace_spaces_with_numbers():
    print("""\
# Replace spaces with increasing numbers
text = input("Enter text: ")
count = 1
result = ""
for char in text:
    if char == " ":
        result += str(count)
        count += 1
    else:
        result += char
print(result)
""")
    print("Test Case 1:\nInput: 'a b c'\nOutput: 'a1b2c'\n")
    print("Test Case 2:\nInput: 'hello world'\nOutput: 'hello1world'\n")
    print("Logic: Replace each space with an incrementing number.")

def non_decreasing_digits():
    print("""\
# Check if number's digits are non-decreasing
num = input("Enter number: ")
is_nd = all(num[i] <= num[i+1] for i in range(len(num)-1))
print(is_nd)
""")
    print("Test Case 1:\nInput: '1234'\nOutput: True\n")
    print("Test Case 2:\nInput: '321'\nOutput: False\n")
    print("Logic: Compare each digit with the next, ensure no decrease.")

def vowel_position_sum():
    print("""\
# Sum of vowel positions in alphabet
vowels = 'aeiou'
word = input("Enter word: ").lower()
total = sum(ord(c) - 96 for c in word if c in vowels)
print(total)
""")
    print("Test Case 1:\nInput: 'abc'\nOutput: 1\n")
    print("Test Case 2:\nInput: 'education'\nOutput: 51\n")
    print("Logic: Map vowels to their positions (a=1, e=5...) and sum.")

