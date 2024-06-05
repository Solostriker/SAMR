#include <gtest/gtest.h>
#include "data_analysis.cpp"  // Make sure this includes the necessary headers and function declarations

TEST(DataAnalysisTest, AnalyzeData) {
    std::vector<double> data = {1.0, 2.0, 3.0};
    double sum = std::accumulate(data.begin(), data.end(), 0.0);
    double mean = sum / data.size();
    double sq_sum = std::inner_product(data.begin(), data.end(), data.begin(), 0.0);
    double stdev = std::sqrt(sq_sum / data.size() - mean * mean);

    ASSERT_NEAR(mean, 2.0, 1e-9);
    ASSERT_NEAR(stdev, std::sqrt(2.0 / 3.0), 1e-9);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
