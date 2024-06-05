#include <iostream>
#include <fstream>
#include <vector>
#include <sstream>
#include <string>
#include <numeric>
#include <cmath>

struct DataSet {
    std::vector<double> data;
    std::string name;
};

void analyze_data(const DataSet& dataset) {
    double sum = std::accumulate(dataset.data.begin(), dataset.data.end(), 0.0);
    double mean = sum / dataset.data.size();

    double sq_sum = std::inner_product(dataset.data.begin(), dataset.data.end(), dataset.data.begin(), 0.0);
    double stdev = std::sqrt(sq_sum / dataset.data.size() - mean * mean);

    std::cout << "Analysis of " << dataset.name << ":\n";
    std::cout << "Mean: " << mean << "\n";
    std::cout << "Standard Deviation: " << stdev << "\n\n";
}

int main() {
    std::ifstream file("performance_metrics.csv");

    if (!file.is_open()) {
        std::cerr << "Error opening file" << std::endl;
        return 1;
    }

    std::string line, word;
    std::getline(file, line); // skip header

    DataSet execution_time = { std::vector<double>(), "Execution Time" };
    DataSet cpu_usage = { std::vector<double>(), "CPU Usage" };
    DataSet memory_usage = { std::vector<double>(), "Memory Usage" };
    DataSet communication_overhead = { std::vector<double>(), "Communication Overhead" };
    DataSet load_distribution = { std::vector<double>(), "Load Distribution" };

    while (std::getline(file, line)) {
        std::stringstream ss(line);
        
        std::getline(ss, word, ','); execution_time.data.push_back(std::stod(word));
        std::getline(ss, word, ','); cpu_usage.data.push_back(std::stod(word));
        std::getline(ss, word, ','); memory_usage.data.push_back(std::stod(word));
        std::getline(ss, word, ','); communication_overhead.data.push_back(std::stod(word));
        std::getline(ss, word, ','); load_distribution.data.push_back(std::stod(word));
    }

    file.close();

    analyze_data(execution_time);
    analyze_data(cpu_usage);
    analyze_data(memory_usage);
    analyze_data(communication_overhead);
    analyze_data(load_distribution);

    return 0;
}
