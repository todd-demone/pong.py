# "Guess the number" mini-project
# Coursera - Interactive Python 1 - Week 2b
# By Todd Demone
# June 6, 2017

import simplegui
import random

global guesses_left
global secret_number
global end_of_range_number

# helper function to start and restart the game

def new_game(end_of_range):
    # initialize global variables used in your code here
    global guesses_left
    if end_of_range == 100:
        guesses_left = 7
    else:
        guesses_left = 10
    global secret_number
    secret_number = random.randrange(0, end_of_range)
    # end_of_range_number is used in input_guess() to prevent out of 
    # range guesses as well as to automatically start a new game using 
    # the same parameters as the last game whenever someone wins or runs
    # out of guesses.
    global end_of_range_number
    end_of_range_number = end_of_range
    print
    print "New game. range is [0,", str(end_of_range) + ")"
    print "Number of remaining guesses is", str(guesses_left)
    

# define event handlers for control panel

def range100():
    # button that changes the range to [0,100) and starts a new game 
    new_game(100)
        
def range1000():
    # button that changes the range to [0,1000) and starts a new game 
    new_game(1000)
            
def input_guess(guess):
    global guesses_left
    guess_int = int(guess)
    print
    
    if guess_int >= end_of_range_number or guess_int < 0:
        print "Invalid entry. try again:"
        return 
    
    print "Guess was", guess
    guesses_left = guesses_left - 1
    print "Number of remaining guesses is", str(guesses_left)
    
    if guesses_left == 0 and guess_int != secret_number:
        print "You ran out of guesses. The number was", str(secret_number)
        new_game(end_of_range_number)
        return
        
    if guess_int > secret_number:
        print "Lower!"
    elif guess_int < secret_number:
        print "Higher!"
    else:
        print "Correct!"
        new_game(end_of_range_number)
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)

frame.start()

# call new_game 
new_game(100)


# always remember to check your completed program against the grading rubric
