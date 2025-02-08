def bracket_counter(opens, closes, symbol):
    if symbol == '(':
        opens += 1
    if symbol == ')':
        closes += 1 
    return opens, closes   


def is_plus_or_minus(symbol):
    return symbol in ['+', '-']


def polynomial_parser(input_string):
    parsed_polynomial = []
    i = 0
    while i < len(input_string):
        monomial = ''
        opens,closes = 0,0
        for symbol in input_string[i: len(input_string)]:
            i += 1
            opens, closes=bracket_counter(opens,closes, symbol)
            if monomial and is_plus_or_minus(symbol) and opens == closes:
                i = i-1
                break 
            else:
                monomial += symbol   
        parsed_polynomial.append(monomial)
    return parsed_polynomial


def monomial_coefficient_parser(monomial):
    coefficient = ''
    for symbol in monomial:
        if symbol.isdigit() or symbol in ('+','-'):
            coefficient+=symbol
        else:
            break
    if coefficient == '-':
        coefficient = '-1'
    elif coefficient == '+':
        coefficient = '+1'    
    return int(coefficient) if coefficient else 1      


def monomial_base_parser(monomial):
    for i,symbol in enumerate(monomial):
        if symbol.isalpha() or symbol == '(':
            break
    base_start_index=i

    power_symbol_index = monomial.find('^')
    base_end_index = power_symbol_index if power_symbol_index!=-1 else len(monomial)           
    base = monomial[base_start_index:base_end_index]
    return base


def monomial_exponent_parser(monomial):
    power_index = monomial.rfind('^')
    exponent = int(monomial[power_index + 1:]) if power_index != -1 else 1
    return exponent   


def first_symbol_analyser(monomial):
    if monomial[0] in ('+','-'):
        monomial_operand=monomial[0] 
        monomial = monomial[1:]
    else:
        monomial_operand = '' 
    return(monomial_operand, monomial)     


def calculate_monomial_derivative(monomial, monomial_operand):
    coefficient = monomial_coefficient_parser(monomial)
    base = monomial_base_parser(monomial)
    exponent = monomial_exponent_parser(monomial)

    print(f'Monomial operand is {monomial_operand}')
    print(f'Coef is {coefficient}')
    print(f'Base is {base}')
    print(f'Exp is {exponent}')

    if exponent == 1:
        return(monomial_operand+str(coefficient))

    derivative_coefficient=str(coefficient * exponent)
    if exponent == 2:
        return(monomial_operand + derivative_coefficient + base)

    derivative_exponent = str(exponent-1)
    return(monomial_operand + derivative_coefficient + base + '^' + derivative_exponent)         


def monomial_differentiator(monomial):
    monomial_operand,monomial = first_symbol_analyser(monomial)
    if monomial.isdigit():
        return('')
    else:
        return(calculate_monomial_derivative(monomial, monomial_operand))


def output_plus_sign_remover (polynomial_derivative):
    formatted_derivative = ''.join(symbol for symbol in polynomial_derivative[1:] if symbol.isdigit())
    if len(polynomial_derivative[1:]) == len(formatted_derivative):
        polynomial_derivative = formatted_derivative
    return(polynomial_derivative)    


def differentiate_polynomial(input_string):
    polynomial_derivative = ''
    parsed_polynomial = polynomial_parser(input_string)
    for monomial in parsed_polynomial:
        print(f'This is monomial {monomial}')
        monomial_derivative = monomial_differentiator(monomial)
        print(f'This is the derivative {monomial_derivative}')
        polynomial_derivative += monomial_derivative
    if not polynomial_derivative:
        return('')  
    if polynomial_derivative[0] == '+':
        polynomial_derivative = output_plus_sign_remover (polynomial_derivative)
    return(polynomial_derivative)    


user_input = input('Please enter a polynomial: ')
derivative = differentiate_polynomial(user_input)
if derivative:
    print(f'The derivative of this polynomial is \n{derivative}')
else:
    print(f'The derivative of this polynomial is 0')

s='-(x+4)^3+11x^5+9x'

    

