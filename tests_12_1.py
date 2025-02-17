import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest (unittest.TestCase):
    def test_walk(self):
        walker = Runner("Di")
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    def test_run(self):
        rn = Runner("Andrew")
        for i in range(10):
            rn.run()
        self.assertEqual(rn.distance, 100)

    def test_challenge(self):
        walker = Runner("Den")
        rn = Runner("Tom")
        for i in range(10):
            walker.walk()
            rn.run()
        self.assertNotEqual(walker.distance, rn.distance)


if __name__ == '__main__':
    unittest.main()
