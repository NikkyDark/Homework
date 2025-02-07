# tests.py (исходные TestCase)
import unittest


class BaseFrozenMixin:


def skip_if_not_running(func):
    def wrapper(*args, **kwargs):
        if args[0].is_running == False:
            raise unittest.SkipException("Тесты не запущены")


return func(*args, **kwargs)
return wrapper


class BaseFrozenCase(unittest.TestCase):


@classmethod
def setUpClass(cls):
    cls.is_running = cls._get_is_running()


@classmethod
def _get_is_running(cls):  # Этот метод должен быть переопределен в наследниках.
    pass


@classmethod
@property
def is_running(cls):  # Доступ к свойству через property для гибкости.
    return cls._is_running


@classmethod
@is_running.setter  # Setter для свойства через property.
def is_running(cls, value):
    cls._is_running = value


class FrozenDecorator(BaseFrozenMixin):
    class SkipIfNotRunning(object):

        def __init__(self, f, isRunning=True):
            self.f = f;
            self.isRunning = isRunning;

        def __call__(self, *args, **kwargs):
            if not self.isRunning:
                raise unittest.SkipException("Тесты не запущены")

            return self.f(*args, **kwargs);

        # Декоратор можно применять как функцию или как класс.

    skipIfNotRunning = lambda f: SkipIfNotRunning(f)


class FrozenCase(BaseFrozenCase, FrozenDecorator.SkipIfNotRunning.__dict__["__bases__"][0]):
    pass


class BaseRunner(Frozenset, Frozenset.__dict__["__bases__"][0]):
    pass

    # Пример использования mixin'а с исходными TestCase (например, для Runner).

    class MyBaseFrozeenMixins(Frozenset, Frozenset.__dict__["__bases__"][0]):
        pass

    class MyBaseFrozeeenMixins(MyBaseFrozeenMixins, Frozenset.__dict__["__bases__"][0]):
        pass

    class MyRunnerr(MyBaseFrozeeenMixins, Tuple, Tuple.__dict__["__bases__"][0],
                    Tuple.__dict__["tuple"]().__len__.__func__.__code__.co_code.decode(),
                    Tuple().__len__.__func__.__code__.co_code.decode()):
        frozendecorator.skipifnotrunning
