import polynomial_parser 

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
    monomial_operand,monomial = polynomial_parser.first_symbol_analyser(monomial)
    if monomial.isdigit():
        return('')
    else:
        return(calculate_monomial_derivative(monomial, monomial_operand))
    

def calculate_monomial_derivative(monomial, monomial_operand):
    coef = polynomial_parser.expression_coefficient_parser(monomial)
    base = differentiation_base_parser(monomial)
    exponent = differentiation_exponent_parser(monomial)

    if exponent == 1:
        return(monomial_operand+str(coef))

    derivative_coef=str(coef * exponent)
    if exponent == 2:
        return(monomial_operand + derivative_coef + base)

    derivative_exp = str(exponent-1)
    return(monomial_operand + derivative_coef + base + '^' + derivative_exp)      


def differentiate_polynomial(input_string):
    parsed_polynomial = polynomial_parser.parse_polynomial_for_differentiation(input_string)
    polynomial_derivative = ''
    for monomial in parsed_polynomial:
        monomial_derivative = monomial_differentiator(monomial)
        polynomial_derivative += monomial_derivative
    if not polynomial_derivative:
        return('')  
    if polynomial_derivative[0] == '+':
        polynomial_derivative = polynomial_derivative[1:]
    return polynomial_derivative   



if __name__ =="__main__": 

    user_input = input('Please enter a polynomial: ')
    derivative = differentiate_polynomial(user_input)
    if derivative:
       print(f'The derivative of this polynomial is: {derivative}')
    else:
        print(f'The derivative of this polynomial is 0')


#How could we improve the program?
# - polynomial validation: is given expression a polynomial with one variable?
# - error prevention instructions: we rely on the variable being 1 char not multiple chars
# - improve the output: we currently can get things like 14+9 as output, but it would be nice to get 23 instead
# - brackets opening: we didn't count for a variable being outside brackets, like 14x(x+8)
#                     we didn't count for the brackets containing a monomial with an exponent, like +16(x^2+4)                                      



 