Day 37 — Execution Log | Date : 27-01-2026



Module: Systems Thinking → State-Based Control

Project: Room Temperature Controller (Python)



🎯 Objective



Design and implement a simple state-based control system that regulates a fan based on room temperature using deterministic logic and hysteresis.





🧠 System Description



* Input: Room temperature (manual input, simulating sensor data)



* States:

-FAN\_ON



-FAN\_OFF



* Control Logic:



-Turn ON fan if temperature ≥ 30°C



-Turn OFF fan if temperature ≤ 26°C



-Maintain current state otherwise (hysteresis)



This prevents rapid ON/OFF toggling when temperature fluctuates near a threshold.





🧩 Implementation Details



* Language: Python



* Programming Paradigm: Procedural, state-based logic



* Key Concepts Used:



-Conditional branching



-State variables



-Threshold-based control



-Hysteresis





🧪 Test Scenarios \& Results

| Input Temperature | Initial State | Output         | Final State |
| ----------------- | ------------- | -------------- | ----------- |
| 32°C              | FAN_OFF       | Fan turned ON  | FAN_ON      |
| 29°C              | FAN_ON        | No change      | FAN_ON      |
| 25°C              | FAN_ON        | Fan turned OFF | FAN_OFF     |
| 27°C              | FAN_OFF       | No change      | FAN_OFF     |



All test cases behaved as expected.





📊 Observations



* Hysteresis successfully prevents unstable switching.



* Logic remains deterministic and predictable.



* System mirrors real-world thermostat behavior.



* Suitable for future porting to embedded systems (ESP32/MCU).





🚀 Next Steps



* Introduce looping for continuous monitoring.



* Replace manual input with simulated or real sensor data.



* Persist state across iterations.



* Port logic to microcontroller (ESP32/Arduino).





✅ Status



Completed successfully. Logic verified and logged.


