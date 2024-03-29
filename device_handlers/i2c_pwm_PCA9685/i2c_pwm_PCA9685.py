from __future__ import division
import logging
import Adafruit_PCA9685
from device_handlers.meta_driver import MetaDriver

logger = logging.getLogger(__name__)


class i2c_pwm_PCA9685(MetaDriver):

    pwm = None

    def __init__(self, device_config):

        super(i2c_pwm_PCA9685, self).__init__()
        assert isinstance(device_config, dict), "device_config should be instance of dict"

        self.dev_id = device_config.get("id", 0)
        self.null_pos_on = device_config.get("null_pos_on", 0)
        self.null_pos_off = device_config.get("null_pos_off", 270)

        if not self.pwm:
            self.pwm = Adafruit_PCA9685.PCA9685()
            self.pwm.set_pwm_freq(device_config.get("pwm_freq", 50))
            logger.info("PCA9685 initiated")
        self.pwm.set_pwm(self.dev_id, self.null_pos_on, self.null_pos_off)

    def set_device_double_value(self, value):
        int_value = int(self.null_pos_off + round(value))
        self.pwm.set_pwm(self.dev_id, self.null_pos_on, int_value)
