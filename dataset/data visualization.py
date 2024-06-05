import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
performance_metrics = pd.read_csv('performance_metrics.csv')
computational_tasks = pd.read_csv('computational_tasks.csv')
adaptive_mesh_data = pd.read_csv('adaptive_mesh_data.csv')
node_information = pd.read_csv('node_information.csv')
load_balancing_data = pd.read_csv('load_balancing_data.csv')

# Function to create histograms
def plot_histograms(df, column, title):
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=True)
    plt.title(title)
    plt.xlabel(column)
    plt.ylabel('Frequency')
    plt.show()

# Plot histograms for each dataset
plot_histograms(performance_metrics, 'Execution_Time', 'Execution Time Distribution')
plot_histograms(performance_metrics, 'CPU_Usage', 'CPU Usage Distribution')
plot_histograms(performance_metrics, 'Memory_Usage', 'Memory Usage Distribution')

plot_histograms(computational_tasks, 'Task_Size', 'Task Size Distribution')
plot_histograms(computational_tasks, 'Task_Complexity', 'Task Complexity Distribution')

plot_histograms(adaptive_mesh_data, 'Mesh_Resolution', 'Mesh Resolution Distribution')
plot_histograms(adaptive_mesh_data, 'Refinement_Level', 'Refinement Level Distribution')

plot_histograms(node_information, 'Node_Capacity', 'Node Capacity Distribution')
plot_histograms(node_information, 'Memory_Capacity', 'Memory Capacity Distribution')

plot_histograms(load_balancing_data, 'Previous_Load_Balancing_Decisions', 'Previous Load Balancing Decisions Distribution')
plot_histograms(load_balancing_data, 'Resulting_Performance', 'Resulting Performance Distribution')
