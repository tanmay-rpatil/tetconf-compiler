from sly import Parser
from tetlexer import tetLexer
import pickle

class tetParser(Parser):

	cnt = 1
	data_map = dict()

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
		print("bool_var: ", p.bool_var)
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
		print("num_var: ", p.num_var)
		return p

	@_('SPEED')
	def num_var(self,p):
		return "speed"

	########################

	@_('str_var ASSIGN string')
	def str_assign(self,p):
		self.data_map[p.str_var] = p.string
		print("str_var: ", p.str_var)
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
		self.data_map["rows"] = dims[0]
		self.data_map["cols"] = dims[1]
		print("array_var: ", "board_set")
		return p

	@_('scoring_set')
	def array_assign(self,p):
		self.data_map["points"] = p.scoring_set
		print("array_var: ", "scoring_set")
		return p

	@_('pieces_set')
	def array_assign(self,p):
		for pc_spec in p.pieces_set:
			self.data_map[pc_spec[0]] = pc_spec
		print("array_var: ", "pieces_set")
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
		color_hex = str(p.COLOR)
		color_hex_int = []2
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
		return (p.string, color)

	@_('STR')
	def string(self,p):
		return (p.STR[1:-1])

if __name__ == '__main__':
	lexer = tetLexer()
	parser = tetParser()

	with open('tet_conf.tads', 'r') as fileh:
		lines = fileh.readlines()
		line_count = 1;
		for line in lines:
			try:
				result = parser.parse(lexer.tokenize(line))
			except:
				print("Syntax error in line #",line_count,":",line, "skipping this line")
			line_count+=1
		# print(result)
		print(parser.data_map)
				
