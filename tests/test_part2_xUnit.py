class TestCase:
    def __init__(self, name):
        self.name = name

    def setup(self):
        pass

    def teardown(self):
        pass

    def run(self):
        result = TestResult()
        result.test_started()
        self.setup()
        method = getattr(self, self.name)
        method()
        self.teardown()
        return result


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

    # def setup(self):
    #     self.test = WasRun('test_method')

    def test_template_method(self):
        test = WasRun('test_method')
        test.run()
        print(f'\n\ttest.log >\t{test.log}')
        assert test.log == 'setup test_method teardown'

    def test_result(self):
        test = WasRun('test_method')
        result = test.run()
        print(f'\n\tresult.summary >\t{result.summary()}')
        assert result.summary() == '1 run, 0 failed'

    def test_failed_result(self):
        test = WasRun('test_broken_method')
        result = test.run()
        assert result.summary() == '1 run, 1 failed'

    # def test_running(self):
    #     self.test.run()
    #     assert self.test.was_run


class TestResult:
    def __init__(self):
        self.run_count = 0

    def test_started(self):
        self.run_count += 1

    def summary(self):
        return f'{self.run_count} run, 0 failed'


TestCaseTest('test_template_method').run()
TestCaseTest('test_result').run()
TestCaseTest('test_failed_result').run()
