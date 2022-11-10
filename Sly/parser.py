from sly import Parser
from Sly.lexer import KLexer

class KParser(Parser):
    tokens = KLexer.tokens

    stack_dim = []
    stack_params = []
    stack_vars = []
    stack_gvars = []

    call_params = []
    counter_params = 0
    counter = 0

    precedence = (
        ('left', '+', '-'),
        ('left', '*', '/')
    )