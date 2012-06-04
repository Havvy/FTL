"""Flux Lexer
    requirements: Python 3

    Flux is an attempt to create kinder markup language than WikiMedia's
    WikiCode, and this Lexer is the beginning.

    For more information, visit the project's wiki:
        http://flux.referata.com/
"""

from re import findall
from collections import namedtuple


example = 'examples/escape code.flux'


def char_stream(txt):
    """Yields a stream of characters from a given text file"""
    with open(txt) as stream:
        for line in stream:
            for char in line:
                yield char


def tokenize(stream=char_stream, fluxor=example):
    """Reads characters from a stream
       Characters are matched against tokens and a list
       of tokens is returned.
    """
    token_stream = []
    char_buffer = []

    for char in stream(fluxor):
        char_buffer.append(char)
        token_stream.extend(lookup(char_buffer))

    return token_stream


def _extract_occurance(lst, occurance):
    """Treats a list of strings as a single string, searching it for
       the occurances. Matches will be removed from the list. Any
       text found prior to matches will be returned as a string.
    """
    try:
        index = ''.join(lst).find(occurance)
    except TypeError:
        print(lst)
        print(occurance)
        import sys; sys.exit()
    end = index + len(occurance)

    # Grab any text prior to match for return later
    text = lst[:index] if index != 0 else None

    to_remove = lst[:end]
    for char in to_remove:
        lst.remove(char)


    return ''.join(text) if text else None


def lookup(iterable):
    """Examines a buffer and searches for token occurances.
       Results will be extracted from the buffer (mutating it)
       and will be returned in a list in order of occurance.
       Any unmatched characters in the buffer occuring prior
       to matches will be considered as a TEXT token. As such,
       the lookup generator may yield between 0 and 2 tokens.
    """
    for regex in token_table:
        matches = findall(regex, ''.join(iterable))

        if matches:
            match = matches.pop()
            text = _extract_occurance(iterable, match)

            if text:
                yield TEXT(text)

            yield token_table[regex](match)

            break


def pprint_token_stream(stream):
    for token in stream:
        name = token.__doc__.split('(')[0]
        print("{}:: {}".format(name, token.consumed))


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


if __name__ == '__main__':
    with open(example) as to_parse:
        print('\nParsing:' + ''.join(to_parse), end='\n\n')

    pprint_token_stream(tokenize())
