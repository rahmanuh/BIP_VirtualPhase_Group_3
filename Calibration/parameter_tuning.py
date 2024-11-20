import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

from simulate import readMat

def run_simulation(M=10, d_c=2):
    simulation_cmd='./exp_1_calib_damp_c --override M='+str(M)+',d_c='+str(d_c)

    os.chdir('gantry_system.exp_1_calib_damp_c/')
    os.system(simulation_cmd)

    [name, data] = readMat('exp_1_calib_damp_c_res.mat')

    return [name, data]

def read_real_live_calib_data(file):
    df = pd.read_csv(file, header=None)
    time = df[0]
    x_pos = df[1]
    new_time = []
    for t in time:
        if t == np.nan:
            new_time.append(0)
        else:
            new_time.append(t * 0.004)
    
    real_data = [new_time, x_pos]
    return real_data

def plot_real_life_calib_data(real_data):
    plt.plot(real_data[0], real_data[1])
    plt.title('Real-life X position')  # Add a title
    plt.xlabel('Time (s)')     # Label for the x-axis
    plt.ylabel('X (m)')     # Label for the y-axis
    plt.show()

#data = read_real_live_calib_data('../BIP_VirtualPhase_Group_3/Calibration/calibration_data_d_c.csv')
#plot_real_life_calib_data(data)

[name, data] = run_simulation()

print(name)