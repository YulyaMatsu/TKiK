import os

COLORS = {
    'T_KEYWORD': '#569CD6',
    'T_IDENT': '#9CDCFE',
    'T_NUMBER': '#B5CEA8',
    'T_STRING': '#CE9178',
    'T_OP': '#C586C0',
    'T_PUNCT': '#D4D4D4',
    'T_UNKNOWN': '#FF0000' 
}

KEYWORDS = {'let', 'show'}

def scan_and_highlight(input_code):
    pos = 0
    length = len(input_code)
    html_output = "<html><body style='background-color:#1E1E1E; font-family: Consolas, monospace; font-size: 16px;'>\n<pre>\n"

    while pos < length:
        ch = input_code[pos]

        # 1. obsługa białych znaków (dla HTML)
        if ch.isspace():
            space_str = ""
            while pos < length and input_code[pos].isspace():
                space_str += input_code[pos]
                pos += 1
            html_output += space_str
            continue

        # 2. identyfikatory i słowa kluczowe (zaczynają się od litery)
        if ch.isalpha() or ch == '_':
            ident = ""
            while pos < length and (input_code[pos].isalnum() or input_code[pos] == '_'):
                ident += input_code[pos]
                pos += 1
            
            token_type = 'T_KEYWORD' if ident in KEYWORDS else 'T_IDENT'
            html_output += f"<span style='color: {COLORS[token_type]}'>{ident}</span>"
            continue

        # 3. liczby
        if ch.isdigit():
            num = ""
            while pos < length and input_code[pos].isdigit():
                num += input_code[pos]
                pos += 1
            html_output += f"<span style='color: {COLORS['T_NUMBER']}'>{num}</span>"
            continue

        # 4. ciągi znaków (str)
        if ch == '"':
            string_val = '"'
            pos += 1
            while pos < length and input_code[pos] != '"':
                string_val += input_code[pos]
                pos += 1
            if pos < length and input_code[pos] == '"':
                string_val += '"'
                pos += 1
            html_output += f"<span style='color: {COLORS['T_STRING']}'>{string_val}</span>"
            continue

        # 5. operatory
        if ch in "+-*=":
            html_output += f"<span style='color: {COLORS['T_OP']}'>{ch}</span>"
            pos += 1
            continue

        # 6. interpunkcja
        if ch in "();":
            html_output += f"<span style='color: {COLORS['T_PUNCT']}'>{ch}</span>"
            pos += 1
            continue

        # 7. nieznany znak 
        # zamiana nawiasów trójkątnych na encje HTML, aby nie popsuć pliku wyjśc
        safe_ch = ch.replace('<', '&lt;').replace('>', '&gt;')
        html_output += f"<span style='color: {COLORS['T_UNKNOWN']}'>{safe_ch}</span>"
        pos += 1

    html_output += "\n</pre>\n</body></html>"
    return html_output

if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.html"

    if not os.path.exists(input_file):
        with open(input_file, 'w', encoding='utf-8') as f:
            f.write('let wynik = 10 + 20;\nshow("Wynik to:");\nshow(wynik);')

    with open(input_file, 'r', encoding='utf-8') as f:
        source_code = f.read()

    colored_html = scan_and_highlight(source_code)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(colored_html)

    print(f"Sukces! Składnia została pokolorowana i zapisana w pliku: {output_file}")