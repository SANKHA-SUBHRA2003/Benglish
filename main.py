import sys
from lexer import tokenize
from parser import parse
from interpreter import interpreter

def run_benglish_file(filename):
    with open(filename, 'r') as f:
        code = f.read()
    tokens = tokenize(code)
    ast = parse(tokens)
    interpreter(ast)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_benglish_file>")
    else:
        run_benglish_file(sys.argv[1])
