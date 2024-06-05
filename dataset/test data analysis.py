import unittest
import pandas as pd
from io import StringIO

class TestDataAnalysis(unittest.TestCase):
    
    def setUp(self):
        self.csv_data = StringIO("""Execution_Time,CPU_Usage,Memory_Usage,Communication_Overhead,Load_Distribution
                                    1.0,50.0,1000.0,10.0,50.0
                                    2.0,60.0,2000.0,20.0,60.0
                                    3.0,70.0,3000.0,30.0,70.0""")
        self.df = pd.read_csv(self.csv_data)
    
    def test_analyze_dataset(self):
        summary = self.df.describe()
        self.assertTrue(summary is not None)
        self.assertEqual(summary.loc['mean', 'Execution_Time'], 2.0)
        self.assertEqual(summary.loc['mean', 'CPU_Usage'], 60.0)
        self.assertEqual(summary.loc['mean', 'Memory_Usage'], 2000.0)

if __name__ == '__main__':
    unittest.main()
