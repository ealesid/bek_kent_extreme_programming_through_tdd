class WasRun:
    def __init__(self, name):
        self.was_run = None

    def run(self):
        self.test_method()

    def test_method(self):
        self.was_run = True


test = WasRun('test_method')
print(test.was_run)
test.run()
print(test.was_run)
