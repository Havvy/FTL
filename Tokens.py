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

    def lookup(self, char):
        """Compared values against regex keys in a Token's table
           If a match is found,
        """
        for regex, token in self.table.items():
            #if debug:
            #    print('-----------------------')
            #    print("Value: {}, Key: {}".format(char, regex))
            #    print(re.findall(regex, char))
            #    print('-----------------------')
            if re.findall(regex, char):
                return token


# Token declarations. Main data declared afterwards.
class NEW_LINE(Token):
    pass


class ARGUMENT_COMMA(Token):
    pass


class ARGUMENT_EQUALS(Token):
    pass


class ANONYMOUS_ARGUMENT(Token):
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


class ARGUMENT(Token):
    pass


class EOF(Token):
    """End of file token ends each token stream"""
    pass


class INIT(Token):
    """The first token added to the token stream"""
    pass


# Tables declared here to allow cyclic dependencies.
NEW_LINE.table = {
    close_paren: TEMPLATE_CLOSE_PAREN
    }

ARGUMENT_COMMA.table = {
    comma: ARGUMENT,
    new_line: NEW_LINE,
    not_close_paren: ARGUMENT}

ARGUMENT_EQUALS.table = {
    "^[^ ]$": ANONYMOUS_ARGUMENT}

TEMPLATE_CLOSE_PAREN.table = {
    new_line: NEW_LINE}

TEMPLATE_OPEN_PAREN.table = {
    close_paren: TEMPLATE_CLOSE_PAREN,
    new_line: NEW_LINE,
    not_close_paren: ARGUMENT}

AT_TEXT.table = {
    "template\(": TEMPLATE_OPEN_PAREN,
    new_line: NEW_LINE}

AT.table = {
    text: AT_TEXT,
    new_line: NEW_LINE}

ARGUMENT.table = {
    close_paren: TEMPLATE_CLOSE_PAREN,
    new_line: NEW_LINE,
    comma: ARGUMENT_COMMA,
    equals: ARGUMENT_EQUALS}

ANONYMOUS_ARGUMENT.table = {
    comma: ARGUMENT_COMMA,
    close_paren: TEMPLATE_CLOSE_PAREN}

EOF.table = {}

INIT.table = {
    at: AT,
    new_line: NEW_LINE}
