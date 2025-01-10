import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants[:]:  # Копируем список, чтобы избежать ошибок удаления
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        cls.all_results = {}

    def setUp(self):

        self.usain = Runner("Усэйн", speed=10)
        self.andrey = Runner("Андрей", speed=9)
        self.nick = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):

        for result in cls.all_results.values():
            print(result)

    def test_usain_and_nick(self):

        tournament = Tournament(90, self.usain, self.nick)
        results = tournament.start()
        self.__class__.all_results["Usain and Nick"] = results
        self.assertTrue(results[max(results.keys())] == "Ник", "Ник должен быть последним")

    def test_andrey_and_nick(self):

        tournament = Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        self.__class__.all_results["Andrey and Nick"] = results
        self.assertTrue(results[max(results.keys())] == "Ник", "Ник должен быть последним")

    def test_usain_andrey_and_nick(self):

        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        self.__class__.all_results["Usain, Andrey, and Nick"] = results
        self.assertTrue(results[max(results.keys())] == "Ник", "Ник должен быть последним")


# Запуск тестов
if __name__ == "__main__":
    unittest.main()
    