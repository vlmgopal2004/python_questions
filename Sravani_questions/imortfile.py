import assignmnet4 as mp

while True:
    print("\n==== Python Function Bank (Part 2) ====")
    print("1. Find first repeated word in sentence")
    print("2. Generate all two-letter combinations from a word")
    print("3. Replace digits with their squares")
    print("4. Group words by first letter")
    print("5. Reverse only vowels in a string")
    print("6. Duplicate each consonant twice")
    print("7. Find words made only from given letters")
    print("8. Alternate case by word")
    print("9. Sum digits until single digit")
    print("10. Check if two numbers have same set of digits")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        mp.first_repeated_word()
    elif choice == "2":
        mp.two_letter_combinations()
    elif choice == "3":
        mp.replace_digits_with_squares()
    elif choice == "4":
        mp.group_words_by_first_letter()
    elif choice == "5":
        mp.reverse_only_vowels()
    elif choice == "6":
        mp.duplicate_consonants()
    elif choice == "7":
        mp.words_from_given_letters()
    elif choice == "8":
        mp.alternate_case_by_word()
    elif choice == "9":
        mp.sum_digits_until_single()
    elif choice == "10":
        mp.same_digit_set()
    elif choice == "0":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")