import re

class Lexer:
    def __init__(self, token_specification):
        # Compile the regex pattern from the token specification
        tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)
        self.get_token = re.compile(tok_regex).finditer

    def tokenize(self, code):
        tokens = []
        line_num = 1
        line_start = 0
        for match in self.get_token(code):
            kind = match.lastgroup
            value = match.group()
            if kind != 'WHITESPACE':  # Ignore whitespace
                # Calculate line number and position
                start_pos = match.start()
                while True:
                    line_end = code.find('\n', line_start)
                    if line_end == -1 or line_end > start_pos:
                        break
                    line_start = line_end + 1
                    line_num += 1
                column = start_pos - line_start + 1
                tokens.append((kind, value, line_num, column))
        return tokens