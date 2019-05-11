from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()




pwm.set_pwm(0, 0, 1000)
pwm.set_pwm(1, 0, 1000)
#print("sleep 10, 100")
#time.sleep(10)
