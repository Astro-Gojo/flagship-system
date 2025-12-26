import random  # Import random module to simulate sensor readings

# Function 1: Get sensor value
def get_sensor_value():
    """
    Simulates reading a sensor by returning a random value between 0 and 100
    """
    value = random.randint(0, 100)
    return value

# Function 2: Decide light state based on sensor value
def decide_light_state(sensor_value):
    """
    Determines the state of the light based on sensor value:
    - < 30 -> "ON"
    - 30 <= value < 70 -> "DIM"
    - >= 70 -> "OFF"
    """
    if sensor_value < 30:
        return "ON"
    elif 30 <= sensor_value < 70:
        return "DIM"
    else:
        return "OFF"

# Function 3: Display results
def display_status(sensor_value, light_state):
    """
    Prints the sensor value and corresponding light state
    """
    print("Sensor value:", sensor_value)
    print("Light state:", light_state)

# Main function: Entry point of the program
def main():
    """
    Calls functions in order:
    1. Gets sensor value
    2. Decides light state
    3. Displays the result
    """
    sensor = get_sensor_value()                  # Get a fresh random sensor value
    state = decide_light_state(sensor)           # Decide light state based on that value
    display_status(sensor, state)                # Print the output neatly

# Call main() to run the program
main()

