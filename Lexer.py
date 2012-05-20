"""Flux Lexer
    requirements: Python 3

    Flux is an attempt to create kinder markup language than WikiMedia's
    WikiCode, and this Lexer is the beginning.

    For more information, visit the project's wiki:
        http://flux.referata.com/
"""

from flux import Tokens
debug = True
example = "examples/complex function.flux"

def char_stream(txt):
    """Yields a stream of characters from a given text file"""
    with open(txt) as stream:
        for line in stream:
            for char in line:
                yield char


def tokenize(stream=char_stream,
                   fluxor=example):
    """Reads characters from a stream
       Characters are matched against tokens and a list
       of tokens is returned.
    """

    # Initialize the current state to the initial token.
    state = Tokens.FLUX()
    token_stream = []
    context = []; # Treat as a stack.

    for char in stream(fluxor):
        consumed = state.getNextToken(state.consumed + char)
        # consumed is None if not a token change.
        next_state = consumed if consumed else state.getNextToken(char)

        if next_state:
            # Drop spaces, but instantiate the next Token with the next char.
            token_stream.append(state)
            state = next_state(char) if char != ' ' else next_token()
        else:
            state.consumed += char

        if debug:
            print(state)

    token_stream.append(state)
    token_stream.append(Tokens.EOF())
    return token_stream

if __name__ == '__main__':
    with open(example) as to_parse:
        print('\nParsing:' + ''.join(to_parse), end='\n\n')
    print([str(x) for x in tokenize()])
