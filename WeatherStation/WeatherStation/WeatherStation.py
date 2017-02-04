#!/usr/bin/python
# Based on https://www.ghielectronics.com/docs/333/fez-hat-and-linux
# and on https://github.com/bechynsky/FEZHATPY
# and on https://bitbucket.org/ghi_elect/windows-iot/src
# and on https://github.com/Gravicode/FezHatBot/blob/master/FezHatBot/

from Adafruit_PWM_Servo_Driver import PWM
from Adafruit_I2C import Adafruit_I2C
import RPi.GPIO as GPIO

# Initialise the PWM
pwm = PWM(0x7F)

# Initialise the ADC
adc = Adafruit_I2C(0x48)

# Channel for light sensor on ADC
lightSensorChannel = 5

# Channel for temperature sensor on ADC
tempSensorChannel = 4

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

Color = {'red':			[255, 0, 0],
		 'green':		[0, 255, 0],
		 'blue':		[0, 0, 255],
		 'cyan':		[0, 255, 255],
		 'magenta':		[255, 0, 255],
		 'yellow':		[255, 255, 0],
		 'white':		[255, 255, 255],
		 'black':		[0, 0, 0]}

while (True):
   # Read the light sensor
   lightLevel = read_from_adc(lightSensorChannel)
   
   # Read the temperature sensor
   # For details on the formula, see page 8 in http://ww1.microchip.com/downloads/en/DeviceDoc/20001942F.pdf
   temperature = (((3300 / 255) * read_from_adc(tempSensorChannel)) - 400) / 19.5

   print "Light level is " + str(lightLevel) + "  Temperature is " + str(temperature) + " C"
   if lightLevel < 100:
      setColor(0, Color['magenta'])
      setColor(1, Color['cyan'])
   else:
      setColor(0, Color['black'])
      setColor(1, Color['black'])
