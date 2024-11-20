import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

from simulate import readMat

def run_simulation(d_c):
    simulation_cmd='./exp_1_calib_damp_c -override M=10,d_c='+str(d_c)

    os.chdir('../../generatedCode/gantry_system.exp_1_calib_damp_c/')
    os.system(simulation_cmd)

    [name, data] = readMat('../../generatedCode/gantry_system.exp_1_calib_damp_c/exp_1_calib_damp_c_res.mat')

    return [name, data]

def read_real_live_calib_data(file):
    df = pd.read_csv(file, header=None)
    time = df[0].values
    x_pos = df[1].values
    new_time = []
    for t in time:
        if t == np.nan:
            new_time.append(0)
        else:
            new_time.append(t * 0.004)
    
    return [new_time, x_pos]

def plot_real_life_calib_data(real_data):
    plt.plot(real_data[0], real_data[1])
    plt.title('Real-life X position')  # Add a title
    plt.xlabel('Time (s)')     # Label for the x-axis
    plt.ylabel('X (m)')     # Label for the y-axis
    plt.show()

def plot_simul_data(simul_data):
    plt.plot(simul_data[0], simul_data[2])
    plt.title('Simulation X position d_c=4.79')  # Add a title
    plt.xlabel('Time (s)')     # Label for the x-axis
    plt.ylabel('X (m)')     # Label for the y-axis
    plt.show()

def calculate_sum_of_squared_error(real_data, simul_data):
    return np.sum((real_data - simul_data) ** 2)

real_data = read_real_live_calib_data('calibration_data_d_c.csv')
x_real_pos = real_data[1]

d_c_range = np.arange(0.00, 5.01, 0.01)
x_simul_pos = []
sse_results = []

for num in d_c_range:
    [name, simul_data] = run_simulation(num)
    #x_simul_pos.append([num, simul_data[2]])
    sse_results.append([simul_data[6], calculate_sum_of_squared_error(x_real_pos[-5002:], simul_data[2])])
    #break

#sse_results.sort(key=lambda x: x[:1])
#sse_results_sorted = sorted(sse_results, key=lambda x: x[1])
#print(sse_results)

# From the calibration, we got d_c = 4.79 with the smallest sse = 12.700664774200487
[name, simul_data] = run_simulation(4.79)

plot_real_life_calib_data(real_data)
plot_simul_data(simul_data)

