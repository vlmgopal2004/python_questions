while True:
    print("Function MENU:")
    print("0.Exit")
    print("1. Reverse Every Word in a Sentence")
    print("2. Print Emoji Right Angle Triangle")
    print("3. Convert Decimal to Binary (without bin())")
    print("4. Number of Days Between Two Dates")
    print("5. Python Program to Find Largest element in an Array")
    print("6. Count the Number of Matching Characters in a Pair of Strings")
    print("7. Generate a Table of Squares")
    print("8. Check if Binary Representations of Two Numbers are Anagrams")
    print("9. Sort a List of Tuples by Second Item")
    print("10. Printing Alphabet 'D' Star Pattern with Integer Input as Rows Length")
    print()
    ch= int(input("Select your Program: "))
    if ch==0:
        break

    elif ch == 1:
        from gopi_my_programs import reverse_wrd
        reverse_wrd()

    elif ch == 2:
        from gopi_my_programs import emoji
        emoji()

    elif ch == 3:
        from gopi_my_programs import dec_bin
        dec_bin()

    elif ch == 4:
        from gopi_my_programs import date_diff
        date_diff()

    elif ch == 5:
        from gopi_my_programs import large_ele
        large_ele()

    elif ch == 6:
        from gopi_my_programs import count_matches
        count_matches()

    elif ch == 7:
        from gopi_my_programs import sqrs
        sqrs()

    elif ch == 8:
        from gopi_my_programs import bin_anagram
        bin_anagram()

    elif ch == 9:
        from gopi_my_programs import sort_tuple
        sort_tuple()

    elif ch == 10:
        from gopi_my_programs import pattern
        pattern()

    else:
        print("Invalid choice. Please select from 1-10.")