import runner_and_tournament
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = runner_and_tournament.Runner('Усейн', 10)
        self.andrey = runner_and_tournament.Runner('Андрей', 9)
        self.nick = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    def test_usain_and_nick(self):
        tournament = runner_and_tournament.Tournament(90, self.usain, self.nick)
        results = tournament.start()
        self.__class__.all_results['Usain_vs_Nick'] = results

        self.assertTrue(results[max(results)].name == "Ник")

    def test_andrey_and_nick(self):
        # Турнир с Андреем и Ником на дистанцию 90
        tournament = runner_and_tournament.Tournament(90, self.andrey, self.nick)
        results = tournament.start()
        self.__class__.all_results['Andrey_vs_Nick'] = results

        self.assertTrue(results[max(results)].name == "Ник")

    def test_usain_andrey_and_nick(self):
        tournament = runner_and_tournament.Tournament(90, self.usain, self.andrey, self.nick)
        results = tournament.start()
        self.__class__.all_results['Usain_Andrey_vs_Nick'] = results

        self.assertTrue(results[max(results)].name == "Ник")


if __name__ == '__main__':
    unittest.main()
