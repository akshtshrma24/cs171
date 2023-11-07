import os
from scipy import io
import pandas as pd
import matplotlib.pyplot as plt

# Define the directory path
# directory = "/Users/nachikethmamidi/Documents/Fall2023/CS171/MLProject/Data"

# # Access the folders in the directory
# folders = os.listdir(directory)

# # Iterate through each folder and load the .mat files
# for folder in folders:
#     folder_path = os.path.join(directory, folder)
#     if os.path.isdir(folder_path):
#         files = os.listdir(folder_path)
#         for file in files:
#             if file.endswith(".mat"):
#                 file_path = os.path.join(folder_path, file)
#                 data = io.loadmat(file_path)
#                 # Process the data as needed
#                 # Example: Print the keys of the loaded .mat file
#                 print(f"Keys in {file}: {data.keys()}")

# Analysing a single file
first_file = "/Users/nachikethmamidi/Documents/Fall2023/CS171/MLProject/Data/1. BatteryAgingARC-FY08Q4/B0005.mat"
# single_data = io.loadmat(first_file)

# data_mat = single_data["B0005"]

# cycles = data_mat['cycle']

mat = io.loadmat(first_file)


# cycles = mat['cycle']

print(len(mat))
print(type(mat))
print(mat.keys())

# Access the data for Battery #5
battery_data = mat['B0005']

print(type(battery_data))



