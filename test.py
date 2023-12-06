import scipy
import numpy as np
import datetime
import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.linear_model import LinearRegression


# Load data from the MATLAB filese] = discharge_data

# print(times)
# print(capacities)

# for key, discharge_entry in all_discharge_data.items():
#     first_entry = next(iter(discharge_entry.values()))
#     times.append(total)
#     capacities.append(first_entry['current_capacity'][0])
#     total += float(first_entry['time'])

# print((capacities))

# # Plotting
# plt.plot(times, capacities, marker='o', linestyle='-')
# plt.xlabel('Time (s)')
# plt.ylabel('Capacity (c)')
# plt.title('Capacity Load Over Time')


battery_5_data = scipy.io.loadmat('./Data/1. BatteryAgingARC-FY08Q4/B0006.mat')
discharge = {}
for i, element in enumerate(battery_5_data['B0006'][0][0][0][0]):
    if element[0][0] == 'discharge':
        discharge[i] = {}
        data = element[3]
        discharge[i]["amb_temp"] = str(element[1][0][0])
        discharge[i]["voltage_load"] = data[0][0][4][0].tolist()
        discharge[i]["time"] = np.real(data[0][0][5][0][-1])
        discharge[i]["current_capacity"] = np.real(data[0][0][6])


battery_5_data = scipy.io.loadmat('./Data/1. BatteryAgingARC-FY08Q4/B0018.mat')
discharge2 = {}
for i, element in enumerate(battery_5_data['B0018'][0][0][0][0]):
    if element[0][0] == 'discharge':
        discharge2[i] = {}
        data = element[3]
        discharge2[i]["amb_temp"] = str(element[1][0][0])
        discharge2[i]["voltage_load"] = data[0][0][4][0].tolist()
        discharge2[i]["time"] = np.real(data[0][0][5][0][-1])
        discharge2[i]["current_capacity"] = np.real(data[0][0][6])

unseen_times = []
unseen_capacities = []
unseen_total = 0

for key, entry in discharge2.items():
    if 'current_capacity' in entry and 'time' in entry:
        unseen_times.append(unseen_total)
        unseen_capacities.append(entry['current_capacity'][0][0])
        time = entry['time']
        unseen_total += float(time)


import matplotlib.pyplot as plt

times = []
capacities = []
total = 0

for key, entry in discharge.items():
    if 'current_capacity' in entry and 'time' in entry:
        times.append(total)
        capacities.append(entry['current_capacity'][0][0])
        time = entry['time']
        total += float(time)

times = np.array(times).reshape(-1, 1)
capacities = np.array(capacities)

# Create and fit a linear regression model
linear_model = LinearRegression()
linear_model.fit(times, capacities)

# Create and fit a RandomForestRegressor model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(times, capacities)

# Make predictions using both models
times_pred = np.linspace(min(times), max(times), 100).reshape(-1, 1)
capacities_pred_linear = linear_model.predict(times_pred)
capacities_pred_rf = rf_model.predict(times_pred)

unseen_times_pred = np.array(unseen_times).reshape(-1, 1)
capacities_pred_linear_unseen = linear_model.predict(unseen_times_pred)
capacities_pred_rf_unseen = rf_model.predict(unseen_times_pred)

# Plotting training data
plt.scatter(times, capacities, marker='o', label='Training Data')

# # Plotting predictions from Linear Regression on training data
# plt.plot(times_pred, capacities_pred_linear, linestyle='solid', label='Linear Regression Predictions (Training)')

# # Plotting predictions from RandomForestRegressor on training data
# plt.plot(times_pred, capacities_pred_rf, linestyle='dashdot', label='Random Forest Predictions (Training)')

# # Plotting unseen data
# plt.scatter(unseen_times, unseen_capacities, marker='x', label='Unseen Data')

# Plotting predictions from Linear Regression on unseen data
plt.plot(unseen_times_pred, capacities_pred_linear_unseen, linestyle='dashed', label='Linear Regression Predictions (Unseen)')

# Plotting predictions from RandomForestRegressor on unseen data
plt.plot(unseen_times_pred, capacities_pred_rf_unseen, linestyle='dotted', label='Random Forest Predictions (Unseen)')

# Adding labels and title
plt.xlabel('Time (s)')
plt.ylabel('Capacity (c)')
plt.title('Capacity Load Over Time')

# Adding legend
plt.legend()

# Display the plot
plt.show()

mse_linear_train = mean_squared_error(capacities, linear_model.predict(times))
mae_linear_train = mean_absolute_error(capacities, linear_model.predict(times))

mse_rf_train = mean_squared_error(capacities, rf_model.predict(times))
mae_rf_train = mean_absolute_error(capacities, rf_model.predict(times))

# Calculate accuracy metrics for unseen data
mse_linear_unseen = mean_squared_error(unseen_capacities, capacities_pred_linear_unseen)
mae_linear_unseen = mean_absolute_error(unseen_capacities, capacities_pred_linear_unseen)

mse_rf_unseen = mean_squared_error(unseen_capacities, capacities_pred_rf_unseen)
mae_rf_unseen = mean_absolute_error(unseen_capacities, capacities_pred_rf_unseen)

# Print or log the accuracy metrics
print('Training Data Metrics:')
print(f'Linear Regression MSE: {mse_linear_train}')
print(f'Linear Regression MAE: {mae_linear_train}')
print(f'Random Forest MSE: {mse_rf_train}')
print(f'Random Forest MAE: {mae_rf_train}')

print('\nUnseen Data Metrics:')
print(f'Linear Regression MSE (Unseen): {mse_linear_unseen}')
print(f'Linear Regression MAE (Unseen): {mae_linear_unseen}')
print(f'Random Forest MSE (Unseen): {mse_rf_unseen}')
print(f'Random Forest MAE (Unseen): {mae_rf_unseen}')