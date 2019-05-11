
INIT_SCHEMA = {
    "id": "id_00001",
    "name": "Panzer Red",
    "type": "Transport",
    "manufacture": "Lolez Ltd",
    "version": "1",
    "api_version": "1",

    "devices": {
        "engine_left": {
            "driver": "i2c_pwm_PCA9685",
            "physical_dev_opt": {"id": 0, "pwm_freq": 50, "null_pos": 270},
            "type": "set_device_double_value",
            "default_value": 0,
            "min_value": -100,
            "max_value": 100
        },
        "engine_right": {
            "driver": "i2c_pwm_PCA9685",
            "physical_dev_opt": {"id": 0, "pwm_freq": 50, "null_pos": 270},
            "type": "set_device_double_value",
            "default_value": 0,
            "min_value": -100,
            "max_value": 100
        }
    }
}
