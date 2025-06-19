import operator

def calculate(expression):
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }

    precedence = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2
    }

    tokens = expression.split()
    values = []
    operators = []

    for token in tokens:
        if token.isdigit():
            values.append(int(token))
        elif token in ops:
            while operators and precedence[token] <= precedence[operators[-1]]:
                op = operators.pop()
                val2 = values.pop()
                val1 = values.pop()
                values.append(ops[op](val1, val2))
            operators.append(token)

    while operators:
        op = operators.pop()
        val2 = values.pop()
        val1 = values.pop()
        values.append(ops[op](val1, val2))

    return values[0]


if __name__ == "__main__":
    expression = "3 + 7 * 2"
    result = calculate(expression)
    print(result)
