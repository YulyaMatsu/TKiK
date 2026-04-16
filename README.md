# Prosty język dla nauki algorytmów

1. Założenia programu:
  - Ogólne cele: Stworzenie przejrzystego środowiska do uruchamiania algorytmów bez zbędnego "szumu" składniowego. Język wspiera podstawowe struktury danych i sterowania.

  - Rodzaj translatora: Interpreter

  - Planowany wynik: Program, który po wczytaniu pliku wykonuje obliczenia, obsługuje interakcję z użytkownikiem (wejście/wyjście) i zarządza stanem zmiennych w czasie rzeczywistym.

  - Język implementacji: Python 3.13

  - Sposób realizacji skanera/parsera: Wykorzystanie generatora PLY (Python Lex-Yacc). Skaner bazuje na wyrażeniach regularnych, a parser implementuje gramatykę bezkontekstową typu LALR.

2. Opis tokenów:

| Kod Tokena        | Reguła / Wartość        | Opis                                                         |
|-------------------|------------------------|--------------------------------------------------------------|
| BEGIN             | BEGIN                  | Otwarcie bloku programu                                      |
| END               | END                    | Zamknięcie bloku programu                                    |
| IF                | IF                     | Słowa kluczowe instrukcji warunkowej                         |
| THEN              | THEN                   | Słowo kluczowe (wstęp do bloku prawdy)                       |
| ELSE              | ELSE                   | Słowo kluczowe (blok alternatywny)                           |
| WHILE             | WHILE                  | Początek pętli                                               |
| DO                | DO                     | Wprowadzenie ciała pętli                                     |
| WRITE             | WRITE                  | Instrukcja wyjścia                                           |
| READ              | READ                   | Instrukcja wejścia                                           |
| IDENTIFIER        | [a-zA-Z_][a-zA-Z0-9_]* | Nazwy zmiennych (zaczynające się od litery lub podkreślnika) |
| INTEGER           | [0-9]+                 | Liczby całkowite                                             |
| FLOAT             | [0-9]+\.[0-9]+         | Liczby zmiennoprzecinkowe                                    |
| ASSIGN            | :=                     | Operator przypisania wartości                                |
| RELOP             | =, !=, <, >, <=, >=    | Operatory porównania logicznego (relacyjne)                  |
| ADD_OP            | +, -,                  | Operatory o niskim priorytecie                               |
| MULT_OP           | *, /                   | Operatory o wysokim priorytecie                              |
| LPAREN            | (                      | Nawias otwierający                                           |
| RPAREN            | )                      | Nawias zamykający                                            |
| SEMICOLON         | ;                      | Separator instrukcji                                         |
| DOT               | .                      | Znak kończący strukturę programu                             |
3. Gramatyka formatu:

```ebnf
program     ::= "BEGIN" stmt_list "END" "."
stmt_list   ::= stmt (";" stmt)*

stmt        ::= assign_stmt
              | if_stmt
              | while_stmt
              | io_stmt

assign_stmt ::= IDENTIFIER ":=" expr

if_stmt     ::= "IF" condition "THEN" stmt_list ("ELSE" stmt_list)?

while_stmt  ::= "WHILE" condition "DO" stmt_list

io_stmt     ::= "READ" IDENTIFIER
              | "WRITE" expr

condition   ::= expr RELOP expr

expr        ::= term (("+" | "-") term)*

term        ::= factor (("*" | "/") factor)*

factor      ::= IDENTIFIER
              | INTEGER
              | FLOAT
              | "(" expr ")"
<relop> ::= "=" | "!=" | "<" | ">" | "<=" | ">="

<expression> ::= <term>
               | <expression> "+" <term>
               | <expression> "-" <term>

<term> ::= <factor>
         | <term> "*" <factor>
         | <term> "/" <factor>

<factor> ::= IDENTIFIER
           | INTEGER
           | FLOAT
           | "(" <expression> ")"
