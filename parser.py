from nodes import Assignment, Print

def parse(tokens):
    ast = []
    i = 0
    while i < len(tokens):
        if tokens[i][1] == 'dekh':
            var = tokens[i+1][1]
            if tokens[i+2][0] == 'EQUALS':
                if tokens[i+3][0] == 'NUMBER':
                    value = tokens[i+3][1]
                    ast.append(Assignment(var, value))
                    i += 4
                elif tokens[i+3][0] == 'IDENT' and tokens[i+4][0] == 'PLUS' and tokens[i+5][0] == 'IDENT':
                    value = ('PLUS', tokens[i+3][1], tokens[i+5][1])
                    ast.append(Assignment(var, value))
                    i += 6
                else:
                    i += 1
            else:
                i += 1
        elif tokens[i][0] == 'IDENT' and tokens[i+1][1] == 'ke' and tokens[i+2][1] == 'chhaap':
            ast.append(Print(tokens[i][1]))
            i += 3
        else:
            i += 1
    return ast
