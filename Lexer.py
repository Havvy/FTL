"""Flux Lexer
    requirements: Python 3

    Flux is an attempt to create kinder markup language than WikiMedia's
    WikiCode, and this Lexer is the beginning.

    For more information, visit the project's wiki:
        http://flux.referata.com/
"""

from flux import Tokens
debug = False
#example = "examples/complex function.flux"
#example = "examples/author.flux"
example = "examples/escape code.flux"

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

    # Initialize the current state to the initial token.
    state = Tokens.FLUX()
    token_stream = []

    for char in stream(fluxor):
        lookup_result = state.next(char)
        next_state = lookup_result

        if isinstance(state, type(next_state)):
            state.consumed += char
            continue

        token_stream.append(state)
        state = next_state

        # DEBUG!
        print("Examining char: {}".format(char))
        print("Current state: {}".format(state))
        print("Next State: {}".format(next_state))
        print("Consumed: {}".format(state.consumed))

    token_stream.append(state)
    token_stream.append(Tokens.EOF())
    return token_stream

if __name__ == '__main__':
    with open(example) as to_parse:
        print('\nParsing:' + ''.join(to_parse), end='\n\n')
    print([str(x) for x in tokenize()])
