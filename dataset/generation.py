import pandas as pd
import numpy as np

# Constants
num_records = 5000

# 1. Performance Metrics
performance_metrics = pd.DataFrame({
    'Execution_Time': np.random.uniform(0.1, 100.0, num_records),  # seconds
    'CPU_Usage': np.random.uniform(0, 100, num_records),  # percentage
    'Memory_Usage': np.random.uniform(100, 32000, num_records),  # MB
    'Communication_Overhead': np.random.uniform(0.01, 500.0, num_records),  # milliseconds
    'Load_Distribution': np.random.uniform(0, 100, num_records)  # percentage
})

# 2. Computational Tasks Data
task_ids = np.arange(1, num_records + 1)
computational_tasks = pd.DataFrame({
    'Task_ID': task_ids,
    'Task_Size': np.random.uniform(1, 1000, num_records),  # MB
    'Task_Complexity': np.random.uniform(1, 10, num_records)  # arbitrary complexity scale
})

# 3. Adaptive Mesh Data
adaptive_mesh_data = pd.DataFrame({
    'Mesh_Resolution': np.random.uniform(0.1, 10.0, num_records),  # arbitrary resolution scale
    'Refinement_Level': np.random.randint(1, 6, num_records),  # levels 1 to 5
    'Refinement_Criteria': np.random.choice(['criterion1', 'criterion2', 'criterion3'], num_records)
})

# 4. Node Information
node_ids = np.arange(1, num_records + 1)
node_information = pd.DataFrame({
    'Node_ID': node_ids,
    'Node_Capacity': np.random.uniform(2.0, 128.0, num_records),  # CPU in GHz
    'Memory_Capacity': np.random.uniform(8, 1024, num_records),  # Memory in GB
    'Network_Bandwidth': np.random.uniform(1.0, 100.0, num_records)  # Bandwidth in Gbps
})

# Load distribution strategies
load_distribution_strategies = [
    'Static Round-robin', 'Static Random', 'Static Block',
    'Dynamic Work Stealing', 'Dynamic Master-worker', 'Dynamic Hierarchical',
    'Partitioning Graph', 'Partitioning Recursive Bisection',
    'Centralized Scheduling', 'Central Queue',
    'Decentralized Neighbor Exchange', 'Decentralized Diffusion',
    'Adaptive Hierarchical', 'Adaptive AMR'
]

# 5. Load Balancing Data
load_balancing_data = pd.DataFrame({
    'Load_Distribution_Strategy': np.random.choice(load_distribution_strategies, num_records),
    'Previous_Load_Balancing_Decisions': np.random.uniform(0, 1, num_records),  # some decision metric
    'Resulting_Performance': np.random.uniform(0.1, 100.0, num_records)  # arbitrary performance scale
})

# Saving the datasets to CSV files
performance_metrics.to_csv('performance_metrics.csv', index=False)
computational_tasks.to_csv('computational_tasks.csv', index=False)
adaptive_mesh_data.to_csv('adaptive_mesh_data.csv', index=False)
node_information.to_csv('node_information.csv', index=False)
load_balancing_data.to_csv('load_balancing_data.csv', index=False)

performance_metrics.head(), computational_tasks.head(), adaptive_mesh_data.head(), node_information.head(), load_balancing_data.head()
