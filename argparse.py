#TODO: Include means of asking for .flux file to parse.
#TODO: Set this file up as "flux.py" (main)

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

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
