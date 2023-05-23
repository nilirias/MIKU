from sly import Lexer
import sys
import re

class MikuLexer(Lexer):
  reflags = re.IGNORECASE
  tokens = {
    DRAWING, ID, NUMBER, CTE_NUM, WORD, CTE_STR, BOOL, READ, WRITE, IF, ELSE, WHILE, LEFT, RIGHT, FORWARD, CENTER, PEN_UP, PEN_DOWN, FUNC, SUM, SUB, MULT, DIV, TRUE, FALSE, ASSIGN, LESS_THAN, MORE_THAN, DIFFERENT_TO, LESS_OR_EQ_THAN, MORE_OR_EQ_THAN, EQUAL_TO, AND, OR, NEWLINE, COMMA, END, OPEN_PTH, CLOSE_PTH, VOID, OPEN_SQR, CLOSE_SQR, MAIN
  }

  reserved_words = ['drawing', 'number', 'word', 'bool', 'read', 'write', 'if', 'else', 'while', 'left', 'right', 'forward', 'pen_up', 'pen_down', 'center', 'func', 'true', 'false', 'and', 'or', 'end', 'void', 'main']

  ignore = ' \t'
  ignore_comment = r'#.*'

  #ID = r'[a-z][a-z0-9_]*'
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
  LESS_OR_EQ_THAN = r'<='
  MORE_OR_EQ_THAN = r'>='
  COMMA = r','
  OPEN_PTH = r'\('
  CLOSE_PTH = r'\)'
  OPEN_SQR = r'\['
  CLOSE_SQR = r']'
  
  def CTE_NUM(self, token):
    token.value = float(token.value)
    return token

  @_(r'[a-z][a-z0-9_]*')
  def ID(self, t):
    if(t.value.lower() in self.reserved_words):
      t.type = t.value.upper()
    return t
  
  @_(r'\n+')
  def ignore_newline(self, t):
    self.lineno += len(t.value)

  def error(self, t):
        print("ERROR: Illegal character '%s' found" % t.value[0])
        self.index += 1

if __name__ == '__main__':
    lexer = MikuLexer()
    filename = 'test.txt'

    if(len(sys.argv) > 1):
        filename = sys.argv[1]

    with open(filename) as fp:
        for tok in lexer.tokenize(fp.read()):
            print('type=%r, value=%r' % (tok.type, tok.value))