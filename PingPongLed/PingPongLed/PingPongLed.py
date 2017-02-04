from gpiozero import LED, Button
from time import sleep

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

print("LED 0")
led0.on()
sleep(sleep_duration)
led0.off()

# Game loop
while sleep_duration >= 0:
    print("LED 1")
    led1.on()
    sleep(sleep_duration)
    led1.off()

    print("LED 2")
    led2.on()
    sleep(sleep_duration)
    led2.off()

    print("LED 3")
    led3.on()
    sleep(sleep_duration)
    led3.off()

    print("LED 4")
    led4.on()
    sleep(sleep_duration)
    led4.off()

    # Prepare for player 1 button press
    button1_pressed = False
    print("LED 5")
    led5.on()
    sleep(sleep_duration)
    led5.off()
    
    if not button1_pressed:
        # button1_press_handler() was not triggerred by the button press event
        player1_misses = player1_misses + 1
        print("------------------MISS by player 1------------------")
    print("Misses: P1(" + str(player1_misses) + ")  P2(" + str(player2_misses) + ")")

    print("LED 4")
    led4.on()
    sleep(sleep_duration)
    led4.off()

    print("LED 3")
    led3.on()
    sleep(sleep_duration)
    led3.off()

    print("LED 2")
    led2.on()
    sleep(sleep_duration)
    led2.off()

    print("LED 1")
    led1.on()
    sleep(sleep_duration)
    led1.off()

    # Prepare for player 2 button press
    button2_pressed = False
    print("LED 0")
    led0.on()
    sleep(sleep_duration)
    led0.off()
    
    if not button2_pressed:
        # button2_press_handler() was not triggerred by the button press event
        player2_misses = player2_misses + 1
        print("------------------MISS by player 2------------------")
    print("Misses: P1(" + str(player1_misses) + ")  P2(" + str(player2_misses) + ")")

    # Speed up
    sleep_duration = sleep_duration - speedup_by
    if sleep_duration >= 0:
        print("Speedup! New pause duration: " + str(sleep_duration) + " s")