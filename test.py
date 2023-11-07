from scipy import io
import matplotlib.pyplot as plt
import numpy as np

first_file = "./Data/1. BatteryAgingARC-FY08Q4/B0005.mat"
single_data = io.loadmat(first_file)

print(single_data.keys())
print("header: " + str(single_data.get("__header__")))
print("version: " + str(single_data.get("__version__")))
print("global: " + str(single_data.get("__globals__")))

time = []
voltage = []
current = []
temperature = []
b0005_data = single_data.get("B0005")

time = []
voltage = []
current = []
temperature = []

temp = b0005_data[0][0][0][0][2]


f = open("readable2.txt", "a")

for i in temp:
    f.write(str(i))

print("go check readable.txt for readable format of B0005.mat file")