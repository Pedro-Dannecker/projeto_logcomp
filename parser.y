%{
#include <iostream>
#include <string>
extern int yylex();
void yyerror(const char *s) { printf("ERROR: %sn", s); }

%}

%union {
    std::string* string;
}

%token <string> TIDENTIFIER TNUMBER TLBRACE TRBRACE
%token <string> TEQUAL TPLUS TMINUS TMUL TDIV
%token <string> TCEQ TCNE TCLT TCLE TCGT TCGE
%token <string> TLPAREN TRPAREN  TDOT TCOMMA

%type <string> expression statement_list game_block point_block


%start program

%{
    int player1_score = 0;
    int player2_score = 0;
    int player1_games = 0;
    int player2_games = 0;
    int current_player = 1; // Inicia com o Player 1
%}

%%

program:
    | program game
    ;

game:
    TIDENTIFIER TLBRACE game_block TRBRACE
    {
        std::cout << "Game comecou!\n";
        std::cout << "Player 1 Games: " << player1_games << " | Player 2 Games: " << player2_games << std::endl;
        delete $3; 
    }
    ;

game_block:
    | game_block point_block
    {
        
        if (player1_games >= 6 || player2_games >= 6) {
            std::cout << "Partida finalizada\n";
            if (player1_games > player2_games) {
                std::cout << "Player 1 ganhou a partida\n";
            } else if (player2_games > player1_games) {
                std::cout << "Player 2 ganhou a partida\n";
            } else {
                
            }
            // Nova partida
            player1_score = 0;
            player2_score = 0;
            player1_games = 0;
            player2_games = 0;
        }
    }
    ;

point_block:
    TLBRACE statement_list TRBRACE
    {
        std::cout << "Ponto comecou \n";
        delete $2; 
        if (player1_score >= 40 || player2_score >= 40) {
            std::cout << "Game terminou\n";
            if (player1_score > player2_score) {
                std::cout << "Player 1 ganhou o game\n";
                player1_games++;
            } else if (player2_score > player1_score) {
                std::cout << "Player 2 ganhou o game\n";
                player2_games++;
            } else {
            }
            // Novo game
            player1_score = 0;
            player2_score = 0;
        }
    }
    ;

statement_list:
    | statement_list statement
    ;

statement:
    expression TCOMMA 
    {
        std::cout << "Action: " << $1 << std::endl; 
        if (*$1 == "venceu") {
            std::cout << "Ponto finalizado\n";
        
            if (current_player == 1) {
                std::cout << "Player 1 venceu o ponto\n";
                player1_score += 15;
            } else {
                std::cout << "Player 2 venceu o ponto\n";
                player2_score += 15;
            }
            // Alternar para o próximo jogador
            current_player = (current_player == 1) ? 2 : 1;
        }
        std::cout << "Player 1 Pontos: " << player1_score << " | Player 2 Pontos: " << player2_score << std::endl;
        
    }
    | expression 
    {
        std::cout << "Action: " << $1 << std::endl; 
    }
    ;

expression:
    TIDENTIFIER 
    {
        $$ = *$1;
    }
    | TNUMBER 
    {
        $$ = *$1;
    }
    ;

%%

extern "C" int yylex();
extern "C" int yyparse();
