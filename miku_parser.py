from sly import Parser
from sly.yacc import _decorator as _
from .miku_lexer import MikuLexer
from .miku_quadruples import Quadruple
from . import miku_semantic_cube as sm

class MikuParser(Parser):
  tokens = MikuLexer.tokens

