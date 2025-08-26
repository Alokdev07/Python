import random

def game():
    print("0 -> Stone \n1 -> Paper \n2 -> Scissor")
    user_input = int(input("Enter an option: "))
    game_element_list = ('Stone', 'Paper', 'Scissor')
    computer_selection = random.randint(0, 2)

    print(f"\nYou chose: {game_element_list[user_input]}")
    print(f"Computer chose: {game_element_list[computer_selection]}\n")

    
    if user_input == computer_selection:
        print("It's a Draw!")

    
    elif user_input == 0 and computer_selection == 1:
        print("Paper covers Stone → You Lose!")
    elif user_input == 0 and computer_selection == 2:
        print("Stone breaks Scissor → You Win!")

   
    elif user_input == 1 and computer_selection == 0:
        print("Paper covers Stone → You Win!")
    elif user_input == 1 and computer_selection == 2:
        print("Scissor cuts Paper → You Lose!")

    
    elif user_input == 2 and computer_selection == 0:
        print("Stone breaks Scissor → You Lose!")
    elif user_input == 2 and computer_selection == 1:
        print("Scissor cuts Paper → You Win!")

game()
