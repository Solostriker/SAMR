import pandas as pd

# Load datasets
performance_metrics = pd.read_csv('performance_metrics.csv')
computational_tasks = pd.read_csv('computational_tasks.csv')
adaptive_mesh_data = pd.read_csv('adaptive_mesh_data.csv')
node_information = pd.read_csv('node_information.csv')
load_balancing_data = pd.read_csv('load_balancing_data.csv')

# Analyze datasets
def analyze_dataset(dataset, name):
    print(f"Analysis of {name}:")
    print(dataset.describe())
    print("\n")

# Perform analysis
analyze_dataset(performance_metrics, "Performance Metrics")
analyze_dataset(computational_tasks, "Computational Tasks")
analyze_dataset(adaptive_mesh_data, "Adaptive Mesh Data")
analyze_dataset(node_information, "Node Information")
analyze_dataset(load_balancing_data, "Load Balancing Data")
