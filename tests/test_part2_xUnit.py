class TestCase:
    def __init__(self, name):
        self.name = name

    def setup(self):
        pass

    def run(self):
        self.setup()
        method = getattr(self, self.name)
        method()


class WasRun(TestCase):
    def __init__(self, name):
        self.was_run = None
        super().__init__(name)

    def test_method(self):
        self.was_run = True

    def setup(self):
        self.was_run = None
        self.was_setup = True


class TestCaseTest(TestCase):

    def setup(self):
        self.test = WasRun('test_method')

    def test_setup(self):
        self.test.run()
        assert self.test.was_setup

    def test_running(self):
        self.test.run()
        assert self.test.was_run


TestCaseTest('test_setup').run()
