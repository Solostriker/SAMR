import subprocess
import time

def measure_runtime(command):
    start_time = time.time()
    process = subprocess.run(command, shell=True, capture_output=True, text=True)
    end_time = time.time()
    runtime = end_time - start_time
    return runtime, process.stdout

# Measure runtime of performance_simulation.py
python_command = "python3 performance_simulation.py"
python_runtime, python_output = measure_runtime(python_command)

# Measure runtime of performance_simulation.cpp
cpp_command = "./performance_simulation_test"
cpp_runtime, cpp_output = measure_runtime(cpp_command)

# Print runtime comparison
print(f"Python script runtime: {python_runtime:.4f} seconds")
print(f"C++ script runtime: {cpp_runtime:.4f} seconds")

# Output results of C++ and Python for verification
print("\nPython output:\n", python_output)
print("\nC++ output:\n", cpp_output)
