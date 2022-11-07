from sly import Lexer

class KLexer(Lexer):
    
    tokens = {
        'PROG',
        'MAIN',
        'VAR',
        'FUNC',                 # func
        'ID',
        'INT',
        'FLOAT',
        'STRING',
        'BOOL',
        'TRUE',
        'FALSE',
        'IF',                   # if
        'THEN',                 # then
        'ELSE',                 # else
        'FOR',                  # for
        'TO',                   # to
        'WHILE',                # while
        'ARROW',                # arrow
        'COMMENT',              # //
        'EQEQ',                 # ==
        'GOETHAN',              # >=          
        'LOETHAN',              # <=
        'DIFF',                 # !=
        'AND',                  # &&
        'OR'                    # ||
    }

    reserved = {
        'program'       : 'PROGRAM',
        'main'          : 'MAIN',
        'var'           : 'VAR',
        'if'            : 'IF',
        'else'          : 'ELSE',
        'function'      : 'FUNC',
        'return'        : 'RETURN',
        'input'         : 'INPUT',
        'print'        : 'OUTPUT',
        'int'           : 'INT',
        'float'         : 'FLOAT',
        'string'        : 'STRING',
        'bool'          : 'BOOL',
        'true'          : 'TRUE',
        'false'         : 'FALSE',
        'while'         : 'WHILE'
    }

    ignore = '\t'

    literals = { 
        '=', 
        '+', 
        '-', 
        '*', 
        '/', 
        '(', 
        ')', 
        ',', 
        ';', 
        '.', 
        ' ', 
        ':',
        '[',
        ']',
        '{',
        '}'
        }

    PROG = r'program'
    MAIN = r'main'
    VAR = r'var'
    FUNC = r'function'
    IF = r'if'
    THEN = r'then'
    ELSE = r'else'
    FOR = r'for'
    TO = r'to'
    WHILE = r'while'
    TRUE = r'true'
    FALSE = r'false'
    ARROW = r'->'

    EQEQ = r'=='
    GOETHAN = r'>='
    LOETHAN = r'<='
    DIFF = r'!='
    AND = r'&&'
    OR = r'\|\|'

    # Keywords

    PROG = r'program'
    MAIN = r'main'
    VAR = r'var'
    FUNC = r'function'
    IF = r'if'
    THEN = r'then'
    ELSE = r'else'
    FOR = r'for'
    TO = r'to'
    WHILE = r'while'
    TRUE = r'true'
    FALSE = r'false'
    ARROW = r'->'

    EQEQ = r'=='
    GOETHAN = r'>='
    LOETHAN = r'<='
    DIFF = r'!='
    AND = r'&&'
    OR = r'\|\|'

    @_(r'\".*?\"')
    def STRING(self, t):
        t.value = str(t.value)
        return t

    @_(r'\d+\.\d*')
    def FLOAT(self, t):
        t.value = float(t.value)
        return t

    @_(r'\d+')
    def INT(self, t):
        t.value = int(t.value)
        return t

    @_(r'[a-zA-Z_][a-zA-Z_0-9]*')
    def ID(self, t):
        t.type = self.reserved.get(t.value, 'ID')
        return t

    @_(r'//.*')
    def COMMENT(self, t):
        pass

    @_(r' ')
    def space(self, t):
        pass

    @_(r'\n+')
    def newline(self, t):
        self.lineno = t.value.count('\n')