import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import platform

from simulate import readMat

def deg_to_rad(degree):
    return np.deg2rad(degree)

def rad_to_deg(radian):
    return np.rad2deg(radian)

def calculate_cost(max_theta, t_task):
    '''
    Calculate cost function, a and b are constant from the following calculation
    cost_param.generate_cost_function_params('9278', '9274')
    '''
    a = 46.0
    b = 39.0
    return (a * rad_to_deg(max_theta)) + (b * t_task)

def run_control_simulation(k_p, k_i, k_d):
    # Run simulation for 120 seconds with 0.004 sec interval
    simulation_cmd='./control_loop -override pid.k_p='+str(k_p)+',pid.k_i='+str(k_i)+',pid.k_d='+str(k_d)

    os.chdir('../../generatedCode/gantry_system.control_loop/')
    os.system(simulation_cmd)

    [name, data] = readMat('../../generatedCode/gantry_system.control_loop/control_loop_res.mat')

    thetas = data[4]
    t_tasks = data[0]
    x_outputs = data[16]
    # r.k (10) = data[37]

    set_point = 10 # 10 meter
    lowest_cost = 1000000
    max_allowed_theta_rad = deg_to_rad(30) # max theta = 30 degree
    suff_theta_rad = deg_to_rad(10) # pendulum sufficiently positioned if theta < 10 degree

    stable_theta = thetas[-1]
    stable_theta_idx = len(thetas)
    t_task_idx = 0

    # look for earliset stable theta, we traverse from the back
    # this way we can automatically discard > 30 deg theta
    for i, theta in reversed(list(enumerate(thetas))):
        if abs(stable_theta - theta) > suff_theta_rad:
            stable_theta_idx = i
            #print('theta', i)
            break

    # look for t_task
    x_upper_bound = set_point + 0.01
    x_lower_bound = set_point - 0.01
    
    for i, x_output in enumerate(x_outputs):
        if (x_output >= x_lower_bound) and (x_output <= x_upper_bound):
            t_task_idx = i
            #print('t_task', i)
            break

    if t_task_idx < stable_theta_idx:
        t_task_idx = stable_theta_idx

    max_theta = thetas[t_task_idx]
    t_task = t_tasks[t_task_idx]

    cost = calculate_cost(abs(max_theta), t_task)

    if cost < lowest_cost:
        lowest_cost = cost
        print(lowest_cost, theta, t_task, k_p, k_d)
        return lowest_cost, theta, t_task, k_p, k_d


if __name__ == "__main__":
    k_i = 0
    k_p = range(1, 41, 1)
    k_d = range(10, 501, 10)

    lowest_cost_res = []
    theta_res = []
    t_task_res = []
    kp_res = []
    kd_res = []

    for i in k_p:
        for j in k_d:
            lowest_cost, theta, t_task, kp, kd = run_control_simulation(i, k_i, j)
            lowest_cost_res.append(lowest_cost)
            theta_res.append(theta)
            t_task_res.append(t_task)
            kp_res.append(kp)
            kd_res.append(kd)

    simul_data_res = {
        'lowest_cost' : lowest_cost_res,
        'theta' : theta_res,
        't_task' : t_task_res,
        'k_p' : kp_res,
        'k_d' : kd_res
    }

    df = pd.DataFrame(simul_data_res)
    df.to_csv('simul_data_res.csv')

    sorted_df = df.sort_values(by='lowest_cost')
    print(sorted_df.head)