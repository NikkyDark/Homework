calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())


def is_contains(string, list_to_search):
    count_calls()
    len(string), string.upper(), string.lower()
    return True if string in list_to_search else False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'Urban']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
