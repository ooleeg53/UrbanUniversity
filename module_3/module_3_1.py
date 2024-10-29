calls = 0


def count_calls():
    global calls
    calls = calls + 1


def string_info(string):
    count_calls()
    a = (len(string), string.upper(), string.lower())
    return a


def is_contains(string, list_to_search):
    count_calls()
    c = False
    for search in list_to_search:
        if search.lower() == string.lower():
            c = True
    return c


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
