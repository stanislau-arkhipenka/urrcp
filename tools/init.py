from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685


pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)


val = 270
pwm.set_pwm(0, 0, val)
pwm.set_pwm(1, 0, val)
time.sleep(1)  # 10


