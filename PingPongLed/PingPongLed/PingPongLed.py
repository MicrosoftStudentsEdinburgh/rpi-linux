########  Library imports  ######## 
from gpiozero import LED, Button
from time import sleep

########  Initializations  ######## 
# Initialize LEDs
led0 = LED(18)
led1 = LED(23)
led2 = LED(24)
led3 = LED(25)
led4 = LED(8)
led5 = LED(7)

# Reset LEDs
led0.off()
led1.off()
led2.off()
led3.off()
led4.off()
led5.off()

# Button press handlers
def button1_press_handler():
    global button1_pressed
    button1_pressed = True

def button2_press_handler():
    global button2_pressed
    button2_pressed = True

# Initialize buttons
button1 = Button(15)
button2 = Button(14)
global button1_pressed
global button2_pressed

# Assign button press event handlers
button1.when_pressed = button1_press_handler
button2.when_pressed = button2_press_handler

# Initialize score
player1_misses = 0
player2_misses = 0

sleep_duration = 1  # Seconds
speedup_by = 0.1    # Seconds


########  Example code  ######## 
while (True):
    led3.on()
    sleep(0.5)
    led3.off()    
    
    if button2_pressed:
        # button2_press_handler() was triggerred by the button press event
        print("------------------Button 2 pressed------------------")

########  Game implementation  ######## 
