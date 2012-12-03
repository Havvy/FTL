import tempfile
import pytest
import os

from FTL import lexer
from FTL import tokens

# Example files
examples = '../examples'

# Combines a file to be Lexed and the expected token stream
# for a number of example files
test_result_pairs = (
    (os.path.join(examples, 'complex function.flux'),
     [tokens.AT(consumed='@', start=0, end=1),
      tokens.TEXT(consumed='outer', start=1, end=6),
      tokens.OPEN_PAREN(consumed='(', start=6, end=7),
      tokens.AT(consumed='@', start=7, end=8),
      tokens.TEXT(consumed='inner', start=8, end=13),
      tokens.OPEN_PAREN(consumed='(', start=13, end=14),
      tokens.TEXT(consumed='"anonymous quoted parameter"', start=14, end=42),
      tokens.CLOSE_PAREN(consumed=')', start=42, end=43),
      tokens.COMMA(consumed=',', start=43, end=44),
      tokens.TEXT(consumed=' name', start=44, end=49),
      tokens.EQUALS(consumed='=', start=49, end=50),
      tokens.TEXT(consumed='value', start=50, end=55),
      tokens.CLOSE_PAREN(consumed=')', start=55, end=56)]),

    (os.path.join(examples, 'escape code.flux'),
     [tokens.ESCAPED(consumed='\\H', start=0, end=2),
      tokens.TEXT(consumed='i', start=2, end=3),
      tokens.OPEN_PAREN(consumed='(', start=3, end=4),
      tokens.CLOSE_PAREN(consumed=')', start=4, end=5),
      tokens.TEXT(consumed=' ', start=5, end=6),
      tokens.AT(consumed='@', start=6, end=7),
      tokens.TEXT(consumed='template', start=7, end=15),
      tokens.OPEN_PAREN(consumed='(', start=15, end=16),
      tokens.TEXT(consumed='arg', start=16, end=19),
      tokens.CLOSE_PAREN(consumed=')', start=19, end=20),
      tokens.TEXT(consumed=' and a ', start=20, end=27),
      tokens.VARIABLE(consumed='%variable', start=27, end=36),
      tokens.NEW_LINE(consumed='\n', start=36, end=37)]),

    (os.path.join(examples, 'function.flux'),
     [tokens.AT(consumed='@', start=0, end=1),
      tokens.TEXT(consumed='function', start=1, end=9),
      tokens.OPEN_PAREN(consumed='(', start=9, end=10),
      tokens.CLOSE_PAREN(consumed=')', start=10, end=11)]),

    (os.path.join(examples, 'function with arguments.flux'),
     [tokens.AT(consumed='@', start=0, end=1),
      tokens.TEXT(consumed='template', start=1, end=9),
      tokens.OPEN_PAREN(consumed='(', start=9, end=10),
      tokens.TEXT(consumed='testamajin', start=10, end=20),
      tokens.COMMA(consumed=',', start=20, end=21),
      tokens.TEXT(consumed=' argument1 ', start=21, end=32),
      tokens.EQUALS(consumed='=', start=32, end=33),
      tokens.TEXT(consumed=' 23', start=33, end=36),
      tokens.CLOSE_PAREN(consumed=')', start=36, end=37),
      tokens.NEW_LINE(consumed='\n', start=37, end=38)]),

    (os.path.join(examples, 'link.flux'),
     [tokens.OPEN_ILINK(consumed='[[', start=0, end=2),
     tokens.TEXT(consumed='http://testamjest.com| testamajest',
                 start=2, end=36),
     tokens.CLOSE_ILINK(consumed=']]', start=36, end=38),
     tokens.NEW_LINE(consumed='\n', start=38, end=39)]),

    (os.path.join(examples, 'nested function.flux'),
     [tokens.OPEN_PAREN(consumed='(', start=0, end=1),
     tokens.AT(consumed='@', start=1, end=2),
     tokens.TEXT(consumed='A', start=2, end=3),
     tokens.OPEN_PAREN(consumed='(', start=3, end=4),
     tokens.AT(consumed='@', start=4, end=5),
     tokens.TEXT(consumed='B', start=5, end=6),
     tokens.OPEN_PAREN(consumed='(', start=6, end=7),
     tokens.CLOSE_PAREN(consumed=')', start=7, end=8),
     tokens.CLOSE_PAREN(consumed=')', start=8, end=9),
     tokens.CLOSE_PAREN(consumed=')', start=9, end=10),
     tokens.NEW_LINE(consumed='\n', start=10, end=11)]))


# Facilities for use when debugging errors in tests
def compare_streams(actual, expected):
    for act_token, exp_token in zip(actual, expected):
        for attrib in ("consumed", "start", "end"):
            if getattr(act_token, attrib) != getattr(exp_token, attrib):
                print("Expected {}, found {} in {}.{}".format(
                    getattr(exp_token, attrib),
                    getattr(act_token, attrib),
                    type(act_token),
                    attrib))
            else:
                print("Good here!")


@pytest.mark.parametrize(('char_stream', 'token_stream'), test_result_pairs)
def test_Tokenize(char_stream, token_stream):
    assert lexer.tokenize(char_stream) == token_stream


class TestCharStream():
    def setup_read(self):
        name = os.path.join(tempfile.mkdtemp(), 'CharStreamTest.txt')
        with open(name, 'w') as read:
            read.write('abcd')

        return name

    def teardown_read(self, read):
        os.remove(read)

    def pytest_funcarg__read(self, request):
        """Creates and returns a temp file for reading"""
        return request.cached_setup(self.setup_read, self.teardown_read,
                                    scope='class')
