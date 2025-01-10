import unittest
import sys
sys.path.append("WayFinder")
import testdata.data as d
import modules.between_feature as bwt




# CustomTestResult to capture and log failed tests
class CustomTestResult(unittest.TestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.failed_tests_info = []

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.failed_tests_info.append((test, 'Failure', err))

    def addError(self, test, err):
        super().addError(test, err)
        self.failed_tests_info.append((test, 'Error', err))
        
    def save_failed_tests_info(self, filename='Wayfinder/tests/failed_tests_summary.txt'):
        with open(filename, 'w') as f:
            for test, result_type, err in self.failed_tests_info:
                f.write(f'{test.id()} -> {result_type}\n')
                for line in self._exc_info_to_string(err, test).splitlines():
                    f.write(f'\t{line}\n')
                f.write('\n')




# CustomTestRunner to use CustomTestResult
class CustomTestRunner(unittest.TextTestRunner):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self, test):
        # Use CustomTestResult
        result = CustomTestResult(self.stream, descriptions=self.descriptions, verbosity=self.verbosity)
        test(result)
        return result
                
                
                
                
# Main test case class
class TestBetweenFunctions(unittest.TestCase):
    pass




# Function to generate test methods based on data
def generate_test_method(data):
    def test_method(self):
        output = bwt.between_query(data[0], data[1], data[2])
        output.sort()
        
        expected = data[3]
        expected.sort()
        print(output)
        print(expected)
        self.assertEqual(output, expected)
    return test_method




# Dynamically adding test methods
for i, data in enumerate(d.between_data, start=1):
    test_name = f'test_between_data_{i}'
    test_method = generate_test_method(data)
    setattr(TestBetweenFunctions, test_name, test_method)




if __name__ == '__main__':
    # Using the custom runner instead of unittest.main()
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestBetweenFunctions)
    runner = CustomTestRunner(verbosity=2)
    result = runner.run(suite)
    # At this point, all tests have been run, and we can save the failed information.
    result.save_failed_tests_info()
    
    print(f"Ran {result.testsRun} tests.")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")