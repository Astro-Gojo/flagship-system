import random

# Simulate sensor input
sensor_value = random.randint(0, 100)  # light sensor example

# Processing (simple rule)
if sensor_value < 50:
    output = "Lights ON"
else:
    output = "Lights OFF"

# Output
print(f"Sensor value: {sensor_value}, Action: {output}")
