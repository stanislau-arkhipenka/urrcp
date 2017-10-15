
INIT_SCHEMA = {
    "id": "id_001",
    "name": "Panzer Red",
    "type": "Transport",
    "manufacture": "Stas Systems",
    "version": "1",
    "api_version": "1",

    "devices": [
        {
            "id": "cat_1",
            "name": "caterpillar_left",
            "available_control_types": [
                {
                    "name": "speed",
                    "min_value": -100,
                    "max_value": 100,
                    "granularity": 1
                }
            ]

        },
        {
            "id": "cat_1",
            "name": "caterpillar_right",
            "available_control_types": [
                {
                    "name": "speed",
                    "min_value": -100,
                    "max_value": 100,
                    "granularity": 1
                }
            ]

        }
    ]
}
