"""Flux Lexer
    requirements: Python 3

    Flux is an attempt to create a kinder markup language than WikiMedia's
    WikiCode, and this Lexer is the beginning of the toolchain.

    For more information, visit the project's wiki:
        http://flux.referata.com/
"""


import argparse
from re import finditer
from copy import copy

from FTL.tokens import tokens, TEXT


example = 'examples/escape code.flux'


def tokenize(fluxor=example):
    """Reads lines from given file path and produces an iterable of tokens"""
    token_stream = []

    with open(fluxor) as stream:
        for line in stream:
            token_stream.extend(lookup(line))

    return token_stream


def lookup(iterable):
    """Creates a list of tokens found in a string

    Creates a list of tokens in order their occurance in the given iterable.
    Any length of characters in the iterable that do not match any token will
    be tokenized as a TEXT token.
    """
    # Find all of the matches and create a list of tokens based on matches
    matches = []
    for token in tokens:
        for match in finditer(token.pattern, iterable):
            matches.append(token(match.group(),
                                 match.start(),
                                 match.end()))

    matches.sort(key=lambda x: x.start)

    # Find any characters in the string that didn't match a token and
    # tokenize them as TEXT and insert them into the list of tokens
    current_index = 0
    added_texts = 0
    for index, match in enumerate(copy(matches)):
        if match.start > current_index:
            matches.insert(index + added_texts,
                           TEXT(iterable[current_index:match.start],
                                current_index,
                                match.start))
            added_texts += 1

        current_index = match.end

    # Catch any unmatched characters that follow the last token as TEXT
    if current_index < len(iterable):
        matches.append(TEXT(iterable[current_index:],
                            current_index,
                            len(iterable)))

    return matches


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
