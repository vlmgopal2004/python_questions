import Assignment4 as As

while True:
    print("\n==== Python Function Bank (Part 3) ====")
    print("1. Count Letter Changes")
    print("2. Interleave Two Strings")
    print("3. Longest Same Character Run")
    print("4. Shift Characters by 2")
    print("5. Remove Every Third Character")
    print("6. Reverse Alternate Words")
    print("7. Find Substring Indices")
    print("8. Replace Spaces with Numbers")
    print("9. Check Non-Decreasing Digits")
    print("10. Sum of Vowel Positions")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        mp.count_letter_changes()
    elif choice == "2":
        mp.interleave_two_strings()
    elif choice == "3":
        mp.longest_same_char_run()
    elif choice == "4":
        mp.shift_chars_by_two()
    elif choice == "5":
        mp.remove_every_third_char()
    elif choice == "6":
        mp.reverse_alternate_words()
    elif choice == "7":
        mp.find_substring_indices()
    elif choice == "8":
        mp.replace_spaces_with_numbers()
    elif choice == "9":
        mp.non_decreasing_digits()
    elif choice == "10":
        mp.vowel_position_sum()
    elif choice == "0":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
