#!/usr/bin/env python3

# Echoes of Innovation - Updated Text-Based Adventure Game

def start_game():
    print("Welcome to 'Echoes of Innovation: The Quest for Lost Tech'!")
    print("You are Ally Elvis Nzeyimana, a genius software engineer in a futuristic metropolis.")
    print("Your goal is to find the lost technology hidden within an ancient digital artifact.")
    main_menu()

def main_menu():
    print("\nWhat would you like to do?")
    print("1. Search for the artifact")
    print("2. Visit Dr. Emilia Roche")
    print("3. Fight Victor Kade’s mercenaries")
    print("4. Explore the futuristic city")
    print("5. Exit the game")
    
    choice = input("> ")
    
    if choice == "1":
        search_for_artifact()
    elif choice == "2":
        visit_emilia()
    elif choice == "3":
        fight_mercenaries()
    elif choice == "4":
        explore_city()
    elif choice == "5":
        print("Goodbye, Ally!")
        exit(0)
    else:
        print("Invalid choice. Please select again.")
        main_menu()

def search_for_artifact():
    print("\nYou begin searching for the artifact in a hidden part of the city.")
    print("As you approach the ancient vault, you must solve a puzzle to enter.")
    puzzle = input("Solve this puzzle (What is 12 + 8?): ")
    
    if puzzle == "20":
        print("Correct! The vault opens, revealing the ancient artifact!")
        find_clue()
    else:
        print("Incorrect! You failed to open the vault.")
        main_menu()

def find_clue():
    print("\nInside the vault, you find a clue related to the lost technology.")
    print("You now need to decode the clue to proceed.")
    clue = input("Decode this clue (What is 2 * 5 + 3?): ")
    
    if clue == "13":
        print("Clue decoded successfully! You gain access to the next level.")
        level_two()
    else:
        print("Clue decoding failed. Try again.")
        find_clue()

def level_two():
    print("\nYou have entered Level 2 of the game.")
    print("You encounter a security system protecting the artifact.")
    security = input("Disable the security system by solving this (What is 50 - 22?): ")
    
    if security == "28":
        print("Security system disabled. You obtain the artifact!")
        end_game()
    else:
        print("Failed to disable the security system. Try again.")
        level_two()

def visit_emilia():
    print("\nYou visit Dr. Emilia Roche at her secret lab.")
    print("She helps you decode part of the artifact and gives you a crucial clue.")
    print("You now have a lead on Victor Kade’s plans.")
    main_menu()

def fight_mercenaries():
    print("\nVictor Kade’s mercenaries have found you!")
    print("You must defend yourself using advanced tech gadgets.")
    
    fight = input("Do you want to fight (yes or no)?: ").lower()
    
    if fight == "yes":
        print("You defeated the mercenaries using your advanced gadgets!")
        main_menu()
    else:
        print("You fled from the battle. Victor Kade gains more power.")
        main_menu()

def explore_city():
    print("\nExploring the futuristic city reveals new opportunities and challenges.")
    print("You can visit different locations to gather information and resources.")
    print("1. Visit a high-tech store")
    print("2. Go to the city archives")
    print("3. Return to main menu")
    
    choice = input("> ")
    
    if choice == "1":
        visit_store()
    elif choice == "2":
        visit_archives()
    elif choice == "3":
        main_menu()
    else:
        print("Invalid choice. Please select again.")
        explore_city()

def visit_store():
    print("\nAt the high-tech store, you find various gadgets and tools.")
    print("You can purchase items to assist in your quest.")
    item = input("What would you like to buy (scanner, decoder, gadget)?: ").lower()
    
    if item in ["scanner", "decoder", "gadget"]:
        print(f"You purchased a {item}. It will help you in your adventure.")
        explore_city()
    else:
        print("Invalid item. Try again.")
        visit_store()

def visit_archives():
    print("\nIn the city archives, you find historical records and maps.")
    print("These may provide valuable information about the lost technology.")
    print("You gain insights that will help in your quest.")
    explore_city()

def end_game():
    print("\nCongratulations! You've obtained the ancient artifact and uncovered the lost technology.")
    print("You have successfully completed your quest!")
    print("Thank you for playing 'Echoes of Innovation: The Quest for Lost Tech'.")
    exit(0)

# Start the game
if __name__ == "__main__":
    start_game()
