"""Here lies code that is no longer in use, but may be useful in the future.

        I'm loathe to delete it; I'm loathe to leave it in.
"""


###############################################################################


"""Not a clue what this is attempting to accomplish.

What's the target?

Checks to see if node from a stream is in target. Perhaps
this is an attempt to allow the 'ALL' node to function. If
so, it is unnecessary as the 'ALL' node has an overridden
__eq__ method that handles this.

Came from the parser.
"""

def extra_lex(stream, target):
    for index, token in enumerate(stream):
        ix = index
        for desired in target:
            if isinstance(desired, Node):
                if not stream[ix] == desired:
                    break
            else:
                if not isinstance(stream[ix], desired):
                    break
            ix += 1
        else:
            return index, ix


###############################################################################


"""Variable REGEX Test

A test used to help test out regex against various variable forms
that are considered to be legal in flux.

Iterates through the test_phrases and attempts to match the given
pattern. Output displays successes as "Win" and then failures to match
as "Lose." An example of one such run follows:

    Win: In attempting to match '%a %', got '%a' and expected '%a'
    Win: In attempting to match '%variable', got '%variable' and
         expected '%variable'
    Win: In attempting to match '\ %', got 'None' and expected 'None'
    Win: In attempting to match '%%a', got '%a' and expected '%a'
    Win: In attempting to match '%a b', got '%a' and expected '%a'
    Win: In attempting to match '(%a)', got '%a' and expected '%a'
    Win: In attempting to match '%var1', got '%var1' and expected '%var1'
    Win: In attempting to match '%ab', got '%ab' and expected '%ab'
    Win: In attempting to match '%a', got '%a' and expected '%a'
    Win: In attempting to match '10%', got 'None' and expected 'None'
    Win: In attempting to match ',%a', got '%a' and expected '%a'
    Win: In attempting to match '%varia ble', got '%varia' and
         expected '%varia'
    Win: In attempting to match '%2%', got '%2' and expected '%2'
    Win: In attempting to match '%a_b', got '%a_b' and expected '%a_b'
    Win: In attempting to match '%a\ b', got '%a\ b' and expected '%a\ b'
    Win: In attempting to match ' %a ', got '%a' and expected '%a'
    Win: In attempting to match '%1', got '%1' and expected '%1'

    Lose: In attempting to match 'Obvious Failure', got '' and expected
          'Cannot match'
"""


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


###############################################################################


"""This is a quick lemma for ensuring that the ALL node will indeed match
any other node when testing a node for membership in a node's legal_children
"""


class ContainerTest():
    def __init__(self, contains=None):
        self.contains = contains if contains else []

    def __contains__(self, item):
        return item in self.contains

    def __iter__(self):
        return iter(self.contains)

    def append(self, other):
        self.contains.append(other)


class ALL():
    def __eq__(self, other):
        return True


if __name__ == '__main__':
    container = ContainerTest()
    item = ALL()
    container.append(item)

    print("foo" in container)


###############################################################################


