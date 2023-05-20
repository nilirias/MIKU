from sly import Lexer
import re

class MikuLexer(Lexer):
  reflags = re.IGNORECASE
  tokens = {
    PROGRAM, ID, NUMBER, CTE_NUM, STRING, CTE_STR, BOOL, READ, WRITE, IF, ELSE, WHILE, LEFT, RIGHT, FORWARD, CENTER, PEN_UP, PEN_DOWN, FUNC, SUM, SUB, MULT, DIV, TRUE, FALSE, ASSIGN, LESS_THAN, MORE_THAN, DIFFERENT_TO, LESS_OR_EQ_THAN, MORE_OR_EQ_THAN, EQUAL_TO, AND, OR, NEWLINE, COMMA, END, OPEN_PTH, CLOSE_PTH, VOID, OPEN_SQR, CLOSE_SQR, MAIN
  }

reserved_words = {
  'drawing', 'number', 'word', 'bool', 'read', 'write', 'if', 'else', 'while', 'left', 'right', 'forward', 'pen_up', 'pen_down', 'center', 'func', 'true', 'false', 'and', 'or', 'end', 'void', 'main'
}

ignore = ' \t'
ignore_comment = r'#.*'

ID = r'/[a-z][a-z0-9_]*/i'
CTE_NUM = r'-?\d+(\.\d+)*'
CTE_STR = r'\"[^\"\n]*\"'
SUM = r'\+'
SUB = r'\-'
MULT = r'\*'
DIV = r'\/'
EQUAL_TO = r'=='
ASSIGN = r'='
LESS_THAN = r'<'
MORE_THAN = r'>'
DIFFERENT_TO = r'<>'
LESS_OR_EQ = r'<='
MORE_OR_EQ = r'>='
COMMA = r','
OPEN_PTH = r'\('
CLOSE_PTH = r'\)'
OPEN_SQR = r'\['
CLOSE_SQR = r']'