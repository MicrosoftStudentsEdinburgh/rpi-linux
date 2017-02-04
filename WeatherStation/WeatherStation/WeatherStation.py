# Based on https://www.ghielectronics.com/docs/333/fez-hat-and-linux
# and on https://github.com/bechynsky/FEZHATPY
# and on https://bitbucket.org/ghi_elect/windows-iot/src
# and on https://github.com/Gravicode/FezHatBot/blob/master/FezHatBot/

########  Library imports  ######## 
from Adafruit_PWM_Servo_Driver import PWM
from Adafruit_I2C import Adafruit_I2C
from gpiozero import Button
from time import sleep

########  Initializations  ######## 
# Initialise the PWM
pwm = PWM(0x7F)

# Initialise the ADC
adc = Adafruit_I2C(0x48)

# Channel for light sensor on ADC
lightSensorChannel = 5

# Channel for temperature sensor on ADC
tempSensorChannel = 4

# Initialize buttons
button1 = Button(18)
button2 = Button(22)
global button_pressed
button_pressed = False


########  Helper functions  ######## 
def read_from_adc(channel):
   # See details on the protocol on pages 13 and 14 of the ADS7830 ADS:
   # http://ww1.microchip.com/downloads/en/DeviceDoc/20001942F.pdf
   # Usage example:
   # https://github.com/bechynsky/FEZHATPY
   if (channel % 2 == 0):
      c = channel / 2
   else:
      c = (channel - 1) / 2 + 4
   channelAddress = 0x80 | (c << 4)

   return adc.readU8(channelAddress)


def setColor(led, color):
    # Set the selected LED to the selected color
    # Color is encoded as three values for red, green and blue in range 0-255.
    # Each LED has three channels, one for each color.
    # The signals are sent to the corresponding channels as PWM with frequencies calculated by scaling
    # color values from range 0-255 to range 0-4095
	r = int(4096 * float(color[0]) / 255) - 1
	g = int(4096 * float(color[1]) / 255) - 1
	b = int(4096 * float(color[2]) / 255) - 1
	if led == 0:
		# Red channel
		pwm.setPWM(1, 0, r)
		# Green channel
		pwm.setPWM(0, 0, g)
		# Blue channel
		pwm.setPWM(2, 0, b)
	else:
		if led == 1:
			# Red channel
			pwm.setPWM(4, 0, r)
			# Green channel
			pwm.setPWM(3, 0, g)
			# Blue channel
			pwm.setPWM(15, 0, b)


def button_press_handler():
    # Button press handler
    # Implements what happens on button press event
    global button_pressed
    button_pressed = True
    

# Assign button press event handlers
button1.when_pressed = button_press_handler
button2.when_pressed = button_press_handler


########  Colors  ######## 
Color = {'red':			[255, 0, 0],
		 'green':		[0, 255, 0],
		 'blue':		[0, 0, 255],
		 'cyan':		[0, 255, 255],
		 'magenta':		[255, 0, 255],
		 'yellow':		[255, 255, 0],
		 'white':		[255, 255, 255],
		 'black':		[0, 0, 0]}


########  Example code  ######## 
while True:
    # Read the light sensor
    lightLevel = read_from_adc(lightSensorChannel)

    # Read the temperature sensor
    # For details on the formula, see page 8 in http://ww1.microchip.com/downloads/en/DeviceDoc/20001942F.pdf
    temperature = (((3300 / 255) * read_from_adc(tempSensorChannel)) - 400) / 19.5
    if button_pressed:
        # Color.keys() returns the list of color names ('red', 'green', 'blue')
        # This is just a way to access color values by index (0, 1, 2) instead of color name
        # Read more on the data type called dictionary (here Color is a dictionary)
        setColor(0, Color['blue'])
        sleep(1)
        button_pressed = False
    else:
        setColor(0, Color['black'])

########  Main code  ######## 
