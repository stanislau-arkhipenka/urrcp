from init_schema import INIT_SCHEMA


class RobotMeta:

    def __init__(self, init_schema=INIT_SCHEMA):
        self.init_schema = init_schema

    def provide_init_schema(self):
        return self.init_schema

