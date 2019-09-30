grammar STL;

prog	:	stat+
	    ;

stat:   formula NEWLINE                 # textformula
    |   PARAMETERS EQ expr NEWLINE      # assign
    |   NEWLINE                         # blank
    ;

formula: LPAR formula RPAR op=(AND|OR) LPAR formula  RPAR  # AndOr
	|	 NOT LPAR formula  RPAR                            # Not
	|    expr op=(GT|GE|LT|LE|E) expr                        # Atom
	|    LPAR formula RPAR                                 # parensFormula
	|    op =(TRUE|FALSE)                                  # trueFalse
	|	 LPAR formula RPAR U  interval LPAR formula RPAR   # U
	|    F  interval LPAR formula RPAR                     # F
	|	 G  interval LPAR formula RPAR                     # G
	;

expr:   expr op=(MULT|DIV|PLUS|MINUS) expr      # AlgOp
    |   NUMBER                              # number
    |   MINUS NUMBER                        # NegNumber
    |   op=(PARAMETERS|SERIES)              # id
    |   LPAR expr RPAR                      # parensExpr
    ;



interval : LBRAT  expr COMMA  expr RBRAT
	;


PARAMETERS:     [a-z]+ ;
SERIES  :       [A-Z] ([A-Z] | [0-9])* ;

LPAR    :       '(';
RPAR    :       ')';
COMMA   :       ',';
LBRAT   :       '[';
RBRAT   :       ']';
U       :	'U_';
F       :	'F_';
G       :	'G_';

TRUE	:	'True';
FALSE	:	'False';

PLUS	:	'+';
MINUS	:	'-';
MULT	:	'*';
DIV	:	'/';

AND	:	'&';
OR	:	'|';
NOT	:	'!';

EQ	:	'=';
NEQ	:	'!=';
GT	:	'>';
GE	:	'>=';
LT	:	'<';
LE	:	'<=';
E	:	'==';



// $<Terminal

//INTEGER	:	'0'..'9'+
//	;

NUMBER
	:   ('0'..'9')+ ('.')* ('0'..'9')* EXPONENT?
	|   '.' ('0'..'9')+ EXPONENT?
	|   ('0'..'9')+ EXPONENT
	;

fragment
EXPONENT : ('e'|'E') ('+'|'-')? ('0'..'9')+ ;



ID	:	('a'..'z'|'A'..'Z'|'_') ('a'..'z'|'A'..'Z'|'0'..'9'|'_')*
	;

NEWLINE	:	( '\r'| '\n' )
	;

// $>


// $<White space

COMMENT
    :   ('//' ~('\n'|'\r')*)->channel(HIDDEN)
    ;

/* Ignore white space characters, except from newline */
WS
    :   (' ' | '\t' | NEWLINE )->channel(HIDDEN)
    ;
// $>
