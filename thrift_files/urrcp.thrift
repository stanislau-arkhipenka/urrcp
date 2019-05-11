/*
struct default_control_type {
    1: string name,
    2: double min_value,
    3: double max_value,
    4: double granularity
}

struct device {
    1: string id,
    2: string name,
    3: list<string> control_types
}

struct top_level {
    1: string id,
    2: string name,
    3: string type,
    4: string manufacture,
    5: string version,
    6: string api_version,
    7: map<string,device> device_list
}
*/
service Urrcp{

    # test if robot is available
    bool ping(),

    # Get init schema
    string get_init_schema(),

    # Set config
    oneway void set_config(1:string config_name, 2:string config_value),

    # Physical device control
    oneway void set_device_double_value(1:string device_id, 2:double value),

    # Get double information from sensors
    double get_sensor_double_value(1:string sensor_id),

    # Get string information from sensors
    string get_sensor_string_value(1:string sensor_id)

}