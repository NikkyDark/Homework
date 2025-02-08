import logging
import rt_with_exceptions as rn
import unittest as un


class RunnerTest(un.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        logging.basicConfig(filename='runner_tests.log', filemode='w', level=logging.INFO, encoding='utf-8',
                            format='%(asctime)s | %(levelname)s | %(message)s')

    @un.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_walk(self):
        try:
            run = rn.Runner(name='Вося', speed=-5)
            print('test_walk:', run.name)
            for i in range(10):
                run.walk()
            self.assertEqual(run.distance, 50)
            logging.info('Тест "test_walk" выполнен успешно', exc_info=True)
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    @un.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_run(self):
        try:
            run = rn.Runner(name=2, speed=5)
            print('test_run:', run.name)
            for i in range(10):
                run.run()
            self.assertEqual(run.distance, 100)
            logging.info('Тест "test_run" выполнен успешно', exc_info=True)
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    @un.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_challenge(self):
        run1 = rn.Runner('Черепаха')
        run2 = rn.Runner('Заяц')
        print(f'test_challenge: {run2} (run) VS {run1} (walk)')
        for i in range(10):
            run1.walk()
            run2.run()
        self.assertNotEqual(run1.distance, run2.distance)


if __name__ == "__main__":
    un.main()