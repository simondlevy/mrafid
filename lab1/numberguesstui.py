"""
Author: Ken Lambert

This program plays a guessing game with the user.  The program
displays a greeting and thinks of a number between 1 and 100.
The user inputs guesses until a guess equals the number.

Usage on command line (default limits are 1 and 100):

python3 numberguesstui.py

python3 numberguesstui.py 50 100

Usage in IDLE (default limits are 1 and 100):

main()

main(50, 100)
"""

import random
import sys
import math

def main(low = 1, high = 100):
    """Default range is 1..100."""
    if len(sys.argv) == 3:
        low = int(sys.argv[1])
        high = int(sys.argv[2])
    print("Good morning, welcome to the game of guess the number!")
    print("I am thinking of a number between %d and %d." % (low, high))
    number = random.randint(low, high)
    count = 0
    maxCount = math.log((low + high - 1), 2)
    while True:
        count += 1
        guess = int(input('Enter your guess: '))
        if guess == number:
            print("You got it in %d tries!" % count)
            break
        elif guess < number:
            print("Sorry, too low!")
        else:
            print("Sorry, too high!")
        if count > maxCount:
            print("You have exceeded the maximum number of tries.")
            break
    print("Have a nice day!")

if __name__ == "__main__":
    main()
           
            
    

    
        
    



    
    
    

