#!/bin/bash

# Define game directory and file names
GAME_DIR="echoes_of_innovation_game"
GAME_FILE="echoes_of_innovation.py"

# Create game directory
echo "Setting up the game directory..."
mkdir -p "$GAME_DIR"

# Move into the game directory
cd "$GAME_DIR"

# Create Python game file
echo "Creating the game script..."
cat <<EOT > "$GAME_FILE"
#!/usr/bin/env python3

# Echoes of Innovation - A text-based adventure game

def start_game():
    print("Welcome to 'Echoes of Innovation: The Quest for Lost Tech'!")
    print("You are Ally Elvis Nzeyimana, a genius software engineer in a futuristic metropolis.")
    print("Your goal is to find the lost technology hidden within an ancient digital artifact.")
    main_menu()

def main_menu():
    print("\\nWhat would you like to do?")
    print("1. Search for the artifact")
    print("2. Visit Dr. Emilia Roche")
    print("3. Fight Victor Kade’s mercenaries")
    print("4. Exit the game")
    
    choice = input("> ")
    
    if choice == "1":
        search_for_artifact()
    elif choice == "2":
        visit_emilia()
    elif choice == "3":
        fight_mercenaries()
    elif choice == "4":
        print("Goodbye, Ally!")
        exit(0)
    else:
        print("Invalid choice. Please select again.")
        main_menu()

def search_for_artifact():
    print("\\nYou begin searching for the artifact in a hidden part of the city.")
    print("As you approach the ancient vault, you must solve a puzzle to enter.")
    puzzle = input("Solve this puzzle (What is 10 + 5?): ")
    
    if puzzle == "15":
        print("Correct! The vault opens, revealing the ancient artifact!")
    else:
        print("Incorrect! You failed to open the vault.")
    
    main_menu()

def visit_emilia():
    print("\\nYou visit Dr. Emilia Roche at her secret lab.")
    print("She helps you decode part of the artifact and gives you a crucial clue.")
    
    print("You now have a lead on Victor Kade’s plans.")
    
    main_menu()

def fight_mercenaries():
    print("\\nVictor Kade’s mercenaries have found you!")
    print("You must defend yourself using advanced tech gadgets.")
    
    fight = input("Do you want to fight (yes or no)?: ").lower()
    
    if fight == "yes":
        print("You defeated the mercenaries using your advanced gadgets!")
    else:
        print("You fled from the battle. Victor Kade gains more power.")
    
    main_menu()

# Start the game
if __name__ == "__main__":
    start_game()
EOT

# Make the Python file executable
chmod +x "$GAME_FILE"

# Inform the user
echo "Game setup complete! To play, run:"
echo "cd $GAME_DIR && ./echoes_of_innovation.py"
