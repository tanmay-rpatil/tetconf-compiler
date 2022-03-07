# tetlexer.py

from sly import Lexer

class tetLexer(Lexer):
    # Set of token names
    tokens = {EOS, COMMA, NUM, STR, BOOL, COMMENT, EOL, DIMS, SOUND, PCS, K_KEY, SPEED, BIAS, DISCO, GHOST, SCORE, OPEN_ROUND, CLOSE_ROUND, OPEN_CURLY, CLOSE_CURLY, OPEN_SQUARE, CLOSE_SQUARE, PLUS, MINUS, MULT, DIVI, ASSIGN, LT, GT, LE, GE, NE}

    # String containing ignored characters between tokens
    ignore = ' \t'

    # Regular expression rules for tokens
    EOS = r';'
    COMMA = r','
    NUM = r'[0-9]+'
    STR = r'\"[0-9A-Za-z_ \t]\"'
    BOOL = r'(ON|OFF)'
    COMMENT = r'//[.]*'
    EOL = r'\n'
    DIMS = r'board'
    SOUND = r'sound'
    PCS = r'pieces'
    K_KEY = r'(rotate|go_left|go_right|soft_drop|hard_drop|pause)'
    SPEED = r'speed'
    BIAS = r'pga_bias'
    DISCO = r'disco_mode'
    GHOST = r'ghost_mode'
    SCORE = r'scoring'
    WELCOME = r'opening_msg'
    GAMEOVER = r'ending_msg'
    OPEN_ROUND = r'\('
    CLOSE_ROUND = r'\)'
    OPEN_CURLY = r'\{'
    CLOSE_CURLY = r'\}'
    OPEN_SQUARE = r'\['
    CLOSE_SQUARE = r'\]'
    PLUS = r'\+'
    MINUS = r'-'
    MULT = r'\*'
    DIVI = r'/'
    ASSIGN = r'='
    LE = r'<='
    GE = r'>='
    LT = r'<'
    GT = r'>'
    NE = r'<>'
    