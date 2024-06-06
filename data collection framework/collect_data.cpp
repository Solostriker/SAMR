#include <iostream>
#include <fstream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <mpi.h>

void simulate_workload(int task_size, int complexity) {
    // Simulate computational task by consuming CPU cycles
    volatile double result = 0.0;
    for (int i = 0; i < task_size * complexity; ++i) {
        result += sin(i) * cos(i);
    }
}

void adaptive_mesh_refinement(int refinement_level) {
    // Simulate AMR by iteratively refining a mesh
    int base_resolution = 1000;
    for (int i = 0; i < refinement_level; ++i) {
        base_resolution *= 2;
    }
    std::vector<double> mesh(base_resolution, 0.0);
    for (int i = 0; i < base_resolution; ++i) {
        mesh[i] = sin(i) * cos(i);
    }
}

void run_simulation(int task_size, int complexity, int refinement_level, int num_procs) {
    MPI_Init(NULL, NULL);

    int world_size;
    MPI_Comm_size(MPI_COMM_WORLD, &world_size);

    int world_rank;
    MPI_Comm_rank(MPI_COMM_WORLD, &world_rank);

    double start_time = MPI_Wtime();
    simulate_workload(task_size, complexity);
    adaptive_mesh_refinement(refinement_level);
    double end_time = MPI_Wtime();
    double execution_time = end_time - start_time;

    if (world_rank == 0) {
        std::ofstream outfile;
        outfile.open("simulation_data.csv", std::ios_base::app);
        outfile << task_size << "," << complexity << "," << refinement_level << "," << num_procs << "," << execution_time << "\n";
        outfile.close();
    }

    MPI_Finalize();
}

int main(int argc, char** argv) {
    std::vector<int> task_sizes = {5000, 10000, 20000};
    std::vector<int> complexities = {3, 5, 7};
    std::vector<int> refinement_levels = {2, 3, 4};
    std::vector<int> num_procs_list = {1, 2, 4, 8};

    for (int task_size : task_sizes) {
        for (int complexity : complexities) {
            for (int refinement_level : refinement_levels) {
                for (int num_procs : num_procs_list) {
                    run_simulation(task_size, complexity, refinement_level, num_procs);
                }
            }
        }
    }

    return 0;
}
