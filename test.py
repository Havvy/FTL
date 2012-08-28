import re
from collections import OrderedDict

#pattern = "%\w+(?!(?!<\\\) )"
#pattern = "%[\w|(?:\\ )]+"
#pattern = "%(\w+(?:\\\ )*)+"
pattern = "%(?:\w|(?:\\\ ))+(?=\W|\Z)"

test_phrases = OrderedDict({'%1': '%1', '%a': '%a', '%ab': '%ab', ',%a': '%a',
                            '%a_b': '%a_b', '%a\ b': '%a\ b', '%a b': '%a',
                            '(%a)': '%a', '%%a': '%a', '%a %': '%a',
                            '10%': None, '\ %': None, ' %a ': '%a',
                            '%2%': '%2', '%variable': '%variable',
                            '%varia ble': '%varia', '%var1': '%var1'})

failed = []
succeed = []

for test, expected in test_phrases.items():
    try:
        matches = re.findall(pattern, test)
        match = matches.pop() if matches else None
        assert match == expected
        succeed.append("Win: In attempting to match '{}', got '{}' and expected '{}'".format(test, match, expected))
    except AssertionError:
        failed.append("Lose: In attempting to match '{}', got '{}' and expected '{}'".format(test, match, expected))

print('\n'.join(failed))
print()
print('\n'.join(succeed))
