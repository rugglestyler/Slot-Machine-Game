import random  # Import the random module to generate random slot symbols

# Constants
MAX_LINES = 3       # Maximum number of lines a user can bet on
MAX_BET = 100       # Maximum bet per line
MIN_BET = 10        # Minimum bet per line
ROWS = 3            # Number of rows in the slot machine
COLS = 3            # Number of columns in the slot machine

# Symbol frequency setup — more symbols mean lower chance of appearing
symbol_count = {
    "A": 2,  # Rarer symbol
    "B": 4,
    "C": 6,
    "D": 8   # Most common symbol
}

# Payout values for matching symbols
symbol_values = {
    "A": 5,  # High payout
    "B": 4,
    "C": 3,
    "D": 2   # Low payout
}

# Function to check if a line is winning
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break  # Not a winning line
        else: 
            winnings += values[symbol] * bet  # All symbols matched
            winning_lines.append(line + 1)    # Store winning line (1-based index)
    return winnings, winning_lines

# Function to simulate a spin of the slot machine
def get_slot_machine_spin(ROWS, COLS, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)

    columns = []
    for _ in range(COLS):
        column = []
        current_symbols = all_symbols[:]  # Copy list for each column
        for _ in range(ROWS):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

# Function to print the slot machine layout
def print_slot_machine(columns):
    ROWS = len(columns[0])
    for row in range(ROWS):
        for i in range(len(columns)):
            symbol = columns[i][row]
            if i != len(columns) - 1:
                print(symbol, end="|")
            else:
                print(symbol, end="")
        print()

# Function to prompt user for deposit
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

# Function to get number of lines to bet on
def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

# Function to get the bet amount per line
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

# Function to handle a single spin round
def spin(balance):
    lines = get_number_of_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount. Your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} line(s). Total bet is: ${total_bet}\n")

    # Generate and print the slot machine result
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)

    # Check winnings
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
    print(f"You won ${winnings}.")
    if winning_lines:
        print("You won on lines:", *winning_lines)
    else:
        print("No winning lines this time.")
    
    return winnings - total_bet  # Net result to apply to balance

# Main game loop
def main():
    balance = deposit()
    
    while True:
        print(f"\nCurrent balance: ${balance}")
        user_input = input("Press Enter to spin (or 'q' to quit): ")
        if user_input.lower() == "q":
            break
        balance += spin(balance)

    print(f"\nYou left with ${balance}. Thanks for playing!")

# Start the game
main()
