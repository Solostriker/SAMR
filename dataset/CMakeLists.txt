cmake_minimum_required(VERSION 3.10)
project(HPC_Tests)

set(CMAKE_CXX_STANDARD 11)

# Add Google Test
include(FetchContent)
FetchContent_Declare(
  googletest
  URL https://github.com/google/googletest/archive/release-1.10.0.tar.gz
)
FetchContent_MakeAvailable(googletest)
enable_testing()

# Add the source files
add_executable(performance_simulation_test performance_simulation_test.cpp)
add_executable(data_analysis_test data_analysis_test.cpp)

# Link Google Test
target_link_libraries(performance_simulation_test gtest gtest_main)
target_link_libraries(data_analysis_test gtest gtest_main)

add_test(NAME performance_simulation_test COMMAND performance_simulation_test)
add_test(NAME data_analysis_test COMMAND data_analysis_test)
