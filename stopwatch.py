# "Stopwatch: The Game" by Todd Demone

import simplegui

# define global variables
time = 0
is_running = False
total_stops = 0
successful_stops = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    minutes = t / 600
    seconds = t % 600 / 10
    tenths_of_second = t % 10
    
    if seconds < 10:
        seconds = "0" + str(seconds)
    else:
        seconds = str(seconds)

    return str(minutes) + ":" + seconds + "." + str(tenths_of_second)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    global total_stops, successful_stops 
    timer.stop()
    total_stops += 1
    if time % 10 == 0:
        successful_stops += 1

def reset():
    global time, total_stops, successful_stops 
    timer.stop()
    time = 0
    total_stops = 0
    successful_stops = 0
    
# define event handler for timer with 0.1 sec interval
def tick():
    global time 
    time += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(time), (200,250), 40, "Red")
    canvas.draw_text(str(successful_stops) + "/" + str(total_stops), (350,50), 20, "Yellow")
    
# create frame
frame = simplegui.create_frame("Stop Watch", 500, 500)

# register event handlers
timer = simplegui.create_timer(100, tick)
frame.set_draw_handler(draw)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

# start frame
frame.start()

# Please remember to review the grading rubric

