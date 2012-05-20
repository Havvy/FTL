"""Module of token classes used in the Lexer/Parser"""


import re
debug = True

# Defining regular expressions
open_paren = "\("
close_paren = "\)"
not_close_paren = "^[^)]$"
new_line = "\n"
comma = ","
text = "[a-zA-Z0-9 ]"
at = "\@"
equals = "="

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
        for key in self.table: #.keys() not needed in Py3.
            #if debug:
            #    print('-----------------------')
            #    print("Value: {}, Key: {}".format(value, key))
            #    print(re.findall(key, value))
            #    print('-----------------------')
            if re.findall(key, value):
                return self.table[key]


# Skeleton tokens, actually defined afterwards.
class NEW_LINE(Token):
    pass


class ARG_COMMA(Token):
    pass


class ARG_EQUALS(Token):
    pass


class DEFAULT_ARG(Token):
    pass


class TEMPLATE_CLOSE_PAREN(Token):
    pass


class TEMPLATE_OPEN_PAREN(Token):
    pass


class AT_TEXT(Token):
    pass


class AT(Token):
    """The @ character was read"""
    pass


class ARG(Token):
    pass


class EOF(Token):
    """End of file token ends each token stream"""
    pass


class FLUX_INIT(Token):
    """The first token added to the token stream"""
    pass


#Tables! 'cause cyclic dependencies suck
NEW_LINE.table = {close_paren: TEMPLATE_CLOSE_PAREN}

ARG_COMMA.table = {comma: ARG, new_line: NEW_LINE, not_close_paren: ARG}

ARG_EQUALS.table = {"^[^ ]$": DEFAULT_ARG}

TEMPLATE_CLOSE_PAREN.table = {new_line: NEW_LINE}

TEMPLATE_OPEN_PAREN.table = {close_paren: TEMPLATE_CLOSE_PAREN, new_line: NEW_LINE,
                            not_close_paren: ARG}

AT_TEXT.table = {"template\(": TEMPLATE_OPEN_PAREN, new_line: NEW_LINE}

AT.table = {text: AT_TEXT, new_line: NEW_LINE}

ARG.table = {close_paren: TEMPLATE_CLOSE_PAREN, new_line: NEW_LINE,
            comma: ARG_COMMA, equals: ARG_EQUALS}

DEFAULT_ARG.table = {comma: ARG_COMMA, close_paren: TEMPLATE_CLOSE_PAREN}

EOF.table = {}

FLUX_INIT.table = {at: AT, new_line: NEW_LINE}
