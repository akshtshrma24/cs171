from scipy import io
import matplotlib.pyplot as plt
import numpy as np
Analysing the first .mat file in data
first_file = "./Data/1. BatteryAgingARC-FY08Q4/B0005.mat"
single_data = io.loadmat(first_file)

print(single_data.keys())
print("header: " + str(single_data.get("__header__")))
print("version: " + str(single_data.get("__version__")))
print("global: " + str(single_data.get("__globals__")))
print("B0005: " + str(single_data.get("B0005")))

time = []
voltage = []
current = []
temperature = []
b0005_data = single_data["B0005"]

print(b0005_data)