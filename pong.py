# Pong by Todd Demone

import simplegui
import random

# initialize globals
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# vertical info for paddles (Integers)
paddle1_pos = HEIGHT / 2
paddle2_pos = HEIGHT / 2
paddle1_vel = 0
paddle2_vel = 0

#ball variables (Lists)
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]

# score variables (Integers)
score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new ball in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel, paddle1_pos, paddle2_pos
    paddle1_pos = HEIGHT / 2
    paddle2_pos = HEIGHT / 2
    ball_pos = [WIDTH / 2, HEIGHT / 2]
        
    if direction == "RIGHT":
        ball_vel[0] = random.randrange(120, 240) / 60.0
    elif direction == "LEFT":
        ball_vel[0] = - random.randrange(120, 240) / 60.0
    
    ball_vel[1] = - random.randrange(60, 180) / 60.0
    print ball_vel
    
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    global score1, score2
    score1 = 0
    score2 = 0
    spawn_ball("RIGHT")

def reset_button():
    return 0
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, ball_pos, ball_vel
    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # update ball 
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # if ball collides with top or bottom wall
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    
    #if ball collides with left or right gutter
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
        if ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT and ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT:
            ball_vel[0] = - ball_vel[0]
        else:
            spawn_ball("RIGHT")
    if ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS:
        if ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT and ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT:
            ball_vel[0] = - ball_vel[0]
        else:
            spawn_ball("LEFT")
        
    #draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
      
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos <= HALF_PAD_HEIGHT and paddle1_vel < 0:
        paddle1_vel = 0
    elif paddle1_pos >= HEIGHT - HALF_PAD_HEIGHT and paddle1_vel > 0:
        paddle1_vel = 0
    else:
        paddle1_pos += paddle1_vel
    
    if paddle2_pos <= HALF_PAD_HEIGHT and paddle2_vel < 0:
        paddle2_vel = 0
    elif paddle2_pos >= HEIGHT - HALF_PAD_HEIGHT and paddle2_vel > 0:
        paddle2_vel = 0
    else:
        paddle2_pos += paddle2_vel
    
    # draw paddles
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT], [HALF_PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos - HALF_PAD_HEIGHT], [WIDTH - HALF_PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT], PAD_WIDTH, "White")
    
    # determine whether paddle and ball collide    
        
    
    
    #draw score
    canvas.draw_text(str(score1), [40, 40], 24, "White")
    canvas.draw_text(str(score2), [WIDTH - 40, 40], 24, "White")

def keydown(key):
    vel = 3
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel -= vel
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel += vel
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel -= vel
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel += vel
    
        
def keyup(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0

# Create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.add_button("Reset", reset_button, 50)

# Start frame
new_game()
frame.start()

