"""Module of token classes used in the Lexer/Parser"""


import re


class Token(object):
    """Base token class
       Each token will have a 'table' of regex keys and associated Tokens,
       and a 'consume' string to keep track of the token's characters
    """
    def __init__(self, char=''):
        self.consumed = char

    def __str__(self):
        """str(Token) => TokenName::CharsConsumed"""
        return str(self.__class__).split('.')[-1][:-2] + '::' + self.consumed

    def lookup(self, value):
        """Compared values against regex keys in a Token's table
           If a match is found,
        """
        for key in self.table.keys():
            if re.match(key, value):
                return self.table[key]


class NEW_LINE(Token):
    table = {}


class TEMPLATE_CLOSE_PAREN(Token):
    table = {'\n': NEW_LINE}


class TEMPLATE_OPEN_PAREN(Token):
    table = {"\)": TEMPLATE_CLOSE_PAREN, '\n': NEW_LINE}


class AT_TEXT(Token):
    table = {"template\(": TEMPLATE_OPEN_PAREN, '\n': NEW_LINE}


class AT(Token):
    """The @ character was read"""
    table = {"[a-zA-Z0-9 ]": AT_TEXT, '\n': NEW_LINE}


class EOF(Token):
    """End of file token ends each token stream"""
    table = {}


class FLUX_INIT(Token):
    """The first token added to the token stream"""
    table = {"\@": AT, '\n': NEW_LINE}
