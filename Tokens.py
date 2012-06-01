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

    def _lookup(self, query):
        for regex, token in table.items():
            if re.match(regex, query):
                return token

    def next(self, char):
        """Compared values against regex keys in a Token's table
            If a match is found,
        """
        for expression in (self.consumed + char, char):
            result = self._lookup(expression)
            if result:
                return result(char)

        return TEXT(char)


# Token declarations. Main data declared afterwards.
class NEW_LINE(Token):
    pass


class FLUX(Token):
    """The first token added to the token stream"""
    pass


class TEXT(Token):
    def next(self, char):
        """Text tokens are special and can morph into other token
           types if their consumed text and the passed character
           match in a "next" lookup.
        """
        # Lookup consumed + char
        # <Magic type="force a cast of TEXT into another Token">
        result = self._lookup(self.consumed + char)
        if result and result.__class__ != self.__class__:
            self.__class__ = result
            self.consumed += char
            return TEXT()
        # </Magic>

        # Lookup char
        result = self._lookup(char)
        if result:
            return result(char)
        else:
            return TEXT(char)


class AT(Token):
    pass


class COMMA(Token):
    pass


class PERIOD(Token):
    pass


class PERCENT(Token):
    pass


class OPEN_PAREN(Token):
    pass


class CLOSE_PAREN(Token):
    pass


class ARGUMENT(Token):
    pass


class EQUALS(Token):
    pass


class EOF(Token):
    """End of file token ends each token stream"""
    pass


class ESCAPED(Token):
    pass


table = {"\@": AT,
         "^\($": OPEN_PAREN,
         "\)": CLOSE_PAREN,
         "\n": NEW_LINE,
         ",": COMMA,
         "=": EQUALS,
         "\\\.": ESCAPED,
         "%": PERCENT}
