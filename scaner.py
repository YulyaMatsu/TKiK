def lexer(text, index):

    length = len(text)

    while index < length and text[index].isspace():
        index += 1

    if index >= length:
        return "END", None, index

    char = text[index]

    if '0' <= char <= '9':
        start = index
        while index < length and '0' <= text[index] <= '9':
            index += 1
        return "INT", text[start:index], index

    if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
        start = index
        while index < length and (
            ('a' <= text[index] <= 'z') or
            ('A' <= text[index] <= 'Z') or
            ('0' <= text[index] <= '9')
        ):
            index += 1
        return "IDENT", text[start:index], index

    operators = {
        '+': "PLUS",
        '-': "MINUS",
        '*': "MUL",
        '/': "DIV",
        '(': "LPAREN",
        ')': "RPAREN"
    }

    if char in operators:
        index += 1
        return operators[char], char, index

    return "ERROR", f"Niepoprawny symbol '{char}' w kolumnie {index+1}", index + 1


expression = "2+3*(76+8/3) + 3*(9-3)"
pos = 0

while pos < len(expression):

    token, value, pos = lexer(expression, pos)

    if token == "ERROR":
        print("BŁĄD:", value)
        continue

    print(f"({token}, '{value}')   kolumna {pos}")
