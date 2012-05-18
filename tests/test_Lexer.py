"""Testing module for FTL.Lexer
    requires: PyTest (http://pytest.org)
"""


import os
import tempfile
from FTL import Lexer


class TestTokenizer():
    def setup_template_stream(self):
        def stream(x):
            return (char for char in "@template()\n")
        return stream

    def pytest_funcarg__template_stream(self, request):
        """Create a mock character stream: @template()"""
        return request.cached_setup(self.setup_template_stream,
                scope='function')

    def setup_template_arg_stream(self):
        def stream(x):
            return (char for char in "@template(arg1)\n")
        return stream

    def pytest_funcarg__template_arg_stream(self, request):
        """Create a mock character stream: @template()"""
        return request.cached_setup(self.setup_template_arg_stream,
                scope='function')

    def test_template_lexing(self, template_stream):
        tokens = Lexer.flux_tokenizer(template_stream)
        results = [str(x) for x in tokens]
        print(results)
        assert  results == ['FLUX_INIT::', 'AT::@', 'AT_TEXT::template',
                            'TEMPLATE_OPEN_PAREN::(',
                            'TEMPLATE_CLOSE_PAREN::)',
                            'NEW_LINE::\n', 'EOF::']

    def test_template_arg_lexing(self, template_arg_stream):
        tokens = Lexer.flux_tokenizer(template_arg_stream)
        results = [str(x) for x in tokens]
        print(results)
        assert results == ['FLUX_INIT::', 'AT::@', 'AT_TEXT::template',
                           'TEMPLATE_OPEN_PAREN::(', 'ARG::arg1',
                           'TEMPLATE_CLOSE_PAREN::)', 'NEW_LINE::\n',
                           'EOF::']


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
        assert list(Lexer.char_stream(read)) == ['a', 'b', 'c', 'd']
