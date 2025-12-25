import random

def get_sensor_value():
    value = random.randint(0, 100)
    return value
def decide_light_state(sensor_value):
    if sensor_value <30:
        return "ON"
    else:
        return "OFF"
def display_status(sensor_value, light_state):
    print("Sensor value:", sensor_value)
    print("Light state:", light_state)
sensor = get_sensor_value()
state = decide_light_state(sensor)
display_status(sensor, state)
