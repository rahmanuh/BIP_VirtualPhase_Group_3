import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import platform

from simulate import readMat

# How to run this script is you are using OpenModelica container?
# 1. Run it inside the container to run the simulation.
# 2. Run this outside in your local terminal to animate. 

# Workaround to run this script inside a Linux container. 
# because cannot install tkinter inside Linux container eventhough 
# using python venv.
if platform.system() == 'Darwin':
    from animation import animate_gantry_system

def run_control_simulation(k_p, k_i, k_d):
    simulation_cmd='./control_loop -override pid.k_p='+str(k_p)+',pid.k_i='+str(k_i)+',pid.k_d='+str(k_d)

    os.chdir('../../generatedCode/gantry_system.control_loop/')
    os.system(simulation_cmd)

    [name, data] = readMat('../../generatedCode/gantry_system.control_loop/control_loop_res.mat')

    return [name, data]

k_p = 10
k_i = 20
k_d = 5

[name, data] = run_control_simulation(k_p, k_i, k_d)

# process.theta = data[4]
# process.x_output = data[16]
# r.k (20) = data[37]

x = data[16]
theta = data[4]
rope_length = 10

animate_gantry_system(x, theta, rope_length)

