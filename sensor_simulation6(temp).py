FAN_ON = 1
FAN_OFF = 0

fan_state = FAN_OFF

temperature = float(input("Enter room temperature: "))

if temperature >= 30 and fan_state == FAN_OFF:
    fan_state = FAN_ON
    print("Fan turned ON")

elif temperature <= 26 and fan_state == FAN_ON:
    fan_state = FAN_OFF
    print("Fan turned OFF")

else:
    print("No change. Fan state remains",
          "ON" if fan_state == FAN_ON else "OFF")
