import re

def tokenize(code):
    token_specification = [
        ('NUMBER',   r'\d+'),
        ('EQUALS',   r'holo'),
        ('PLUS',     r'\+'),
        ('COMPARE',  r'boro hoy|chhoto hoy'),
        ('KEYWORD',  r'shuru|sesh|dekh|jodi|tahole|jokhon|ke|chhaap|er theke'),
        ('IDENT',    r'[a-zA-Z_]\w*'),
        ('NEWLINE',  r'\n'),
        ('SKIP',     r'[ \t]+'),
    ]
    tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)
    get_token = re.compile(tok_regex).match
    tokens = []
    pos = 0
    while pos < len(code):
        match = get_token(code, pos)
        if match:
            kind = match.lastgroup
            value = match.group()
            if kind == 'NUMBER':
                value = int(value)
            if kind not in ('SKIP', 'NEWLINE'):
                tokens.append((kind, value))
            pos = match.end()
        else:
            raise SyntaxError(f'Unexpected character: {code[pos]}')
    return tokens
