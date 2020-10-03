""" Rock Paper Scissors
----------------------------------------
"""

# import libraries
import random
import os
import re

# validate to clean up the console
os.system('cls' if os.name=='nt' else 'clear')

while (1 < 2):
    print ("\n")
    print ("Rock 🗿, Paper 🧻, Scissors 🔪 - Shoot! ")
    userChoice = input("Choose your weapon [R]ock], [P]aper, or [S]cissors: ")
    # validate if the input character is valid
    if not re.match("[SsRrPp]", userChoice):
        print ("Please choose a letter:")
        print ("[R]ock, [S]cissors or [P]aper.")
        continue
    # Print the user's choice
    print ("You chose: " + userChoice)
    choices = ['R', 'P', 'S']
    # generates a random value
    opponentChoice = random.choice(choices)
    print ("I chose: " + opponentChoice)
    # validating possible scenarios
    if opponentChoice == str.upper(userChoice):
        print ("Tie! 🤝  ")
    elif opponentChoice == 'R' and userChoice.upper() == 'S':      
        print ("Scissors beats rock, I win! 🤗 ")
        continue
    elif opponentChoice == 'S' and userChoice.upper() == 'P':      
        print ("Scissors beats paper! I win! 🤗 ")
        continue
    elif opponentChoice == 'P' and userChoice.upper() == 'R':      
        print ("Paper beat rock, I win! 🤗 ")
        continue
    else:       
        print ("You win! 💯")