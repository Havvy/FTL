class Token():

    def __init__(self, consumed):
        self.consumed = consumed

    @classmethod
    def equals(cls, other):
        return isinstance(other, cls)

    @classmethod
    def name(cls):
        return cls.__name__


class TEXT(Token):
    pattern = "."


class AT(Token):
    pattern = "\@"


class OPEN_PAREN(Token):
    pattern = "\("


class CLOSE_PAREN(Token):
    pattern = "\)"


class COMMA(Token):
    pattern = ","


class ESCAPED(Token):
    pattern = "\\\[\S]"


class EQUALS(Token):
    pattern = "="


class NEW_LINE(Token):
    pattern = "\n"


class VARIABLE(Token):
    pattern = "%\w+(?=\W)"


class OPEN_ILINK(Token):
    pattern = "\[\["


class CLOSE_ILINK(Token):
    pattern = "\]\]"


class OPEN_ELINK(Token):
    pattern = "(?<!\[)\[(?!\[)"


class CLOSE_ELINK(Token):
    pattern = "(?<!\])\](?!\])"


tokens = (AT, CLOSE_ILINK, CLOSE_PAREN, COMMA, EQUALS, ESCAPED, NEW_LINE,
          OPEN_ILINK, OPEN_PAREN, VARIABLE, OPEN_ELINK, CLOSE_ELINK)
