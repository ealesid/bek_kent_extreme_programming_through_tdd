class TestCase:
    def __init__(self, name):
        self.name = name

    def setup(self):
        pass

    def teardown(self):
        pass

    def run(self, result):
        result.test_started()
        self.setup()

        try:
            method = getattr(self, self.name)
            method()
        except Exception as e:
            result.test_failed()

        self.teardown()


class WasRun(TestCase):
    def __init__(self, name):
        self.was_run = None
        super().__init__(name)

    def test_method(self):
        self.was_run = True
        self.log += ' test_method'

    def test_broken_method(self):
        raise Exception

    def setup(self):
        self.was_run = None
        self.was_setup = True
        self.log = 'setup'

    def teardown(self):
        self.log += ' teardown'


class TestCaseTest(TestCase):

    def setup(self):
        self.result = TestResult()

    def test_template_method(self):
        test = WasRun('test_method')
        test.run(self.result)
        print(f'\n\ttest.log >\t{test.log}')
        assert test.log == 'setup test_method teardown'

    def test_result(self):
        test = WasRun('test_method')
        test.run(self.result)
        print(f'\n\ttest_result >\t{self.result.summary()}')
        assert self.result.summary() == '1 run, 0 failed'

    def test_failed_result(self):
        test = WasRun('test_broken_method')
        test.run(self.result)
        print(f'\n\ttest_failed_result >\t{self.result.summary()}')
        assert self.result.summary() == '1 run, 1 failed'

    def test_failed_result_formatting(self):
        self.result.test_started()
        self.result.test_failed()
        print(f'\n\ttest_failed_result_formatting >\t{self.result.summary()}')
        assert self.result.summary() == '1 run, 1 failed'

    def test_suite(self):
        suite = TestSuite()
        suite.add(WasRun('test_method'))
        suite.add(WasRun('test_broken_method'))
        suite.run(self.result)
        print(f'\n\ttest_suite >\t{self.result.summary()}')
        assert self.result.summary() == '2 run, 1 failed'


class TestResult:
    def __init__(self):
        self.run_count = 0
        self.error_count = 0

    def test_started(self):
        self.run_count += 1

    def test_failed(self):
        self.error_count += 1

    def summary(self):
        return f'{self.run_count} run, {self.error_count} failed'


class TestSuite:
    def __init__(self):
        self.tests = []

    def add(self, test):
        self.tests.append(test)

    def run(self, result):
        for test in self.tests:
            print(f'\ntest_suite run >\t{test.name}')
            test.run(result)


suite = TestSuite()
suite.add(TestCaseTest('test_template_method'))
suite.add(TestCaseTest('test_result'))
suite.add(TestCaseTest('test_failed_result'))
suite.add(TestCaseTest('test_failed_result_formatting'))
suite.add(TestCaseTest('test_suite'))

result = TestResult()
suite.run(result)
print(f'\n\tresult summary >\t{result.summary()}')
