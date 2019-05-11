import logging
from device_handlers.meta_driver import MetaDriver

logger = logging.getLogger(__name__)


class Dummy(MetaDriver):

    def __init__(self, device_config):
        super(Dummy, self).__init__()
        logger.warning("Dummy devices initiated with config: %s" % device_config)

    def set_device_double_value(self, value):
        logger.warning("Dummy set_device_double_value %s" % value)
        return super(Dummy, self).set_device_double_value(value)

    def get_sensor_double_value(self):
        logger.warning("Dummy get_sensor_double_value")
        return super(Dummy, self).get_sensor_double_value()

    def get_sensor_string_value(self):
        logger.warning("Dummy get_sensor_string_value")
        return super(Dummy, self).get_sensor_string_value()
