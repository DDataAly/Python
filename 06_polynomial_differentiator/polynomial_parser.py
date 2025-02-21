def count_brackets(opens_count, closes_count, symbol):
    if symbol == '(':
        opens_count += 1
    if symbol == ')':
        closes_count += 1 
    return opens_count, closes_count   


def parse_polynomial(input_string):
    parsed_polynomial = []
    expression=''
    opens_count, closes_count = 0,0
    for symbol in input_string:
        opens_count, closes_count = count_brackets(opens_count,closes_count,symbol)
        if symbol in ('+','-') and expression and closes_count == opens_count:
            parsed_polynomial.append(expression) 
            expression = symbol                
        else:
            expression+=symbol    
    parsed_polynomial.append(expression)      
    return parsed_polynomial       


def is_bracket_opening_required(expression):
    return expression[len(expression)-1] == ')'
    

def first_symbol_analyser(expression):
    if expression[0] in ('+','-'):
        expr_operand=expression[0] 
        expression = expression[1:]
    else:
        expr_operand = '+'  
    return(expr_operand, expression)     


def expression_coefficient_parser(expression):
    coefficient = ''
    for symbol in expression:
        if symbol.isdigit():  
            coefficient+=symbol
        else:
            break  
    return int(coefficient) if coefficient else 1      


def extract_pre_bracket_operand(expression):
    pre_bracket_operand, no_operand_expr = first_symbol_analyser(expression)
    return(pre_bracket_operand, no_operand_expr)


def extract_pre_bracket_coefficient(expression):
    pre_bracket_coef = expression_coefficient_parser (expression)
    return(int(pre_bracket_coef))


def extract_expression_in_brackets(expression):
    open_bracket_index = expression.find('(')
    close_bracket_index = expression.rfind(')')
    expr_in_brackets=expression[(open_bracket_index + 1): close_bracket_index]
    return expr_in_brackets


def extract_expression_base(no_operand_expr, expr_coefficient):
    if expr_coefficient == 1 and not no_operand_expr.startswith('1'):
        expr_base = no_operand_expr
    else:
        len_coefficient = len(str(expr_coefficient))    
        expr_base = no_operand_expr[len_coefficient:]
    return expr_base   


def calculate_open_brackets_expression(expression,pre_bracket_coef, pre_bracket_operand):
    expr_operand, no_operand_expr = first_symbol_analyser(expression)
    expr_coef = expression_coefficient_parser(no_operand_expr)
    expr_base = extract_expression_base(no_operand_expr, expr_coef)

    new_expr_coef = str(pre_bracket_coef * expr_coef)
    new_expr_operand = '+' if (pre_bracket_operand == expr_operand) else '-'
    new_expr = new_expr_operand + new_expr_coef + expr_base
    return new_expr


def open_brackets_expression(expression): 
    pre_bracket_operand, no_operand_expr = extract_pre_bracket_operand(expression)
    pre_bracket_coef = extract_pre_bracket_coefficient(no_operand_expr)
    polynomial_in_brackets = extract_expression_in_brackets (expression)
    parsed_polynomial_in_brackets = parse_polynomial(polynomial_in_brackets)
   
    new_polynomial = ''
    for expression in parsed_polynomial_in_brackets:
        new_expression = calculate_open_brackets_expression(expression, pre_bracket_coef,pre_bracket_operand)
        new_polynomial +=new_expression
    return new_polynomial


def open_brackets_polynomial(input_string):
    polynomial_open_brackets = ''
    parsed_polynomial = parse_polynomial(input_string)
    for expression in parsed_polynomial: 
        if is_bracket_opening_required(expression) == True:
            expression =  open_brackets_expression(expression)       
        polynomial_open_brackets += expression   
    return polynomial_open_brackets   


def polynomial_to_differentiate(input_string):
    initial_polynomial=input_string
    current_polynomial = open_brackets_polynomial(input_string)
    while initial_polynomial != current_polynomial:
        initial_polynomial = current_polynomial
        current_polynomial = open_brackets_polynomial(current_polynomial)
    return current_polynomial  

def parse_polynomial_for_differentiation(input_string):
    polynomial=polynomial_to_differentiate(input_string)
    parsed_polynomial = parse_polynomial(polynomial)
    return(parsed_polynomial)
 

if __name__ =="__main__":         
    input_string ='-7(1x)'
    print(input_string)
    print(polynomial_to_differentiate(input_string))

