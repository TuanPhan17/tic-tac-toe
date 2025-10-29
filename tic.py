# ---Starting the game ---
# "Welcome to the Tic-Tac-Toe game!"
# Ask User to input name
# Greet them ... "Hi, Tuan"

#---Will make difficulty levels ---
# Ask user easy, medium , or hard 
# if easy , elif medium , else hard 
# different modes for the game 

#--- will have three option modes depending on difficulty pciked ---

# ---Ask who goes first---
# Ask user "Would you like to go first?" (yes/no)
# User says yes - User goes first
# User says no - comp goes first

# ---Choose a Symbol (x or o)---
# Ask User: "Please choose X or O"
# Convert to Uppercase to keep consistent 
# If user picks X , comp gets O
# If user picks 0 , comp gets 0
# Make sure Input is valid, Keep asking until user enters X or O

# ---Set up game board---
#  Create 3x3 board representing numbers 1-9
# Each number shows an available spot on the board
# Board shall update every time player / comp makes a move

# ---GamePlay---
# Display current Board each turn
# Ask User to pick either 1-9
# Validate Input 
# Must be a number / Within 1-9
# Spot must already not be taken 
# If input invalid / show error and ask again 
# Place users mark on chosen spot 
# Save the move in the text file called tictactoe.txt in format X:5 or 0:2 etc

# If the comp turn 
# For now, computer can choose a random spot 
# We will upgrade it to a rule-based or minimax algorithm to earn extra 20 points 
# Place computers mark and log the move in the same text file.

# ---Results---
# After each turn , check if there's a winner (3 in a row! horizontally, vertically, or diagonall)
# If theres a winner , display the board and print who won 
# ("Congrats 'user' on wining") if won Else ("Comp won sorry 'user' maybe next time!")
# If all spots are filled and there's no winner. It's a draw 
# If it's a draw , program can automatically start a new round till there's a winner. 

# ---END---
# When there's a winner , display 'congrats' or 'computer wins' message 
# Save final state to the file tictactoe.txt
# Ask user if they want to play again 
# If yes , reset board and repeat
# Else , "Thanks for playing!" and end program 

# --- Error Handling ---
# If user enters something invalid (like letters or out of range numbers), program will show and error but will not crash 
# Keep asking for valid input till its correct 

# --- Tic Tac Toe Game Start ---

print("Welcome to the Tic Tac Toe game!")

# Ask for user's name
player_name = input("Please enter your name: ") # get player's name from input

# Greet the user
print(f"Hey {player_name}, let's get ready to play Tic-Tac-Toe!\n") # greet player with name

# Define difficulty options
difficulties = ["Easy", "Medium", "Hard"] # list of difficulty levels

# Display options using a loop
print("Choose a difficulty level:")
for i, level in enumerate(difficulties, start=1):  # loops through list with index starting at 1
    print(f"{i}. {level}")  # prints each difficulty like "1. Easy", "2. Medium", etc.

# Input validation loop
while True: # keeps looping until user gives valid input
    try:
        choice = int(input("Enter a number (1-3): "))  # convert user input to an integer
        if 1 <= choice <= 3:  # check if the number is between 1 and 3
            difficulty = difficulties[choice - 1]  # use chosen number to get difficulty
            break  # exit loop once valid input is entered
        else:
            print("Invalid choice. Please choose a number between 1 and 3.")  # out of range
    except ValueError:
        print("Invalid input. Please enter a number (1-3).")  # if input isn't a number

# --- Clean difficulty confirmation ---
print(f"\nYou selected '{difficulty}' mode. Good luck, {player_name}!")  # confirm choice

# --- Ask who goes first ---
first = ""  # initialize variable to store user's response

print("\nWould you like to go first? (yes/no):")  # show the question once before looping

while True:  # keeps asking until the user gives a valid answer
    first = input().lower()  # get user input and convert it to lowercase for consistency

    if first in ["yes", "y"]:  # check if user typed yes or y
        player_turn = True  # set flag to indicate player goes first
        print("You will go first.")  # confirm choice
        break  # exit loop after valid input

    elif first in ["no", "n"]:  # check if user typed no or n
        player_turn = False  # set flag to indicate computer goes first
        print("The computer will go first.")  # confirm choice
        break  # exit loop after valid input

    else:
        print("Please type 'yes' or 'no':")  # prompt again if input is invalid


# --- Choose a Symbol (X or O) ---
while True:  # keeps looping until valid symbol entered
    player_symbol = input("\nPlease choose your symbol (X or O): ").upper()  # convert to uppercase
    if player_symbol in ["X", "O"]:  # valid choices
        computer_symbol = "O" if player_symbol == "X" else "X"  # assign opposite to computer
        print(f"You chose '{player_symbol}'. The computer will be '{computer_symbol}'.")  # confirm
        break
    else:
        print("Invalid input. Please choose X or O.")  # invalid entry



# --- Set up game board ---
board = [
    ["1", "2", "3"], # row 1
    ["4", "5", "6"], # row 2
    ["7", "8", "9"] # row 3
]

def display_board(board):
    """Prints the Tic Tac Toe board."""
    print("\nCurrent Board:") # print header before showing grid
    for i, row in enumerate(board): # loop through each row , keeping track of index (i)
        print(" | ".join(row)) # join each cell in the row w/ " | " in between 
        if i < 2:  # only print separator for first two rows
            print("-" * 9) # prints "---------" for visual spacing

# 👉 Show the empty grid BEFORE asking for a move
display_board(board) # show the starting 3x3 board (numbers 1–9)

# --- Player move with input validation ---
while True: # loop keeps going until valid move is entered
    move = input("\nPick a number (1-9) to place your move: ") # ask user for a spot number

    # check if input is a number and within range 1–9
    if move.isdigit() and 1 <= int(move) <= 9: 
        move = int(move) # convert from string to integer
        row = (move - 1) // 3  # determine which row (0, 1, 2)
        col = (move - 1) % 3  # determine which column (0, 1, 2)

    # make sure the chosen cell isn't already taken
        if board[row][col] not in ["X", "O"]:
            board[row][col] = player_symbol # place player's symbol on chosen spot
            print(f"\n{player_name} placed '{player_symbol}' on spot {move}.") # confirm move
            display_board(board)  # show updated board
            break # exit the loop after a valid move
        else:
            print("That spot is already taken. Try again.")
    else:
        print("Invalid input. Please enter a number between 1 and 9.")



# --- Difficulty Mode Logic (placeholder for now) ---
if difficulty == "Easy": 
    pass
elif difficulty == "Medium":
    pass
elif difficulty == "Hard":
    pass
