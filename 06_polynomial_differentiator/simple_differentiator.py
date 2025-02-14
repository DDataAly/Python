import symbolic_brackets_opener 

def differentiation_base_parser(monomial):
    for i,symbol in enumerate(monomial):
        if symbol.isalpha() or symbol == '(':
            break
    base_start_index=i

    power_symbol_index = monomial.find('^')
    base_end_index = power_symbol_index if power_symbol_index!=-1 else len(monomial)           
    base = monomial[base_start_index:base_end_index]
    return base


def differentiation_exponent_parser(monomial):
    power_index = monomial.rfind('^')
    exponent = int(monomial[power_index + 1:]) if power_index != -1 else 1
    return exponent        


def monomial_differentiator(monomial):
    monomial_operand,monomial = symbolic_brackets_opener.first_symbol_analyser(monomial)
    if monomial.isdigit():
        return('')
    else:
        return(calculate_monomial_derivative(monomial, monomial_operand))
    

def calculate_monomial_derivative(monomial, monomial_operand):
    coefficient = symbolic_brackets_opener.expression_coefficient_parser(monomial)
    base = differentiation_base_parser(monomial)
    exponent = differentiation_exponent_parser(monomial)

    if exponent == 1:
        return(monomial_operand+str(coefficient))

    derivative_coefficient=str(coefficient * exponent)
    if exponent == 2:
        return(monomial_operand + derivative_coefficient + base)

    derivative_exponent = str(exponent-1)
    return(monomial_operand + derivative_coefficient + base + '^' + derivative_exponent)      


def differentiate_polynomial(input_string):
    polynomial_for_diff = symbolic_brackets_opener.polynomial_to_differentiate(input_string)
    parsed_polynomial = symbolic_brackets_opener.parse_polynomial(polynomial_for_diff)
    polynomial_derivative = ''
    for monomial in parsed_polynomial:
        monomial_derivative = monomial_differentiator(monomial)
        polynomial_derivative += monomial_derivative
    if not polynomial_derivative:
        return('')  
    if polynomial_derivative[0] == '+':
        polynomial_derivative = polynomial_derivative[1:]
    return(polynomial_derivative)    



if __name__ =="__main__": 

    user_input = input('Please enter a polynomial: ')
    derivative = differentiate_polynomial(user_input)
    if derivative:
       print(f'The derivative of this polynomial is \n{derivative}')
    else:
        print(f'The derivative of this polynomial is 0')

 