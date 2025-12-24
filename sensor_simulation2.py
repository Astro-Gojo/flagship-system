import random

light_value = random.randint(0, 100)
temperature = random.randint(20, 40)

print("Light Sensor Value:", light_value)
print("Temperature Value:", temperature)

if light_value < 50 and temperature > 30:
    print("ACTION: Light ON, Fan ON")
else:
    print("ACTION: Light OFF, Fan OFF")
