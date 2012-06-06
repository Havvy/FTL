import tempfile
import pytest
import os
from flux.Lexer import *
from flux import Lexer

# Example files
examples = '../examples'

# Combines a file to be Lexed and the expected token stream
# for a number of example files
test_result_pairs = (
    (os.path.join(examples, 'complex function.flux'),
    [AT(consumed='@'), TEXT(consumed='outer'), OPEN_PAREN(consumed='('),
     AT(consumed='@'), TEXT(consumed='inner'), OPEN_PAREN(consumed='('),
     TEXT(consumed='"anonymous quoted parameter"'), CLOSE_PAREN(consumed=')'),
     COMMA(consumed=','), TEXT(consumed=' name'), EQUALS(consumed='='),
     TEXT(consumed='value'), CLOSE_PAREN(consumed=')')]),

    (os.path.join(examples, 'escape code.flux'),
    [ESCAPED(consumed='\\H'), TEXT(consumed='i'), OPEN_PAREN(consumed='('),
     CLOSE_PAREN(consumed=')'), TEXT(consumed=' '), AT(consumed='@'),
     TEXT(consumed='template'), OPEN_PAREN(consumed='('),
     TEXT(consumed='arg'), CLOSE_PAREN(consumed=')'),
     TEXT(consumed=' and a '), VARIABLE(consumed='%variable'),
     TEXT(consumed=' or '), VARIABLE(consumed='%v\\ ar\\ iable')]),

    (os.path.join(examples, 'function.flux'),
    [AT(consumed='@'), TEXT(consumed='function'),
     OPEN_PAREN(consumed='('), CLOSE_PAREN(consumed=')')]),

    (os.path.join(examples, 'function with arguments.flux'),
    [AT(consumed='@'), TEXT(consumed='template'), OPEN_PAREN(consumed='('),
     TEXT(consumed='testamajin'), COMMA(consumed=','),
     TEXT(consumed=' argument1 '), EQUALS(consumed='='), TEXT(consumed=' 23'),
     CLOSE_PAREN(consumed=')'), NEW_LINE(consumed='\n')]),

    (os.path.join(examples, 'link.flux'),
    [OPEN_LINK(consumed='[['),
     TEXT(consumed='http://testamjest.com| testamajest'),
     CLOSE_LINK(consumed=']]'), NEW_LINE(consumed='\n')]),

    (os.path.join(examples, 'nested function.flux'),
    [OPEN_PAREN(consumed='('), AT(consumed='@'), TEXT(consumed='A'),
     OPEN_PAREN(consumed='('), AT(consumed='@'), TEXT(consumed='B'),
     OPEN_PAREN(consumed='('), CLOSE_PAREN(consumed=')'),
     CLOSE_PAREN(consumed=')'), CLOSE_PAREN(consumed=')'),
     NEW_LINE(consumed='\n')]))


@pytest.mark.parametrize(('char_stream', 'token_stream'), test_result_pairs)
def test_Tokenize(char_stream, token_stream):
    assert tokenize(fluxor=char_stream) == token_stream


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

    def test_char_stream(self, read):
        assert list(char_stream(read)) == ['a', 'b', 'c', 'd']


class TestExtractOccurance():
    def setup_lst(self):
        return list("Give you the constitution again")

    def pytest_funcarg__lst(self, request):
        """Creates and returns a temp file for reading"""
        return request.cached_setup(self.setup_lst, scope='function')

    def test_extract_from_beginning(self, lst):
        assert Lexer._extract_occurance(lst, 'Give you') == None
        assert lst == list(' the constitution again')

    def test_extract_from_middle(self, lst):
        assert Lexer._extract_occurance(lst,
                'constitution') == 'Give you the '
        assert lst == list(" again")
