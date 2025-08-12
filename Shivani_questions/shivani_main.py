import shivani_my_programs as  my_programs

def show_menu():
    print("\n===== Python Function Bank Menu =====")
    print("1. Check if a Point Lies Inside a Circle")
    print("2. Find the Perimeter of a Rectangle")
    print("3. Convert a String to camelCase")
    print("4. Remove All Whitespace from a String")
    print("5. Check if a Number is Divisible by Both 3 and 5")
    print("6. Generate a Random Password")
    print("7. Find the Average0 of N Numbers")
    print("8. Check if a Substring Exists in a String")
    print("9. Replace All Vowels with a Specific Character")
    print("10. Implement a Basic Stopwatch")
    print("0. Exit")
    print("=====================================")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (0-10): ")

        if choice == "1":
            my_programs.is_inside_circle()
        elif choice == "2":
            my_programs.perimeter_of_rectangle()
        elif choice == "3":
            my_programs.to_camel_case()
        elif choice == "4":
            my_programs.remove_whitespace()
        elif choice == "5":
            my_programs.divisible_by_3_and_5()
        elif choice == "6":
            my_programs.generate_random_password()
        elif choice == "7":
            my_programs.average_of_numbers()
        elif choice == "8":
            my_programs.check_substring()
        elif choice == "9":
            my_programs.replace_vowels()
        elif choice == "10":
            my_programs.basic_stopwatch()
        elif choice == "0":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()




