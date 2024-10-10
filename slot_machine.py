import random

# Setting constant number of maximum number of lines, maximum and minimum bet
MAX_LINES = 3 
MAX_BET = 100
MIN_BET = 1

# Number of rows and columns in our slot machine (3x3)
ROWS = 3
COLS = 3

# Dictionary of symbols available for each column (2As, 4Bs etc)
symbol_count = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}

# The value of each symbol - determinant of the winnings - the rarer the sign, the more it is worth
symbol_value = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 2
}

# Function to define winnings and on which lines there was a win
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)

    return winnings, winnings_lines

# Function to get the slot machine spin (drawing random symbols from symbol_count into the slot matrix 3x3)
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    # Iterating over key, value in dictionary.items() to add them to the list of all available symbols
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:] # to make a copy, without affecting the original
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

# Function to transpose columns and see the result of slot machine's spin
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = ' | ')
            else:
                print(column[row], end = '')
        
        print()

# Function to ask the user for the deposit amount (must be a positive digit - we cannot bet having $0)
def deposit():
    while True:
        amount = input ('What would you like to deposit? $')
        if amount.isdigit(): 
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be greater than 0.')
        else:
            print('Please enter a number.')
    return amount

# Function to ask the user for the number of lines she/he wants to bet on
def get_number_of_lines():
    while True:
        lines = input ('Enter the number of lines to bet on (1-' + str(MAX_LINES) + ')? ')
        if lines.isdigit(): 
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print('Enter a valid number of lines')
        else:
            print('Please enter a number.')
    return lines  

# Function to ask the user for the amount she/he wants to bet on each line (same for every line)
def get_bet():
    while True:
        amount = input ('What would you like to bet on each line? $')
        if amount.isdigit(): 
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'Amount must be between ${MIN_BET} - ${MAX_BET}.')
        else:
            print('Please enter a number.')
    return amount

# Function to check if the user's total bet does not exceed their available balance
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f'You do not have enough to bet that amount, your current balance is: ${balance}.')
        else:
            break
    print(f'You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}.')
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winnings_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f'You won ${winnings}.')
    print(f'You won on lines:', *winnings_lines)
    return winnings - total_bet

# Running the slot machine
def main():
    balance = deposit() # kind like a start of a program
    while True:
        print(f"Current balance is ${balance}.")
        answer = input("Press enter to play (q to quit).")
        if answer == 'q':
            break
        balance += spin(balance)

    print(f'You left with ${balance}.')

# Ok, let's play the game
main()
