def postfixEval(postfixExpr):
    """function to evaluate the postfix expression"""
    operandStack = Stack() #creating a Stack
    tokenList = postfixExpr.split() #tokenising the input postfix expression

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            operand = token
            result = doMath(operand, operand1, operand2)
            operandStack.push(result)
        return operandStack.pop()

def doMath(operand, operand1, operand2):
    """function to calculate the result of an expression passed to it in the form of
        operator and two operands"""
    if operand == "*":
        return operand1 * operand2
    if operand == "/":
        return operand1 / operand2
    if operand == "+":
        return operand1 + operand2
    else:
        return operand1 - operand2

print(postfixEval('7 8 + 3 2 + /'))
