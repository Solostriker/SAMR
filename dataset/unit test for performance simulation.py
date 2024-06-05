import unittest
import pandas as pd
from performance_simulation import simulate_performance

class TestPerformanceSimulation(unittest.TestCase):
    
    def setUp(self):
        self.task_size = 500  # MB
        self.task_complexity = 5  # arbitrary complexity scale
        self.node_capacity = 32  # GHz
    
    def test_simulate_performance(self):
        performance = simulate_performance(self.task_size, self.task_complexity, self.node_capacity)
        expected_performance = self.task_size * self.task_complexity / self.node_capacity
        self.assertAlmostEqual(performance, expected_performance)

if __name__ == '__main__':
    unittest.main()
