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
    return(parsed_polynomial)        


def is_bracket_opening_required(expression):
    open_bracket_index=expression.find('(')
    if open_bracket_index == -1:
        return False
    power_symbol_index = expression.find('^')
    if power_symbol_index !=-1:
        return False
    else:
        return True
    

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
    return(expression_in_brackets)


def extract_expression_base(no_operand_expression, expression_coefficient):
    if expression_coefficient == 1:
        expression_base = no_operand_expression
    else:
        len_coefficient = len(str(expression_coefficient))    
        expression_base = no_operand_expression[len_coefficient:]
    return(expression_base)    


def calculate_expression_operand_no_brackets (expression, expression_operand, pre_bracket_operand):
    if ((pre_bracket_operand == '+' and expression_operand == '+')
        or (pre_bracket_operand == '-' and expression_operand == '-')):
        new_expression_operand = '+'
    else:
        new_expression_operand = '-' 
    return(new_expression_operand)

    
def calculate_open_brackets_expression(expression,pre_bracket_coefficient, pre_bracket_operand):
    expression_operand, no_operand_expression = first_symbol_analyser(expression)
    expression_coefficient = expression_coefficient_parser(no_operand_expression)
    expression_base = extract_expression_base(no_operand_expression, expression_coefficient)

    # print(f'expression is {expression}')
    # print(f'No operand expression is {no_operand_expression}')
    # print(f'expression operand is {expression_operand}')
    # print(f'expression coefficient is {expression_coefficient}')
    # print(f'expression base is {expression_base}')    
    # print('\n')

    new_expression_coefficient = str(pre_bracket_coefficient * expression_coefficient)
    new_expression_operand = calculate_expression_operand_no_brackets(expression,expression_operand,pre_bracket_operand)
    new_expression = new_expression_operand + new_expression_coefficient + expression_base
    return(new_expression)


def open_brackets_expression(expression): 
    pre_bracket_operand, no_operand_expression = extract_pre_bracket_operand(expression)
    pre_bracket_coefficient = extract_pre_bracket_coefficient(no_operand_expression)
    polynomial_in_brackets = extract_expression_in_brackets (expression)
    parsed_polynomial_in_brackets = parse_polynomial(polynomial_in_brackets)
    
    # print(f'Prebracket operand is {pre_bracket_operand}')
    # print(f'Prebracket coefficient is {pre_bracket_coefficient}')
    # print(f'Expression in the brackets {polynomial_in_brackets}')
    # print(f'expressions in the brackets are {parsed_polynomial_in_brackets}')

    new_polynomial = ''
    for expression in parsed_polynomial_in_brackets:
        new_expression = calculate_open_brackets_expression(expression, pre_bracket_coefficient,pre_bracket_operand)
        new_polynomial +=new_expression
    return(new_polynomial)



def polynomial_to_differentiate(input_string):
    polynomial_for_diff = ''
    parsed_polynomial = parse_polynomial(input_string)
    print(parsed_polynomial)
    for expression in parsed_polynomial: 
        if is_bracket_opening_required(expression) == True:
            expression =  open_brackets_expression(expression)       
        polynomial_for_diff += expression   
    return(polynomial_for_diff)        

  


if __name__ =="__main__":         
    input_string ='((x^4+11)^3-2)+8'
    print(input_string)
    print(polynomial_to_differentiate(input_string))



# import simple_differentiator

# def extract_pre_bracket_operand(expression):
#     pre_bracket_operand, no_operand_expression = simple_differentiator.first_symbol_analyser(expression)
#     return(pre_bracket_operand, no_operand_expression)

# def extract_pre_bracket_coefficient(expression):
#     pre_bracket_coefficient = simple_differentiator.monomial_coefficient_parser (expression)
#     return(int(pre_bracket_coefficient))

# def extract_expression_in_brackets(expression):
#     open_bracket_index = expression.find('(')
#     close_bracket_index = expression.rfind(')')
#     expression_in_brackets=expression[(open_bracket_index + 1): close_bracket_index]
#     return(expression_in_brackets)

# def extract_monomial_base(no_operand_monomial, monomial_coefficient):
#     if monomial_coefficient == 1:
#         monomial_base = no_operand_monomial
#     else:
#         len_coefficient = len(str(monomial_coefficient))    
#         monomial_base = no_operand_monomial[len_coefficient:]
#     return(monomial_base)    

# def calculate_monomial_operand_no_brackets (monomial, monomial_operand, pre_bracket_operand):
#     if ((pre_bracket_operand == '+' and monomial_operand == '+')
#         or (pre_bracket_operand == '-' and monomial_operand == '-')):
#         new_monomial_operand = '+'
#     else:
#         new_monomial_operand = '-' 
#     return(new_monomial_operand)

    
# def calculate_open_brackets_monomial(monomial,pre_bracket_coefficient, pre_bracket_operand):
#     monomial_operand, no_operand_monomial = simple_differentiator.first_symbol_analyser(monomial)
#     monomial_coefficient = simple_differentiator.monomial_coefficient_parser(no_operand_monomial)
#     monomial_base = extract_monomial_base(no_operand_monomial, monomial_coefficient)

#     # print(f'Monomial is {monomial}')
#     # print(f'No operand monomial is {no_operand_monomial}')
#     # print(f'Monomial operand is {monomial_operand}')
#     # print(f'Monomial coefficient is {monomial_coefficient}')
#     # print(f'Monomial base is {monomial_base}')    
#     # print('\n')

#     new_monomial_coefficient = str(pre_bracket_coefficient * monomial_coefficient)
#     new_monomial_operand = calculate_monomial_operand_no_brackets(monomial,monomial_operand,pre_bracket_operand)
#     new_monomial = new_monomial_operand + new_monomial_coefficient + monomial_base
#     return(new_monomial)



# def calculate_open_brackets_polynomial(expression): 
#     pre_bracket_operand, no_operand_expression = extract_pre_bracket_operand(expression)
#     pre_bracket_coefficient = extract_pre_bracket_coefficient(no_operand_expression)
#     polynomial_in_brackets = extract_expression_in_brackets (expression)
#     parsed_polynomial_in_brackets = simple_differentiator.polynomial_parser(polynomial_in_brackets)
    
#     # print(f'Prebracket operand is {pre_bracket_operand}')
#     # print(f'Prebracket coefficient is {pre_bracket_coefficient}')
#     # print(f'Expression in the brackets {polynomial_in_brackets}')
#     # print(f'Monomials in the brackets are {parsed_polynomial_in_brackets}')

#     new_polynomial = ''
#     for monomial in parsed_polynomial_in_brackets:
#         new_monomial = calculate_open_brackets_monomial(monomial, pre_bracket_coefficient,pre_bracket_operand)
#         new_polynomial +=new_monomial
#     return(new_polynomial)


# if __name__ =="__main__":         
#     expression='(x+6)'
#     print(expression)
#     print(calculate_open_brackets_polynomial(expression))





