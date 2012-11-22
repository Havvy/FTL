"""Flux Lexer
    requirements: Python 3

    Flux is an attempt to create kinder markup language than WikiMedia's
    WikiCode, and this Lexer is the beginning.

    For more information, visit the project's wiki:
        http://flux.referata.com/
"""

import argparse
from re import findall

from FTL.tokens import tokens, TEXT


example = 'examples/escape code.flux'


def tokenize(fluxor=example):
    """Reads characters from a stream
       Characters are matched against tokens and a list
       of tokens is returned.
    """
    def characters(txt):
        """Yields a stream of characters from a given text file"""
        with open(txt) as stream:
            for line in stream:
                for char in line:
                    yield char

    token_stream = []
    char_buffer = []

    for char in characters(fluxor):
        char_buffer.append(char)
        token_stream.extend(lookup(char_buffer))

    return token_stream


def _extract_occurance(lst, occurance):
    """Treats a list of strings as a single string, searching it for
       the occurances. Matches will be removed from the list. Any
       text found prior to matches will be returned as a string.
    """
    index = ''.join(lst).find(occurance)
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
    for token in tokens:
        matches = findall(token.pattern, ''.join(iterable))

        if matches:
            match = matches.pop()
            text = _extract_occurance(iterable, match)

            if text:
                yield TEXT(text)

            yield token(match)
            break


def pprint_token_stream(stream):
    for token in stream:
        consumed = '(\\n)' if token.consumed == '\n' else token.consumed
        print("{}:: {}".format(token.name(), consumed))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""Description here""")

    # args.to_lex
    # Which file to lex
    parser.add_argument("to_lex", help="File that you wanna lex")

    # args.debug
    # Use logging: http://docs.python.org/py3k/library/logging.html
    parser.add_argument("-D", "--debug", help="Send debug messages to stdout",
                        action="store_true")

    #args.nodoc
    # Will we just drop comment or doc tokens from the stream?
    parser.add_argument("-d", "--nodoc", help="Omit documentation",
                        action="store_true")

    #args.output
    # Just stdout or also stderr?
    parser.add_argument("-o", "--output", help="Redirect output to given file",
                        action="store")

    #args.autodoc
    # Not a clue what this is
    parser.add_argument("-a", "--autodoc", help="Do stuff I don't know yet",
                        action="store")

    args = parser.parse_args()

    with open(args.to_lex) as to_lex:
        print('\nParsing:' + ''.join(to_lex))
        print('\n\n')

    pprint_token_stream(tokenize(args.to_lex))
