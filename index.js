#!/usr/bin/env node

// Echoes of Innovation - Game Entry Point

const readline = require('readline');

// Create an interface to read input and output
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function startGame() {
    console.log("Welcome to 'Echoes of Innovation: The Quest for Lost Tech'!");
    console.log("You are Ally Elvis Nzeyimana, a genius software engineer in a futuristic metropolis.");
    console.log("Your goal is to find the lost technology hidden within an ancient digital artifact.");
    mainMenu();
}

function mainMenu() {
    console.log("\nWhat would you like to do?");
    console.log("1. Search for the artifact");
    console.log("2. Visit Dr. Emilia Roche");
    console.log("3. Fight Victor Kade’s mercenaries");
    console.log("4. Exit the game");
    
    rl.question("> ", (choice) => {
        switch(choice) {
            case "1":
                searchForArtifact();
                break;
            case "2":
                visitEmilia();
                break;
            case "3":
                fightMercenaries();
                break;
            case "4":
                console.log("Goodbye, Ally!");
                rl.close();
                break;
            default:
                console.log("Invalid choice. Please select again.");
                mainMenu();
                break;
        }
    });
}

function searchForArtifact() {
    console.log("\nYou begin searching for the artifact in a hidden part of the city.");
    console.log("As you approach the ancient vault, you must solve a puzzle to enter.");
    
    rl.question("Solve this puzzle (What is 10 + 5?): ", (answer) => {
        if (answer === "15") {
            console.log("Correct! The vault opens, revealing the ancient artifact!");
        } else {
            console.log("Incorrect! You failed to open the vault.");
        }
        mainMenu();
    });
}

function visitEmilia() {
    console.log("\nYou visit Dr. Emilia Roche at her secret lab.");
    console.log("She helps you decode part of the artifact and gives you a crucial clue.");
    console.log("You now have a lead on Victor Kade’s plans.");
    mainMenu();
}

function fightMercenaries() {
    console.log("\nVictor Kade’s mercenaries have found you!");
    console.log("You must defend yourself using advanced tech gadgets.");
    
    rl.question("Do you want to fight (yes or no)?: ", (answer) => {
        if (answer.toLowerCase() === "yes") {
            console.log("You defeated the mercenaries using your advanced gadgets!");
        } else {
            console.log("You fled from the battle. Victor Kade gains more power.");
        }
        mainMenu();
    });
}

// Start the game
startGame();
