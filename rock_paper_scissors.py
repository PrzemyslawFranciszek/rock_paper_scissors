import random
options = {'r':'rock', 'p':'paper', 's':'scissors'}
def check_for_input(input_user):
    while True:
        if input_user in options:
            break
        else:
            input_user = input("You typed wrong key.\n"
                                "Type 'r' for rock, 'p' for paper, 's' for scissors:\n").lower()
    return input_user
def check_for_win(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        print("It's a tie!")
    elif player1_choice == 'r':
        if player2_choice == 'p':
            print("Player1 lose")
        elif player2_choice == 's':
            print("Player1 wins")
    elif player1_choice == 's':
        if player2_choice == 'p':
            print("Player1 wins")
        elif player2_choice == 'r':
            print("Player1 lose")
    elif player1_choice == 'p':
        if player2_choice == 'r':
            print("Player1 wins")
        elif player2_choice == 's':
            print("Player1 lose")
while True:
    game_mode = input("Welcome in rock paper scissors game. If you want to play with another player press 'p',\n"
                      "otherwise if you want to play with computer press 'c', press 'q' to exit:\n").lower()
    if game_mode == 'p':
        print("You choose player vs player")
        player1_choice = check_for_input(input("Player 1. Type 'r' for rock, 'p' for paper, 's' for scissors:\n").lower())
        player2_choice = check_for_input(input("Player 2. Type 'r' for rock, 'p' for paper, 's' for scissors:\n").lower())
        print(f"Player1 choiced {options[player1_choice]}, player2 choiced {options[player2_choice]}")
        check_for_win(player1_choice, player2_choice)
    elif game_mode == 'c':
        print("You choose game vs computer")
        player1_choice = check_for_input(input("Player 1. Type 'r' for rock, 'p' for paper, 's' for scissors:\n").lower())
        player2_choice = random.choice(list(options))
        print(f"Player1 choiced {options[player1_choice]}, computer choiced {options[player2_choice]}")
        check_for_win(player1_choice, player2_choice)
    elif game_mode == 'q':
        print("Goodbye.")
        break
    continue_game = input("Press y to play again:\n").lower()
    if continue_game != 'y':
        break
