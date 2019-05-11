from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)



#pwm.set_pwm(0, 0, 4000)
#print("sleep 10, 4000")
#time.sleep(10)

#pwm.set_pwm(0, 0, 100) 
#print("sleep 10, 100")
#time.sleep(10)


servo_nrm = 700
for i in range(1,20):
   servo_nrm=servo_nrm+50
   print(servo_nrm)
   pwm.set_pwm(0, 0, servo_nrm)
   time.sleep(1)
