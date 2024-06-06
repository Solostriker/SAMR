import subprocess
import pandas as pd
import time
import logging
import os

# Configure logging
logging.basicConfig(filename='simulation.log', level=logging.INFO, format='%(asctime)s %(message)s')

def run_simulation(task_size, complexity, refinement_level, num_procs):
    command = f"mpirun -np {num_procs} ./mpi_simulation {task_size} {complexity} {refinement_level}"
    start_time = time.time()
    try:
        process = subprocess.run(command, shell=True, capture_output=True, text=True)
        end_time = time.time()
        execution_time = end_time - start_time
        logging.info(f"Command: {command}\nOutput: {process.stdout}\nError: {process.stderr}")
        return execution_time, process.stdout
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to run command: {command}\nError: {e}")
        return None, None

def collect_data(task_sizes, complexities, refinement_levels, num_procs_list):
    data = []
    for task_size in task_sizes:
        for complexity in complexities:
            for refinement_level in refinement_levels:
                for num_procs in num_procs_list:
                    execution_time, output = run_simulation(task_size, complexity, refinement_level, num_procs)
                    if execution_time is not None:
                        data.append({
                            'task_size': task_size,
                            'complexity': complexity,
                            'refinement_level': refinement_level,
                            'num_procs': num_procs,
                            'execution_time': execution_time,
                            'output': output
                        })
                        print(f"Task size: {task_size}, Complexity: {complexity}, Refinement level: {refinement_level}, Number of processes: {num_procs}, Execution time: {execution_time:.4f} seconds")
    return pd.DataFrame(data)

def save_data(df, filename):
    df.to_csv(filename, index=False)

# Define task sizes, complexities, refinement levels, and number of processes
task_sizes = [5000, 10000, 20000]
complexities = [3, 5, 7]
refinement_levels = [2, 3, 4]
num_procs_list = [1, 2, 4, 8]

# Collect data
data = collect_data(task_sizes, complexities, refinement_levels, num_procs_list)

# Save data to CSV
save_data(data, 'simulation_data.csv')
