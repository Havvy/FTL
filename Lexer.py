"""Flux Lexer
    requirements: Python 3

    Flux is an attempt to create kinder markup language than WikiMedia's
    WikiCode, and this Lexer is the beginning.

    For more information, visit the project's wiki:
        http://flux.referata.com/
"""

from FTL import Tokens


def char_stream(txt):
    """Yields a stream of characters from a given text file"""
    with open(txt) as stream:
        for line in stream:
            for char in line:
                yield char


def flux_tokenizer(stream=char_stream, fluxor='parse_me.txt'):
    """Reads characters from a stream
       Characters are matched against tokens and a list
       of tokens is returned.
    """

    previous_state = current = Tokens.FLUX_INIT()
    token_stream = []

    for char in stream(fluxor):
        consumed = current.lookup(current.consumed + char)
        new = consumed if consumed else current.lookup(char)

        if new:
            previous_state = current
            current = new(char)
            token_stream.append(previous_state)
        else:
            current.consumed += char

        #TODO: Used for presentations, remove for production
        print(current)

    token_stream.append(current)
    token_stream.append(Tokens.EOF())
    return token_stream

if __name__ == '__main__':
    print([str(x) for x in flux_tokenizer()])
