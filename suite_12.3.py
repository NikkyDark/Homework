# suite_12_3.py
import unittest
from tests import RunnerTest, TournamentTest


def skip_if_frozen(test_func):
    def wrapper(self):
        if self.is_frozen:
            raise unittest.SkipException('Тесты в этом кейсе заморожены')
        return test_func(self)

    return wrapper


class RunnerTestCase(RunnerTest):
    is_frozen = False

    @skip_if_frozen
    def test_challenge(self):
        super().test_challenge()

    @skip_if_frozen
    def test_run(self):
        super().test_run()

    @skip_if_frozen
    def test_walk(self):
        super().test_walk()


class TournamentTestCase(TournamentTest):
    is_frozen = True

    @skip_if_frozen
    def test_first_tournament(self):
        super().test_first_tournament()

    @skip_if_frozen
    def test_second_tournament(self):
        super().test_second_tournament()

    @skip_if_frozen
    def test_third_tournament(self):
        super().test_third_tournament()


# Создание TestSuite и добавление туда тестов.
runner_suite = unittest.TestSuite([
    RunnerTestCase('test_challenge'),
    RunnerTestCase('test_run'),
    RunnerTestCase('test_walk'),
    TournamentTestCase('test_first_tournament'),
    TournamentTestCase('test_second_tournament'),
    TournamentTestCase('test_third_tournament')
])

# Создание TextTextRunner с verbosity=2.
runner = unittest.TextTestRunner(verbosity=2)

# Запуск TestSuite.
runner.run(runner_suite)
