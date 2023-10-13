/* 4aParser.y */

%{
#include <stdio.h>
#include "lex.yy.h"  /* Include the header file for yylex */
%}


int yylex(void);  

void yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
}



%token NUMBER

%%
input: /* empty */
     | exp '\n' { printf("Result: %d\n", $1); }
     ;

exp: term
    | exp '+' term { $$ = $1 + $3; }
    | exp '-' term { $$ = $1 - $3; }
    ;

term: factor
    | term '*' factor { $$ = $1 * $3; }
    | term '/' factor { $$ = $1 / $3; }
    ;

factor: NUMBER
      | '(' exp ')' { $$ = $2; }
      ;
%%

int main() {
    yyparse();
    return 0;
}
