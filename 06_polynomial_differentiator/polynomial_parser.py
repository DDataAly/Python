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
        expression_operand=expression[0] 
        expression = expression[1:]
    else:
        expression_operand = '+'  
    return(expression_operand, expression)     


def expression_coefficient_parser(expression):
    coefficient = ''
    for symbol in expression:
        if symbol.isdigit():  
            coefficient+=symbol
        else:
            break  
    return int(coefficient) if coefficient else 1      


def extract_pre_bracket_operand(expression):
    pre_bracket_operand, no_operand_expression = first_symbol_analyser(expression)
    return(pre_bracket_operand, no_operand_expression)


def extract_pre_bracket_coefficient(expression):
    pre_bracket_coefficient = expression_coefficient_parser (expression)
    return(int(pre_bracket_coefficient))


def extract_expression_in_brackets(expression):
    open_bracket_index = expression.find('(')
    close_bracket_index = expression.rfind(')')
    expression_in_brackets=expression[(open_bracket_index + 1): close_bracket_index]
    return expression_in_brackets


def extract_expression_base(no_operand_expression, expression_coefficient):
    if no_operand_expression.isdigit():
        return('')
    elif expression_coefficient == 1:
        expression_base = no_operand_expression
    else:
        len_coefficient = len(str(expression_coefficient))    
        expression_base = no_operand_expression[len_coefficient:]
    return expression_base   


def calculate_expression_operand_no_brackets (expression, expression_operand, pre_bracket_operand):
    if ((pre_bracket_operand == '+' and expression_operand == '+')
        or (pre_bracket_operand == '-' and expression_operand == '-')):
        new_expression_operand = '+'
    else:
        new_expression_operand = '-' 
    return new_expression_operand

    
def calculate_open_brackets_expression(expression,pre_bracket_coefficient, pre_bracket_operand):
    expression_operand, no_operand_expression = first_symbol_analyser(expression)
    expression_coefficient = expression_coefficient_parser(no_operand_expression)
    expression_base = extract_expression_base(no_operand_expression, expression_coefficient)

    new_expression_coefficient = str(pre_bracket_coefficient * expression_coefficient)
    new_expression_operand = calculate_expression_operand_no_brackets(expression,expression_operand,pre_bracket_operand)
    new_expression = new_expression_operand + new_expression_coefficient + expression_base
    return new_expression

def open_brackets_expression(expression): 
    pre_bracket_operand, no_operand_expression = extract_pre_bracket_operand(expression)
    pre_bracket_coefficient = extract_pre_bracket_coefficient(no_operand_expression)
    polynomial_in_brackets = extract_expression_in_brackets (expression)
    parsed_polynomial_in_brackets = parse_polynomial(polynomial_in_brackets)
   
    new_polynomial = ''
    for expression in parsed_polynomial_in_brackets:
        new_expression = calculate_open_brackets_expression(expression, pre_bracket_coefficient,pre_bracket_operand)
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
 

# if __name__ =="__main__":         
#     input_string ='-6x^2+11-7(x+2)'
#     print(input_string)
#     print(polynomial_to_differentiate(input_string))
