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
        exec('self.' + self.name + '()')
        self.teardown()
        # method = getattr(self, self.name)
        # method()


class WasRun(TestCase):
    def __init__(self, name):
        self.was_run = None
        super().__init__(name)

    def test_method(self):
        self.was_run = True
        self.log += ' test_method'

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
        assert test.log == 'setup test_method teardown'

    # def test_running(self):
    #     self.test.run()
    #     assert self.test.was_run


TestCaseTest('test_template_method').run()
