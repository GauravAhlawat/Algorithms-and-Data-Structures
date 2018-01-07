def infixToPostfix(infixExpr):
    """function to convert infix expression into an Postfix expression"""
    # creating a dictionary for precedence of different operators
    prec = {}
    prec['/'] = 3
    prec['*'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1

    operatorStack = Stack() # stack for storing operators
    postfixList = [] # list for storing the final postfix expression
    tokenList = infixExpr.split()  # tokenising the input expression

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == "(":
            operatorStack.push(token)
        elif token == ")":
            topToken = operatorStack.pop()
            while topToken != ")":
                postfixList.append(topToken)
                topToken = operatorStack.pop()
        else:
            while (not operatorStack.isEmpty()) and (prec[operatorStack.peek()] >= operatorStack.pop()):
                postfixList.append(operatorStack.append())
                operatorStack.push(token)
    while not operatorStack.isEmpty():
        postfixList.append(opStakc.pop())
    return " ".join(postfixList)
