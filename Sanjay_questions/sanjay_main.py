import sanjay_my_programs

programs = {
    1: sanjay_my_programs.automorphic_number,
    2: sanjay_my_programs.roman_to_integer,
    3: sanjay_my_programs.symmetric_matrix,
    4: sanjay_my_programs.caesar_cipher,
    5: sanjay_my_programs.harshad_number,
    6: sanjay_my_programs.char_frequency,
    7: sanjay_my_programs.extract_domain,
    8: sanjay_my_programs.rectangle_overlap,
    9: sanjay_my_programs.flatten_list,
    10: sanjay_my_programs.count_pos_neg_zero
}

def display_menu():
    print("------ FUNCTION MENU ------")
    print("1. Check Automorphic Number")
    print("2. Convert Roman Numeral to Integer")
    print("3. Check Symmetric Matrix")
    print("4. Caesar Cipher Encryption")
    print("5. Check Harshad Number")
    print("6. Count Character Frequency")
    print("7. Extract Domain from Email")
    print("8. Check Rectangle Overlap")
    print("9. Flatten Nested List")
    print("10. Count Positive, Negative, Zero in List")
    print("0. Exit")
    print("----------------------------")

def main():
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))
        if choice == 0:
            print("Exiting...")
            break
        elif choice in programs:
            programs[choice]()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
