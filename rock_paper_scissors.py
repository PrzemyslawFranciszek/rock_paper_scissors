def check_for_input(input_user):
    while True:
        if input_user == 'r' or input_user == 'p' or input_user == 's':
            break
        else:
            input_user = input("You typed wrong key.\n"
                                "Type 'r' for rock, 'p' for paper, 's' for scissors:\n").lower()
    return input_user
player1_win = False
oponent_win = False
def check_for_win(player_choice, oponent_choice):
    if player_choice == 'r' and oponent_choice == 'p':
        oponent_win = True
        print(oponent_win)
    elif player_choice == 'r' and oponent_choice == 's':
        player1_win = True
while True:
    game_mode = input("Welcome in rock paper scissors game. If you want play with another player press 'p',\n"
                      "otherwise if you want to play with computer press 'c', press 'q' to exit:\n").lower()
    if game_mode == 'p':
        print("You choose player vs player")
        player1_choice = check_for_input(input("Player 1. Type 'r' for rock, 'p' for paper, 's' for scissors:\n").lower())
        player2_choice = check_for_input(input("Player 2. Type 'r' for rock, 'p' for paper, 's' for scissors:\n").lower())
        check_for_win(player1_choice, player2_choice)
        print(player1_win)
        print(oponent_win)

    elif game_mode == 'c':
        print("You choose game vs computer")
    elif game_mode == 'q':
        print("Goodbye.")
        break


# def check_for_win():
#     if