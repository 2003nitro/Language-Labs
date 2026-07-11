#################################################
# Author: Adam Wilkins
# Date Created: 7/10/2026
# Date Updated: 7/10/2026
# Description: Basic calculator application that performs addition, subtraction, multiplication, and division.
#################################################


def Addition(a, b):
    """
    # Author: Adam Wilkins
    # Date Created: 7/10/2026
    # Purpose: This function takes two numbers as input and returns their sum.
    """
    return a + b

def Subtraction(a, b):
    """
    # Author: Adam Wilkins
    # Date Created: 7/10/2026
    # Purpose: This function takes two numbers as input and returns their difference.
    """
    return a - b

def Multiplication(a, b):
    """
    # Author: Adam Wilkins
    # Date Created: 7/10/2026
    # Purpose: This function takes two numbers as input and returns their product.
    """
    return a * b

def Division(a, b):
    """
    # Author: Adam Wilkins
    # Date Created: 7/10/2026
    # Purpose: This function takes two numbers as input and returns their quotient.
    """
    return a / b

def StrExpressionToValue(expression):
    """
    # Author: Adam Wilkins
    # Date Created: 7/10/2026
    # Purpose: This function takes a string expression as input and returns its value.
    """
    
    expressionList = expression.split(" ")
    while len(expressionList) > 1:

        #******************************************************************************************#
        # If Multiplication or Division is in the expression, it will be evaluated first before Addition or Subtraction.
        if "*" in expressionList: # Multiplication
            signIndex = expressionList.index("*")

            # Adds the result of the multiplication to the expression list and replaces the sign with the result of the multiplication.
            expressionList[signIndex] = str(Multiplication(float(expressionList[signIndex-1]), float(expressionList[signIndex+1])))

            # Removes the two numbers that were multiplied from the expression list.
            expressionList.pop(signIndex+1)
            expressionList.pop(signIndex-1)

        elif "/" in expressionList: # Division
            signIndex = expressionList.index("/")

            # Adds the result of the division to the expression list and replaces the sign with the result of the division.
            expressionList[signIndex] = str(Division(float(expressionList[signIndex-1]), float(expressionList[signIndex+1])))

            # Removes the two numbers that were divided from the expression list.
            expressionList.pop(signIndex+1)
            expressionList.pop(signIndex-1)
        #******************************************************************************************#

        #******************************************************************************************#
        # If Addition or Subtraction is in the expression, it will be evaluated after Multiplication or Division.
        elif "+" in expressionList: # Addition
            signIndex = expressionList.index("+")

            # Adds the result of the addition to the expression list and replaces the sign with the result of the addition.
            expressionList[signIndex] = str(Addition(float(expressionList[signIndex-1]), float(expressionList[signIndex+1])))

            # Removes the two numbers that were added from the expression list.
            expressionList.pop(signIndex+1)
            expressionList.pop(signIndex-1)

        elif "-" in expressionList: # Subtraction
            signIndex = expressionList.index("-")

            # Adds the result of the subtraction to the expression list and replaces the sign with the result of the subtraction.
            expressionList[signIndex] = str(Subtraction(float(expressionList[signIndex-1]), float(expressionList[signIndex+1])))

            # Removes the two numbers that were subtracted from the expression list.
            expressionList.pop(signIndex+1)
            expressionList.pop(signIndex-1)
        #******************************************************************************************#
    
    # When only 1 number is left in the expression list, it is returned as the final result of the expression.
    return expressionList[0]


def ParseParenExpression(expression):
    """
    # Author: Adam Wilkins
    # Date Created: 7/10/2026
    # Purpose: This function checks for parentheses in the expression and evaluates them first before evaluating the rest of the expression.
    """
    while "(" in expression: # Loops for all first level parentheses in the expression and evaluates them first before evaluating the rest of the expression.
        if ")" in expression: # Ensures a closing parenthesis is present before evaluating the expression inside the parentheses.

            # Extracts the expression inside the parentheses and evaluates it.
            parenExpression = expression[expression.index("(")+1:expression.index(")")]
            
            # Replaces the expression inside the parentheses with the result of the expression inside the parentheses.
            expression = expression[:expression.index("(")] + str(StrExpressionToValue  (parenExpression)) +expression[expression.index(")") + 1:]

    return StrExpressionToValue(expression)


def __main__():
    # TODO : Implement a user interface for the calculator that allows users to input expressions and see the results.
    pass