%{
	#include "calc.tab.h"
	int yylval;
%}

%%

/* board dimsensions */
board						{ return(DIMS); }

/* messages */
opening_msg 				{ return(WELCOME); }
ending_msg 					{ return(GAMEOVER); }
pieces 						{ return(PCS); }

[ \t]+ 						{  }
\n 							{ return(EOL); }
"//".* 						{ return(COMMENT); }

/* data types */
[0-9]+ 						{ yylval = atoi(yytext); return(NUM); }
\"([0-9]|[A-Za-z]|_| |\t)*\" 	{ return(STRING); }
#([A-Fa-f0-9]{6}) 			{ return(COLOR); }
@[A-Za-z_][A-Za-z_0-9]*@	{ return(MACRO); }

/* key bindings */
rotate_left 				{ return(ROTATE); }
go_left 					{ yylval = LEFT; return(MOVE); }
go_right 					{ yylval = RIGHT; return(MOVE); }
soft_drop 					{ yylval = SOFT; return(DROP); }
hard_drop 					{ yylval = HARD; return(DROP); }
pause 						{ return(PAUSE); }

/* Toggles */
ghost 						{ return(GHOST); }
sound 						{ return(SOUND); }
difficulty 					{ return(DIFFICULTY); }
scoring 					{ return(SCORING); }

/* Brackets */
"("  						{ return OPEN_ROUND; }
")"  						{ return CLOSE_ROUND; }
"["  						{ return OPEN_SQUARE; }
"]"  						{ return CLOSE_SQUARE; }
"{"  						{ return OPEN_CURLY; }
"}"  						{ return CLOSE_CURLY; }

/* Arithmetic operators */
"+"  						{ yylval = ADD; return = (ARITH); }
"-"  						{ yylval = SUB; return = (ARITH); }
"*"  						{ yylval = MUL; return = (ARITH); }
"/"  						{ yylval = DIV; return = (ARITH); }

/* Relational operators */
"<" 						{ yylval = LT; return = (RELOP); }
">" 						{ yylval = GT; return = (RELOP); }
"=" 						{ yylval = EQ; return = (RELOP); }
"<="						{ yylval = LE; return = (RELOP); }
">="						{ yylval = GE; return = (RELOP); }
"<>"						{ yylval = NE; return = (RELOP); }

%%
