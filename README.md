# projeto_logcomp

PROGRAM = { STATEMENT };

BLOCK = "{", "\n", { STATEMENT }, "}";

STATEMENT = ( λ | ASSIGNMENT | PRINT | IF | ID | FOR | VARDEC), "\n" ;

VARDEC = "var", IDENTIFIER, TYPE, (λ | ("=", BOOLEAN_EXPRESSION));

ASSIGNMENT = IDENTIFIER,("=", BOOLEAN_EXPRESSION | "+=",BOOLEAN_EXPRESSION) ;

PRINT = "Println", "(", BOOLEAN_EXPRESSION, ")" ;

IF = "if", BOOLEAN_EXPRESSION, BLOCK, (λ | ("else", BLOCK));

WHILE = "while", BOOLEAN_EXPRESSION, BLOCK ;

FOR = "for", ASSIGNMENT, ";", BOOLEAN_EXPRESSION, ";", ASSIGNMENT, BLOCK;

BOOLEAN_EXPRESSION = BOOLEAN_TERM, {"||", BOOLEAN_TERM}; 

BOOLEAN_TERM = RELATIVE_EXPRESSION, {"&&", RELATIVE_EXPRESSION}; 

RELATIVE_EXPRESSION = EXPRESSION, {("==" | ">" | "<"), EXPRESSION}; 

EXPRESSION = TERM, { ("+" | "-" | "."), TERM } ;

TERM = FACTOR, { ("*" | "/"), FACTOR } ;

FACTOR = (("+" | "-" | "!"), FACTOR) | NUMBER | STRING | PLAYER_ACTIONS | ("(", BOOLEAN_EXPRESSION, ")") | IDENTIFIER | ("Scanln", "(", ")") ;

IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;

TYPE = "int" | "string";

PLAYER_ACTIONS = "saque"|"voleio"|"top spin"|"slice"|"flat"|"venceu";

STRING = """, { LETTER }, """;

NUMBER = DIGIT, { DIGIT } ;

LETTER = ( a | ... | z | A | ... | Z ) ;

DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;
