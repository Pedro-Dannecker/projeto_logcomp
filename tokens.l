%option noyywrap
%{
#include <string>
#include "parser.hpp"
#define SAVE_TOKEN yylval.string = new std::string(yytext, yyleng)
#define TOKEN(t) (yylval.token = t)
extern "C" int yywrap() { }
%}

%%

"saque"                      { char* player_action = "Saque"; TOKEN(player_action); }
"voleio"                     { char* player_action = "Voleio"; TOKEN(player_action); }
"top spin"                   { char* player_action = "Top Spin"; TOKEN(player_action); }
"slice"                      { char* player_action = "Slice"; TOKEN(player_action); }
"flat"                       { char* player_action = "Flat"; TOKEN(player_action); }
"venceu"                     { char* player_action = "Venceu"; TOKEN(player_action); }
"{"                          { TOKEN(TLBRACE); }
"}"                          { TOKEN(TRBRACE); }
","                          { return TOKEN(TCOMMA); }
"+"                          { return TOKEN(TPLUS); }
"-"                          { return TOKEN(TMINUS); }
[ \t]                        ;
[a-zA-Z][a-zA-Z0-9_]*         { SAVE_TOKEN; return TIDENTIFIER; }
[0-9]+(\.[0-9]+)?            { SAVE_TOKEN; return TNUMBER; }


\n                           
.                            { printf("CARACTER DESCONHECIDO: %s\n", yytext); yyterminate(); }
%%

