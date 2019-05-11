#!/usr/bin/env python
import logging
import json
from device_handlers import driver_router as dr

logger = logging.getLogger(__name__)


class UrrcpHandler(object):

    def __init__(self, schema):
        logger.info("Handler initialization")
        self.schema = schema
        self.device_schema = schema.get("devices")
        self.devices = dict()
        for dev_name, dev_data in self.schema.get("devices", {}).items():
            self.devices[dev_name] = dr.get(dev_data.get("driver"), dr.get("dummy"))(dev_data.get("physical_dev_opt"))
            logger.info("Device %s use %s driver" % (dev_name, self.devices.get(dev_name).__class__.__name__))

    def get_init_schema(self):
        logger.debug("get_init_schema")
        return json.dumps(self.schema)

    def ping(self):
        logger.debug("ping")
        return True

    def set_device_double_value(self, device_id, c_value):
        logger.debug("set_device_double_value %s %s" % (device_id, c_value))
        if device_id in self.devices:
            self.devices.get(device_id).set_device_double_value(c_value)

    def get_sensor_double_value(self, sensor_id):
        logger.debug("get_sensor_double_value %s" % sensor_id)
        if sensor_id in self.devices:
            return self.devices.get(sensor_id).get_sensor_double_value()

    def get_sensor_string_value(self, sendor_id):
        logger.debug("get_sensor_string_value %s" % sendor_id)
        if sendor_id in self.devices:
            return self.devices.get(sendor_id).get_sensor_string_value()
