
service Tank{

    # test if robot is available
    void ping(),

    # Control by speed
    oneway void c_speed(1:string device_id, 2:double value),

}