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
    pattern = "(?<!\[)\[(?>!\[)"


class CLOSE_ELINK(Token):
    pattern = "(?<!\])\](?>!\])"


tokens = (TEXT, AT, OPEN_PAREN, CLOSE_PAREN, COMMA, ESCAPED, NEW_LINE,
          VARIABLE, OPEN_ILINK, CLOSE_ILINK, OPEN_ELINK, OPEN_ILINK)
