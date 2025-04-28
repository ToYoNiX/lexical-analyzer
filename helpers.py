import re

class Lexer:
    def __init__(self, token_specification):
        # Compile the regex pattern from the token specification
        tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)
        self.get_token = re.compile(tok_regex).finditer

    def tokenize(self, code):
        tokens = []
        for match in self.get_token(code):
            kind = match.lastgroup
            value = match.group()
            if kind != 'WHITESPACE':  # Ignore whitespace
                tokens.append((kind, value))
        return tokens
