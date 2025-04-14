from nodes import Assignment, Print

def interpreter(ast):
    env = {}
    for stmt in ast:
        if isinstance(stmt, Assignment):
            if isinstance(stmt.value, tuple):
                op, left, right = stmt.value
                left_val = env.get(left, 0)
                right_val = env.get(right, 0)
                if op == 'PLUS':
                    env[stmt.var] = left_val + right_val
            else:
                env[stmt.var] = stmt.value
        elif isinstance(stmt, Print):
            print(env.get(stmt.var, f"{stmt.var} not defined"))
