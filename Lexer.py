"""Flux Lexer
    requirements: Python 3

    Flux is an attempt to create kinder markup language than WikiMedia's
    WikiCode, and this Lexer is the beginning.

    For more information, visit the project's wiki:
        http://flux.referata.com/
"""

from flux import Tokens
debug = True

def char_stream(txt):
    """Yields a stream of characters from a given text file"""
    with open(txt) as stream:
        for char in stream:
            yield char


def flux_tokenizer(stream=char_stream,
                   fluxor='examples/function with arguments.flux'):
    """Reads characters from a stream
       Characters are matched against tokens and a list
       of tokens is returned.
    """

    # Initialize the current state to the initial token.
    previous_state = current = Tokens.INIT()
    token_stream = []
    context = []; # Treat as a stack.

    for char in stream(fluxor):
        consumed = current.lookup(current.consumed + char)
        # when is this true/false ?
        new = consumed if consumed else current.lookup(char)

        if new:
            previous_state = current
            # Drop spaces, but instantiate the next Token with the next char.
            current = new(char) if char != ' ' else new()
            token_stream.append(previous_state)
        else:
            current.consumed += char

        if debug:
            print(current)

    token_stream.append(current)
    token_stream.append(Tokens.EOF())
    return token_stream

if __name__ == '__main__':
    with open('./examples/function with arguments.flux') as to_parse:
        print('\nParsing:' + ''.join(to_parse), end='\n\n')
    print([str(x) for x in flux_tokenizer()])
