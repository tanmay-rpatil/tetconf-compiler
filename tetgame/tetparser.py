from sly import Parser
from tetlexer import tetLexer
import pickle, sys

class tetParser(Parser):

	cnt = 1
	data_map = dict()
	valid_pieces = ['L','I','O','J','Z','S','T']
	valid_key_bindings = ['K_BACKSPACE', 'K_TAB', 'K_CLEAR', 'K_RETURN', 'K_PAUSE', 'K_ESCAPE', 'K_SPACE', 'K_EXCLAIM', 'K_QUOTEDBL', 'K_HASH', 'K_DOLLAR', 'K_AMPERSAND', 'K_QUOTE', 'K_LEFTPAREN', 'K_RIGHTPAREN', 'K_ASTERISK', 'K_PLUS', 'K_COMMA', 'K_MINUS', 'K_PERIOD', 'K_SLASH', 'K_0', 'K_1', 'K_2', 'K_3', 'K_4', 'K_5', 'K_6', 'K_7', 'K_8', 'K_9', 'K_COLON', 'K_SEMICOLON', 'K_LESS', 'K_EQUALS', 'K_GREATER', 'K_QUESTION', 'K_AT', 'K_LEFTBRACKET', 'K_BACKSLASH', 'K_RIGHTBRACKET', 'K_CARET', 'K_UNDERSCORE', 'K_BACKQ', 'K_a', 'K_b', 'K_c', 'K_d', 'K_e', 'K_f', 'K_g', 'K_h', 'K_i', 'K_j', 'K_k', 'K_l', 'K_m', 'K_n', 'K_o', 'K_p', 'K_q', 'K_r', 'K_s', 'K_t', 'K_u', 'K_v', 'K_w', 'K_x', 'K_y', 'K_z', 'K_DELETE', 'K_KP0', 'K_KP1', 'K_KP', 'K_KP3', 'K_KP4', 'K_KP5', 'K_KP6', 'K_KP7', 'K_KP8', 'K_KP9', 'K_KP_PERIOD', 'K_KP_DIVIDE', 'K_KP_MULTIPLY', 'K_KP_MINUS', 'K_KP_PLUS', 'K_KP_ENTER', 'K_KP_EQUALS', 'K_UP', 'K_DOWN', 'K_RIGHT', 'K_LEFT', 'K_INSERT', 'K_HOME', 'K_END', 'K_PAGEUP', 'K_PAGEDOWN', 'K_F1', 'K_F2', 'K_F3', 'K_F4', 'K_F5', 'K_F6', 'K_F7', 'K_F8', 'K_F9', 'K_F10', 'K_F11', 'K_F12', 'K_F13', 'K_F14', 'K_F15', 'K_NUMLOCK', 'K_CAPSLOCK', 'K_SCROLLOCK', 'K_RSHIFT', 'K_LSHIFT', 'K_RCTRL', 'K_LCTRL', 'K_RALT', 'K_LALT', 'K_RMETA', 'K_LMETA', 'K_LSUPER', 'K_RSUPER', 'K_MODE', 'K_HELP', 'K_PRINT', 'K_SYSRE', 'K_BREAK', 'K_MENU', 'K_POWER', 'K_AC_BACK']
	keys_list = ['rotate','go_left','go_right','soft_drop','hard_drop','pause']

	tokens = tetLexer.tokens

	@_('expr_list expr')
	def expr_list(self, p):
		return p

	@_('expr')
	def expr_list(self, p):
		return p

	@_('assign_expr EOS')
	def expr(self,p):
		return p

	@_('EOL')
	def expr(self,p):
		self.cnt += 1
		return p
	
	@_('COMMENT')
	def expr(self,p):
		return p

	########################

	@_('bool_assign')
	def assign_expr(self,p):
		return p

	@_('num_assign')
	def assign_expr(self,p):
		return p

	@_('str_assign')
	def assign_expr(self,p):
		return p

	@_('array_assign')
	def assign_expr(self,p):
		return p
		
	########################

	@_('bool_var ASSIGN BOOL')
	def bool_assign(self,p):
		self.data_map[p.bool_var] = (p.BOOL == "ON")
		# print("bool_var: ", p.bool_var)
		return p

	@_('SOUND')
	def bool_var(self,p):
		return "sound"

	@_('PGA_BIAS')
	def bool_var(self,p):
		return "pga_bias"

	@_('GHOST_MODE')
	def bool_var(self,p):
		return "ghost_mode"

	@_('DISCO_MODE')
	def bool_var(self,p):
		return "disco_mode"

	########################

	@_('num_var ASSIGN NUM')
	def num_assign(self,p):
		self.data_map[p.num_var] = int(p.NUM)
		# print("num_var: ", p.num_var)
		return p

	@_('SPEED')
	def num_var(self,p):
		return "speed"

	########################

	@_('str_var ASSIGN string')
	def str_assign(self,p):
		if(p.string not in self.valid_key_bindings) and (p.str_var in self.keys_list):
			print("\n[syntax error]Invalid key binding: ", p.string, "\nRefer https://www.pygame.org/docs/ref/key.html to check valid key bindings.\n")
			raise Exception("Key spec error")
		self.data_map[p.str_var] = p.string
		# print("str_var: ", p.str_var)
		return p

	@_('K_KEY')
	def str_var(self,p):
		return p.K_KEY

	@_('OPENING_MSG')
	def str_var(self,p):
		return p.OPENING_MSG

	@_('ENDING_MSG')
	def str_var(self,p):
		return p.ENDING_MSG

	########################

	@_('board_set')
	def array_assign(self,p):
		dims = p.board_set
		if(len(dims)!=2):
			print("\n[syntax error] At max 2 dimention can be specified")
			raise Exception('Dims cannot have more than 2 elements')
		self.data_map["rows"] = dims[0]
		self.data_map["cols"] = dims[1]
		# print("array_var: ", "board_set")
		return p

	@_('scoring_set')
	def array_assign(self,p):
		if(len(p.scoring_set)>5):
			print("\n[syntax error] At max 5 scoring levels can be specified")
			raise Exception('Dims cannot have more than 2 elements')
		self.data_map["points"] = p.scoring_set
		# print("array_var: ", "scoring_set")
		return p

	@_('pieces_set')
	def array_assign(self,p):
		if(len(p.pieces_set)>7):
			print("\n[syntax error] At max 7 pieces can be specified")
			raise Exception('Dims cannot have more than 2 elements')
		for pc_spec in p.pieces_set:
			self.data_map[pc_spec[0]] = pc_spec
		# print("array_var: ", "pieces_set")
		return p

	@_('DIMS ASSIGN object_array')
	def board_set(self,p):
		return p.object_array

	@_('SCORING ASSIGN object_array')
	def scoring_set(self,p):
		return p.object_array

	@_('PCS ASSIGN object_array')
	def pieces_set(self,p):
		return p.object_array

	@_('OPEN_BRACKET object_list CLOSE_BRACKET')
	def object_array(self,p):
		if((p.OPEN_BRACKET != '[') or (p.CLOSE_BRACKET != ']')):
			print("\n[syntax error] Invalid bracketing. '[' or ']' should be used for arrays, wrt the following error:")
			raise Exception("Bracketing error")
		return p.object_list

	@_('OPEN_BRACKET CLOSE_BRACKET')
	def object_array(self,p):
		return []

	@_('number_list')
	def object_list(self,p):
		return p.number_list

	@_('piece_list')
	def object_list(self,p):
		return p.piece_list

	@_('number_list COMMA NUM')
	def number_list(self,p):
		num_list = p.number_list
		num_list.append(int(p.NUM))
		return num_list

	@_('NUM')
	def number_list(self,p):
		return [int(p.NUM)]

	@_('piece_list COMMA tuples')
	def piece_list(self,p):
		pcs = p.piece_list
		pcs.append(p.tuples)
		return pcs

	@_('tuples')
	def piece_list(self,p):
		return [p.tuples]

	@_('OPEN_BRACKET string COMMA COLOR CLOSE_BRACKET')
	def tuples(self,p):
		
		if((p.OPEN_BRACKET != '{') or (p.CLOSE_BRACKET != '}')):
			print("\n[syntax error] Invalid bracketing. '{' or '}' should be used for tuples, wrt the following error:")
			raise Exception("Bracketing error")

		elif(p.string not in self.valid_pieces):
			print("\n[syntax error] Invalid piece:",p.string,"valid pieces are:",self.valid_pieces, "wrt the following error:")
			raise Exception("Bracketing error")

		color_hex = str(p.COLOR)
		color_hex_int = []
		for ch in color_hex:
			if ord('0') <= ord(ch) <= ord('9'):
				color_hex_int.append(ord(ch)-ord('0'))
			elif ord('a') <= ord(ch) <= ord('z'):
				color_hex_int.append(ord(ch)-ord('a')+10)
			elif ord('A') <= ord(ch) <= ord('Z'):
				color_hex_int.append(ord(ch)-ord('A')+10)

		color = (color_hex_int[0]*16 + color_hex_int[1],
					color_hex_int[2]*16 + color_hex_int[3],
					color_hex_int[4]*16 + color_hex_int[5])
		# print(color)
		return (p.string, color)

	@_('STR')
	def string(self,p):
		return (p.STR[1:-1])

if __name__ == '__main__':
	lexer = tetLexer()
	parser = tetParser()
	num_args = len(sys.argv)

	# check for cl args
	if(num_args>=2):
		fname = sys.argv[1]
	else:
		print("[error] no filename provided")
		exit(1)
	# check if file exists
	try:
		fh = open(fname,'r')
	except:
		print("[error] in opening file:",fname)
		exit(1)
	fh.close()

	with open(fname, 'r') as fileh:
		lines = fileh.readlines()
		line_count = 1;
		for line in lines:
			try:
				result = parser.parse(lexer.tokenize(line))
			except:
				print("[syntax error] in line #",line_count,":",line, "skipping this line")
			line_count+=1
		print(parser.data_map)
		print("\n[success] Parsed")
		outfile = open('data_map.pkl','wb')
		try:
			pickle.dump(parser.data_map, outfile)
		except:
			print("[error] in pickle")

				
