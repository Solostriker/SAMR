#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <string>

struct Task {
    int task_id;
    double task_size;
    double task_complexity;
    double simulated_performance;
};

double simulate_performance(double task_size, double task_complexity, double node_capacity) {
    return task_size * task_complexity / node_capacity;
}

int main() {
    std::ifstream task_file("computational_tasks.csv");
    std::ifstream node_file("node_information.csv");

    if (!task_file.is_open() || !node_file.is_open()) {
        std::cerr << "Error opening file" << std::endl;
        return 1;
    }

    std::vector<Task> tasks;
    std::vector<double> node_capacities;
    std::string line, word;

    // Read node capacities
    std::getline(node_file, line); // skip header
    while (std::getline(node_file, line)) {
        std::stringstream ss(line);
        std::getline(ss, word, ','); // Node_ID
        std::getline(ss, word, ','); // Node_Capacity
        node_capacities.push_back(std::stod(word));
    }

    // Read tasks and simulate performance
    std::getline(task_file, line); // skip header
    while (std::getline(task_file, line)) {
        std::stringstream ss(line);
        Task task;
        std::getline(ss, word, ','); task.task_id = std::stoi(word);
        std::getline(ss, word, ','); task.task_size = std::stod(word);
        std::getline(ss, word, ','); task.task_complexity = std::stod(word);
        
        double node_capacity = node_capacities[rand() % node_capacities.size()];
        task.simulated_performance = simulate_performance(task.task_size, task.task_complexity, node_capacity);
        tasks.push_back(task);
    }

    task_file.close();
    node_file.close();

    // Write to a new CSV file
    std::ofstream out_file("computational_tasks_with_performance_cpp.csv");
    out_file << "Task_ID,Task_Size,Task_Complexity,Simulated_Performance\n";
    for (const auto& task : tasks) {
        out_file << task.task_id << "," << task.task_size << "," << task.task_complexity << "," << task.simulated_performance << "\n";
    }
    out_file.close();

    return 0;
}
