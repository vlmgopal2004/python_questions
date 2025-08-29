import rushi_my_programs as mp

function_map = {
    1: mp.Find_the_Runner_UpScore,
    2: mp.strong_number,
    3: mp.Finding_the_percentage,
    4: mp.number_of_factors,
    5: mp.Calculate_Age_from_DOB,
    6: mp.Find_MOD,
    7: mp.title_case,
    8: mp.square_root,
    9: mp.is_abundant,
    10: mp.diagonal_sum
}
while True:
    print('''
------ FUNCTION MENU ------
1. Find the Runner-Up Score
2. To find the number is Strong number
3. Finding the percentage
4. Count the number of factors of a number
5. Calculate Age from DOB
6. Find MOD(remainder) of two numbers
7. Convert sentence to Title Case
8. Find the Square root of the problem
9. Find the whether the number is Abundant or not
10. Find the sum of the diagonal in a matrix
0. Exit
---------------------------''')
    
    choice = int(input("Enter your choice: "))
    if choice > 0 and choice <= len(function_map):
        function_map[choice]()
    elif choice == 0:
        print("You Exited.")
        break
    else:
        print("❌ Invalid choice. Please try again.")
