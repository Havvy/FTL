from collections import namedtuple

# Tokens
AT = namedtuple("AT", "consumed")
CLOSE_PAREN = namedtuple("CLOSE_PAREN", "consumed")
COMMA = namedtuple("COMMA", "consumed")
ESCAPED = namedtuple("ESCAPED", "consumed")
EQUALS = namedtuple("EQUALS", "consumed")
NEW_LINE = namedtuple("NEW_LINE", "consumed")
OPEN_PAREN = namedtuple("OPEN_PAREN", "consumed")
PERIOD = namedtuple("PERIOD", "consumed")
TEXT = namedtuple("TEXT", "consumed")
VARIABLE = namedtuple("VARIABLE", "consumed")
OPEN_LINK = namedtuple("OPEN_LINK", "consumed")
CLOSE_LINK = namedtuple("CLOSE_LINK", "consumed")


token_table = {"\@": AT,
        "\(": OPEN_PAREN,
        "\)": CLOSE_PAREN,
        "\n": NEW_LINE,
        ",": COMMA,
        "=": EQUALS,
        "\\\[\S]": ESCAPED,
        "%.+(?=(?<!\\\)\s)": VARIABLE,
        "\[\[": OPEN_LINK,
        "\]\]": CLOSE_LINK}
