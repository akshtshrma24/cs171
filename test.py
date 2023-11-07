from scipy import io
import matplotlib.pyplot as plt
import numpy as np

first_file = "./Data/1. BatteryAgingARC-FY08Q4/B0005.mat"
single_data = io.loadmat(first_file)

print(single_data.keys())
print("header: " + str(single_data.get("__header__")))
print("version: " + str(single_data.get("__version__")))
print("global: " + str(single_data.get("__globals__")))
# print("B0005: " + str(single_data.get("B0005")))

time = []
voltage = []
current = []
temperature = []
b0005_data = single_data.get("B0005")

time = []
voltage = []
current = []
temperature = []

f = open("readable.txt", "a")

for i in b0005_data:
    f.write(str(i))

# for record in b0005_data:
#     print(record)
#     time_data = record['data']['Time'][0][0][0]
#     voltage_data = record['data']['Voltage_measured'][0][0][0]
#     current_data = record['data']['Current_measured'][0][0][0]
#     temperature_data = record['data']['Temperature_measured'][0][0][0]

#     time.append(time_data)
#     voltage.append(voltage_data)
#     current.append(current_data)
#     temperature.append(temperature_data)

# # Plot voltage, current, and temperature over time
# plt.figure(figsize=(12, 6))

# plt.subplot(311)
# for i in range(len(time)):
#     plt.plot(time[i], voltage[i], label=f"Cycle {i+1}")
# plt.title('Voltage vs. Time')
# plt.xlabel('Time (s)')
# plt.ylabel('Voltage (V)')
# plt.legend()

# plt.subplot(312)
# for i in range(len(time)):
#     plt.plot(time[i], current[i], label=f"Cycle {i+1}")
# plt.title('Current vs. Time')
# plt.xlabel('Time (s)')
# plt.ylabel('Current (A)')
# plt.legend()

# plt.subplot(313)
# for i in range(len(time)):
#     plt.plot(time[i], temperature[i], label=f"Cycle {i+1}")
# plt.title('Temperature vs. Time')
# plt.xlabel('Time (s)')
# plt.ylabel('Temperature (°C)')
# plt.legend()

# plt.tight_layout()
# plt.show()
