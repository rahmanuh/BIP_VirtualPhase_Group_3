import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

from simulate import readMat

def run_simulation(d_p):
    simulation_cmd='./exp_2_calib_damp_p -override m=0.2,r=0.1,d_p='+str(d_p)+',g=9.8'

    os.chdir('../../generatedCode/gantry_system.exp_2_calib_damp_p/')
    os.system(simulation_cmd)

    [name, data] = readMat('../../generatedCode/gantry_system.exp_2_calib_damp_p/exp_2_calib_damp_p_res.mat')

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
    plt.title('Real-life theta position')  # Add a title
    plt.xlabel('Time (s)')     # Label for the x-axis
    plt.ylabel('Theta (rad)')     # Label for the y-axis
    plt.show()

def plot_simul_data(simul_data):
    plt.plot(simul_data[0], simul_data[2])
    plt.title('Simulation theta position d_p=0.05')  # Add a title
    plt.xlabel('Time (s)')     # Label for the x-axis
    plt.ylabel('Theta (rad)')     # Label for the y-axis
    plt.show()

def calculate_sum_of_squared_error(real_data, simul_data):
    return np.sum((real_data - simul_data) ** 2)

real_data = read_real_live_calib_data('calibration_data_d_p.csv')
x_real_pos = real_data[1]

d_p_range = np.arange(0.00, 5.01, 0.01)
x_simul_pos = []
sse_results = []

#for num in d_p_range:
#    [name, simul_data] = run_simulation(num)
#    #x_simul_pos.append([num, simul_data[2]])
#    sse_results.append([simul_data[5], calculate_sum_of_squared_error(x_real_pos[-5002:], simul_data[2])])
#    #sse_results.append(calculate_sum_of_squared_error(x_real_pos[-5002:], simul_data[2]))
#    #break

#sse_results.sort()
#sse_results_sorted = sorted(sse_results, key=lambda x: x[1])
#print(sse_results)

# From the calibration, we got d_p = 0.05 with the smallest sse = 45.72760109141336
[name, simul_data] = run_simulation(0.05)

plot_real_life_calib_data(real_data)
plot_simul_data(simul_data)

