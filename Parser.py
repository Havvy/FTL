"""Flux Parser
    requirements: Python 3

    Flux is an attempt to create kinder markup language than WikiMedia's
    WikiCode, and this Lexer is the beginning.

    For more information, visit the project's wiki:
        http://flux.referata.com/
"""

from Lexer import (AT, CLOSE_PAREN, COMMA, ESCAPED, EQUALS, NEW_LINE,
                   OPEN_PAREN, PERIOD, TEXT, VARIABLE, OPEN_LINK, CLOSE_LINK)
"""
FLUX
  LINE
    TEMPLATE
    TEXT
    LINK
    LIST_ITEM
      LINK
      TEXT
    VARIABLE
"""


class ALL():
    """Temporary class. This will be replaced when I can think of where
    to best put the damn thing.
    """
    pass


class Node():
    legal_children = (ALL)

    def __init__(self):
        self.children = []

    @property
    @classmethod
    def name(cls):
        return cls.__name__

    @classmethod
    def legal_child(cls, child):
        return child in cls.legal_children

    def add_child(self, child):
        if self.legal_children(child):
            self.children.append(child)


class Flux(Node):
    legal_children = ('Line')


class Line(Node):
    pass


class Template(Node):
    legal_children = ()
    pattern = (AT, ALL)

    def __init__(self, name, *args, **kwargs):
        super()
        self.args = {'name': name}

        count = 1
        for arg in args:
            args[count] = arg

        args.update(kwargs)


class Link(Node):
    legal_children = ()
    pattern = (OPEN_LINK, ALL, CLOSE_LINK)

    def __init__(self, name, dest):
        super()
        self.name = name
        self.destination = dest
        # TODO: This is only good enough for now
        self.local = dest.startswith('http://')


class Text(Node):
    legal_children = ()
    pattern = (TEXT)

    def __init__(self, content):
        super()
        self.content = content

if __name__ == '__main__':
    root = Flux()
    line = Line()

    root.add_child(line)
