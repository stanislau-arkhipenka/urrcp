from device_handlers.dummy.dummy import Dummy
from device_handlers.i2c_pwm_PCA9685.i2c_pwm_PCA9685 import i2c_pwm_PCA9685
from device_handlers.meta_driver import MetaDriver

driver_router = {
    "dummy": Dummy,
    "i2c_pwm_PCA9685": i2c_pwm_PCA9685
}
