# Rock wins against scissors
# Scissors win aginst paper
# Paper wins against rock

# 0 for rock, 1 for paper, 2 for scissors
import random 

user_choice = int(input("Enter your choice: Type 0 for Rock, 1 for Paper, 2 for scissors: "))
computer_choice = random.randint(0,2)
print("Computer choice is: ", computer_choice)

if user_choice < 0 or user_choice > 2:
    print("Invalid number, you lose.")

elif user_choice == computer_choice:
    print("It's a draw!")

elif computer_choice > user_choice:
    if user_choice == 0 and computer_choice == 2:
        print("User wins!") 
    else:
        print("Computer wins, you lose.")

elif user_choice > computer_choice:
    if user_choice == 2 and computer_choice == 0:
        print("Computer wins, you lose")
    else:
        print("User wins!")




