# tetlexer.py
 
from sly import Lexer
 
class tetLexer(Lexer):
    # Set of token names
    tokens = {EOS, COMMA, NUM, STR, BOOL, COMMENT, EOL, DIMS, SOUND, PCS, K_KEY, SPEED, PGA_BIAS, DISCO_MODE, GHOST_MODE, SCORING, OPENING_MSG, ENDING_MSG, OPEN_BRACKET, CLOSE_BRACKET, ARITHOP, ASSIGN, RELOP, COLOR}
 
    # String containing ignored characters between tokens
    ignore = ' \t'
 
    # Regular expression rules for tokens
    EOS = r';'
    COMMA = r','
    NUM = r'[0-9]+'
    STR = r'\".*?\"'
    BOOL = r'(ON|OFF)'
    COMMENT = r'//.*'
    EOL = r'\n'
    DIMS = r'board'
    SOUND = r'sound'
    PCS = r'pieces'
    K_KEY = r'(rotate|go_left|go_right|soft_drop|hard_drop|pause)'
    SPEED = r'speed'
    PGA_BIAS = r'pga_bias'
    DISCO_MODE = r'disco_mode'
    GHOST_MODE = r'ghost_mode'
    SCORING = r'scoring'
    OPENING_MSG = r'opening_msg'
    ENDING_MSG = r'ending_msg'
    OPEN_BRACKET = r'(\(|\[|\{)'
    CLOSE_BRACKET = r'(\)|\]|\})'
    ARITHOP = r'(\+|-|\*|/)'
    ASSIGN = r'='
    RELOP = r'(<=|>=|<|>|<>)'
    COLOR = r'#([0-9a-fA-F]{6})'
    
if __name__ == '__main__':
    i = 1
    with open('tet_conf.tads', 'r') as fileh:
        
        lines = fileh.readlines()
        lexer = tetLexer()
        for data in lines:
            print("Line #",i)
            for tok in lexer.tokenize(data):
                print('\tt<%r>,%r' % (tok.type, tok.value))
            i+=1