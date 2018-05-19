# implementation of card game - Memory

import simplegui
import random

numbers = range(0, 8) + range(0, 8)
canvas_height = 100
canvas_width = 800
number_of_cards = len(numbers)
grid_width = canvas_width // number_of_cards
exposed = [False] * 16
card_one_index = -1
card_two_index = -1
turns = 0

# helper function to initialize globals
def new_game():
    global state, numbers, exposed, turns
    state = 0
    turns = 0
    random.shuffle(numbers)
    exposed = [False] * 16
    
# define event handlers
def mouseclick(pos):
    global state, card_one_index, card_two_index, turns
    idx = pos[0] // grid_width
    if exposed[idx] == False and state == 0 :
        exposed[idx] = True
        state = 1
        card_one_index = idx
    elif exposed[idx] == False and state == 1:
        exposed[idx] = True
        state = 2
        card_two_index = idx
        turns += 1
    elif exposed[idx] == False and state == 2:
        exposed[idx] = True
        state = 1
        if numbers[card_one_index] != numbers[card_two_index]:
            exposed[card_one_index] = False
            exposed[card_two_index] = False
        card_one_index = idx
        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    line_width = 1
    outline_color = 'White'
    for card in range(number_of_cards):
        if exposed[card]:
            canvas.draw_polygon([(card * grid_width, 0), ((card + 1) * grid_width, 0), ((card + 1) * grid_width, canvas_height), (card * grid_width, canvas_height)], line_width, outline_color, 'Black')
            canvas.draw_text(str(numbers[card]), (15 + card * grid_width, 65), 40, 'White')
        else:
            canvas.draw_polygon([(card * 50, 0), ((card + 1) * grid_width, 0), ((card + 1) * grid_width, canvas_height), (card * grid_width, canvas_height)], line_width, outline_color, 'Green')
    label.set_text("Turns = " + str(turns))   

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")
# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)
# get things rolling
new_game()
frame.start()

