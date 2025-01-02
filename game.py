# Function to display the Tic Tac Toe board
def print_board(board):
    print("\nHere's your game board!")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

# Function to check if a player has won
def check_win(board, player):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(board[pos] == player for pos in combo) for combo in winning_combinations)

# Function to check if the board is full (no more moves left)
def check_full(board):
    return '-' not in board

# Function to get a valid move from the player
def get_move(board, player_name):
    while True:
        try:
            move = int(input(f"{player_name}, where would you like to place your mark? Pick a spot (1-9): ")) - 1
            if move < 0 or move > 8:
                print("Oops! That spot doesn’t exist. Please choose a number between 1 and 9. Try again! 😊")
            elif board[move] != '-':
                print("Uh-oh, that spot is already taken! Pick another one. 😅")
            else:
                return move  # Return the valid move
        except ValueError:
            print("Oops! That wasn’t a number. Please pick a valid number between 1 and 9.")

# Function to save the game state to a file
def save_game(board, moves, result=None):
    with open("game_state.txt", "a") as file:
        file.write("Game Board:\n")
        for i in range(0, 9, 3):
            file.write(f"{board[i]} | {board[i+1]} | {board[i+2]}\n")
        file.write(f"Moves made: {', '.join(moves)}\n")
        if result:
            file.write(f"Game result: {result}\n")
        file.write("-" * 20 + "\n")
    print("🎉 Game saved successfully! You’re awesome! 🎉")

# Function to ask if the players want to play again
def play_again():
    while True:
        replay = input("Would you like to play again? (yes/no): ").lower()
        if replay == "yes":
            return True
        elif replay == "no":
            print("Thanks so much for playing! Hope you had fun! Until next time! 👋")
            return False
        else:
            print("Please type 'yes' or 'no'. 😊")

# Main game function
def play_game():
    print("🎉 Welcome to Tic Tac Toe! 🎉")
    print("Player 1 (X) vs Player 2 (O)\n")
    print("To play, just type a number between 1 and 9 to place your mark. Let’s get started! ✨")

    # Ask for player names
    player1_name = input("\nWhat’s your name, Player 1? (X): ")
    player2_name = input("And you, Player 2? (O): ")

    player_scores = {player1_name: 0, player2_name: 0}
    draw_count = 0  # Count the number of draws

    while True:
        # Initialize the game state
        board = ['-'] * 9
        moves = []
        current_player = 'X'
        current_name = player1_name

        print(f"\nAlright, {player1_name} is X and {player2_name} is O. Let’s do this! 🎲")

        while True:
            print_board(board)  # Show the current board
            print(f"It's {current_name}'s turn! 🙌")
            move = get_move(board, current_name)

            board[move] = current_player
            moves.append(f"{current_name} -> {move + 1}")  # Record the move (1-indexed for readability)

            # Check if the current player has won
            if check_win(board, current_player):
                print_board(board)
                print(f"🎉 Woohoo! {current_name} (Player {current_player}) wins! 🎉 Amazing job! 🏆")
                player_scores[current_name] += 1
                save_game(board, moves, result=f"{current_name} (Player {current_player}) wins!")
                break

            # Check if the board is full (draw condition)
            elif check_full(board):
                print_board(board)
                print("🤝 It's a draw! Both of you were incredible!")
                draw_count += 1
                save_game(board, moves, result="Draw")
                break

            # Switch to the next playerS
            current_player = 'O' if current_player == 'X' else 'X'
            current_name = player2_name if current_name == player1_name else player1_name

        # Display the scores after each game
        print(f"\n🎯 Final Scores: {player1_name}: {player_scores[player1_name]} | {player2_name}: {player_scores[player2_name]} | Draws: {draw_count} 🎯")

        # Ask if they want to play again
        if not play_again():
            break

# Start the game
if __name__ == "__main__":
    play_game()     