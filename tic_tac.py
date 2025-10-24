# ---Starting the game ---
# "Welcome to the Tic-Tac-Toe game!"
# Ask User to input name
# Greet them ... "Hi, Tuan"

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