game = [" "] * 9
turn = 0
player1_moves = []
player2_moves = []

# Take names only once
first = input("Add the first player's name: ").strip()
second = input("Add the second player's name: ").strip()

# Draw the board
def gameplay():
    print()
    for i in range(3):
        row = " " + game[i * 3] + " | " + game[i * 3 + 1] + " | " + game[i * 3 + 2]
        print(row)
        if i < 2:
            print(" --+---+--")
    print()

# Get player input
def current_player(symbol):
    global turn
    try:
        move = int(input(f"{symbol}'s Turn: Enter a number from 0 to 8: "))
        if 0 <= move <= 8 and game[move] == " ":
            game[move] = symbol
            turn += 1
            return move
        else:
            print("Invalid move. Try again.")
            return None
    except ValueError:
        print("Please enter a valid number!")
        return None

# Check for winner
def check_winner():
    lines = [
        game[0] + game[1] + game[2],
        game[3] + game[4] + game[5],
        game[6] + game[7] + game[8],
        game[0] + game[3] + game[6],
        game[1] + game[4] + game[7],
        game[2] + game[5] + game[8],
        game[0] + game[4] + game[8],
        game[2] + game[4] + game[6],
    ]

    for line in lines:
        if line == "XXX":
            print(f"We got our {first} as the winner!!!")
            return True
        elif line == "OOO":
            print(f"We got our {second} as the winner!!!")
            return True
    return False

# Player switching logic
def switch_player():
    global turn
    while turn < 9:
        if turn % 2 == 0:
            move = current_player("X")
            if move is not None:
                player1_moves.append(move)
        else:
            move = current_player("O")
            if move is not None:
                player2_moves.append(move)

        gameplay()

        if check_winner():
            return

    print("Match is a draw... No winner.")

# Game start
def gamestart():
    global game, turn, player1_moves, player2_moves

    # Reset game state
    game = [" "] * 9
    turn = 0
    player1_moves = []
    player2_moves = []

    gameplay()
    switch_player()

    replay = input('Do you wanna try again? (yes/no): ').strip().lower()
    if replay == "yes":
        gamestart()  # ⬅️ recursively restart the game
    else:
        print("Thanks for playing!!")

gamestart()