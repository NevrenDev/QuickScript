import re
from pathlib import Path

# Token types
TOKEN_TYPES = {
    'MULTICOMMENT_START': r'#\{"',
    'MULTICOMMENT_END': r'"\}',
    'COMMENT': r'#.*',
    'LBRACE': r'\{',
    'RBRACE': r'\}',
    'COLON': r':',
    'STRING': r'"(.*?)"',
    'FLOAT': r'\d+\.\d+',
    'INT': r'\d+',
    'IDENT': r'[a-zA-Z_][\w\.]*',
    'WHITESPACE': r'[ \t\n\r]+',
}

# Token regex
TOKEN_REGEX = re.compile('|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_TYPES.items()))

# Class for tokens so I can get values like this: token.type
class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value
    def __repr__(self):
        return f"Token({self.type}, {self.value!r})"

# Class for parsed tokens so I can get values with parsed.args
class DotDict:
    def __init__(self, data):
        for key, value in data.items():
            if isinstance(value, dict):
                value = DotDict(value)
            self.__dict__[key] = value

    def __getitem__(self, key):
        return self.__dict__[key]

    def __repr__(self):
        return f"DotDict({self.__dict__})"

# Tokenizer which takes words from .qsx and sorts them for the parser
def tokenize(text: Path):
    text = text.read_text()
    tokens = []
    pos = 0
    in_multiline_comment = False
    while pos < len(text):
        if in_multiline_comment:
            end_match = re.match(TOKEN_TYPES['MULTICOMMENT_END'], text[pos:])
            if end_match:
                in_multiline_comment = False
                pos += len(end_match.group(0))
                continue
            pos += 1
            continue

        match = TOKEN_REGEX.match(text, pos)
        if not match:
            raise SyntaxError(f"Unexpected character: {text[pos]!r} at position {pos}")

        type_ = match.lastgroup
        value = match.group(type_)

        if type_ == 'WHITESPACE' or type_ == 'COMMENT':
            pass  # skip whitespace and single-line comments
        elif type_ == 'MULTICOMMENT_START':
            in_multiline_comment = True
        else:
            tokens.append(Token(type_, value))

        pos = match.end()
    return tokens

# Parser, makes the gibberish from .qsx make sens
def parse(tokens):
    def parse_block(index):
        result = {}
        key = None
        values_only = []

        while index < len(tokens):
            token = tokens[index]

            if token.type == 'RBRACE':
                if values_only:
                    return values_only, index + 1
                return result, index + 1

            if token.type == 'IDENT':
                key_parts = token.value.split(".")
                index += 1
                if index >= len(tokens) or tokens[index].type != 'COLON':
                    raise SyntaxError("Expected ':' after identifier")
                index += 1
                if index >= len(tokens):
                    raise SyntaxError("Unexpected end of input after ':'")
                value_token = tokens[index]

                if value_token.type == 'LBRACE':
                    index += 1
                    value, index = parse_block(index)
                elif value_token.type in {'STRING', 'INT', 'FLOAT', 'IDENT'}:
                    value = value_token.value
                    if value_token.type == 'INT':
                        value = int(value)
                    elif value_token.type == 'FLOAT':
                        value = float(value)
                    index += 1
                else:
                    raise SyntaxError(f"Unexpected token {value_token.type} after colon")

                current = result
                for part in key_parts[:-1]:
                    if part not in current or not isinstance(current[part], dict):
                        current[part] = {}
                    current = current[part]
                current[key_parts[-1]] = value

            elif token.type in {'STRING', 'INT', 'FLOAT'}:
                val = token.value
                if token.type == 'INT':
                    val = int(val)
                elif token.type == 'FLOAT':
                    val = float(val)
                values_only.append(val)
                index += 1
            else:
                index += 1

        if values_only:
            return "\n".join(values_only), index
        return result, index

    index = 0
    ast = {}

    while index < len(tokens):
        token = tokens[index]
        if token.type == 'IDENT':
            key = token.value
            index += 1
            if index >= len(tokens) or tokens[index].type != 'COLON':
                raise SyntaxError("Expected ':' after top-level identifier")
            index += 1
            if index >= len(tokens) or tokens[index].type != 'LBRACE':
                raise SyntaxError("Expected '{' after top-level ':'")
            index += 1
            value, index = parse_block(index)
            ast[key] = value
        else:
            index += 1

    return DotDict(ast)
