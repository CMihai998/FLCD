%{
#include <stdio.h>
#include <stdlib.h>


#define YYDEBUG 1
%define parse.error verbose
%}

%token IDENTIFIER
%token CONSTANT
%token MAIN
%token IN
%token OUT
%token IF
%token FOR
%token BREAK
%token NUMBER
%token CHAR
%token BOOL
%token TRUE
%token FALSE
%token COLON
%token DOLLAR
%token COMA
%token DOT
%token PLUS
%token MINUS
%token MULTIPLY
%token DIVISION
%token DIVISION_2
%token MOD
%token LEFT_ROUND_PARENTHESIS
%token RIGHT_ROUND_PARENTHESIS
%token LEFT_SQUARE_PARENTHESIS
%token RIGHT_SQUARE_PARENTHESIS
%token LEFT_CURLY_PARENTHESIS
%token RIGHT_CURLY_PARENTHESIS
%token LESS_THAN
%token GREATER_THAN
%token DIFFERENT
%token EQUAL
%token OR
%token AND
%token TOARNA_STANGA
%token TOARNA_DREAPTA
%token AFTER_UITE
%token AFTER_TIPAMI
%token INCREASE
%token DECREASE
%token ASSIGNMENT
%token SMALLER_THAN
%token LARGER_THAN



%start program

%%


program : MAIN stmtlist
cmpstmt : LEFT_CURLY_PARENTHESIS stmtlist RIGHT_CURLY_PARENTHESIS ;
stmtlist : stmt | stmt stmtlist;
stmt : decl DOLLAR | assignment DOLLAR | toarna DOLLAR | iostmt DOLLAR | ifstmt DOLLAR | forstmt DOLLAR | cmpstmt DOLLAR ;
decl : type IDENTIFIER ;
toarna : ASSIGNMENT term TOARNA_STANGA CONSTANT | ASSIGNMENT term TOARNA_DREAPTA CONSTANT | inc_dec;
assignment : ASSIGNMENT term TOARNA_STANGA expression | ASSIGNMENT term TOARNA_DREAPTA expression ;
for_assignment : type term TOARNA_STANGA expression | type term TOARNA_STANGA expression ;
inc_dec : term INCREASE | term DECREASE ;
iostmt : OUT  term | IN term ;
ifstmt : IF LEFT_ROUND_PARENTHESIS condition RIGHT_ROUND_PARENTHESIS cmpstmt ;
forstmt : FOR LEFT_ROUND_PARENTHESIS for_assignment DOLLAR condition DOLLAR assignment RIGHT_ROUND_PARENTHESIS cmpstmt ;
relation : LESS_THAN | GREATER_THAN | DIFFERENT | EQUAL ;
expression : term | term PLUS expression | term MINUS expression | term MULTIPLY expression | term DIVISION expression | term MOD expression | LEFT_ROUND_PARENTHESIS expression RIGHT_SQUARE_PARENTHESIS ;
term : IDENTIFIER | CONSTANT | IDENTIFIER LEFT_SQUARE_PARENTHESIS term RIGHT_SQUARE_PARENTHESIS  ;
type : primitiveType | arrayDeclaration ;
primitiveType : NUMBER | BOOL ;
arrayDeclaration : primitiveType LEFT_SQUARE_PARENTHESIS CONSTANT RIGHT_SQUARE_PARENTHESIS  ;
condition : expression relation expression ;


%%

yyerror(char *s)
{
    printf("%s\n",s);
}

extern FILE *yyin;

main(int argc, char **argv)
{
    if(argc>1) yyin :  fopen(argv[1],"r");
    if(argc>2 && !strcmp(argv[2],"-d")) yydebug: 1;
    if(!yyparse()) fprintf(stderr, "\tO.K.\n");
}