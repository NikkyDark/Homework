import unittest
from runner import Runner, Tournament  # Импортируйте необходимые классы


class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner("Усэйн", speed=10)
        self.andrey = Runner("Андрей", speed=9)
        self.nik = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for key in sorted(cls.all_results.keys()):
            print(f"Результат {key}: {cls.all_results[key]}")

    def test_usain_and_nik(self):
        tournament = Tournament(90, self.usain, self.nik)

        result_dict = tournament.start()

        last_runner_name_in_test_setup_result_dict = list(result_dict.values())[-1].name

        # Проверяем последнего бегуна (должен быть Ник)

        last_participant_in_current_tournament_start_result_list_is_Nick_or_not = self.assertTrue(
            last_runner_name_in_test_setup_result_dict == "Ник"
        )


# исправленный метод для второго кейса:

def test_andrey_and_nik(self):
    tournament = Tournament(90, self.andrey, self.nik)
    result = tournament.start()

    last_participant = list(result.values())[-1]

    assert (last_participant.name == "Ник")


# Аналогично исправьте третий кейс:


def test_usain_andrey_nic(self):
    t = Tournament(90, self.usain, self.andrey, self.nik)
    r = t.start()
    assert (list(r.values())[-1].name == "Ник")
