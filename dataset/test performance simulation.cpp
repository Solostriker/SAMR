#include <gtest/gtest.h>
#include "performance simulation.cpp"  // Make sure this includes the necessary headers and function declarations

TEST(PerformanceSimulationTest, SimulatePerformance) {
    double task_size = 500;  // MB
    double task_complexity = 5;  // arbitrary complexity scale
    double node_capacity = 32;  // GHz
    double performance = simulate_performance(task_size, task_complexity, node_capacity);
    double expected_performance = task_size * task_complexity / node_capacity;
    ASSERT_NEAR(performance, expected_performance, 1e-9);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
