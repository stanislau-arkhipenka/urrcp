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
service Urrcp{

    # test if robot is available
    bool ping(),

    # Get init schema
    top_level get_init_schema(),

    # Set config
    oneway void set_config(1:string config_name, 2:string config_value),

    # Control by position
    oneway void set_device_position(1:string device_id, 2:double value),

    # Control by speed
    oneway void set_device_speed(1:string device_id, 2:double value),

    # Control by acceleration
    oneway void set_device_acceleration(1:string device_id, 2:double value),


}