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


class RunnerTest(unittest.TestCase):
    def test_walk(self):

        runner = Runner("Walker")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50, "Дистанция при 10 шагах должна быть 50")

    def test_run(self):

        runner = Runner("Runner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100, "Дистанция при 10 пробежках должна быть 100")

    def test_challenge(self):

        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")

        for _ in range(10):
            runner1.run()  # Увеличивает дистанцию на 10 за каждый вызов
            runner2.walk()  # Увеличивает дистанцию на 5 за каждый вызов

        self.assertNotEqual(
            runner1.distance,
            runner2.distance,
            "Дистанции двух бегунов должны быть разными"
        )


# Запуск тестов
if __name__ == "__main__":
    unittest.main()