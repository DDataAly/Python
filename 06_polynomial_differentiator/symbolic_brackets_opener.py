import simple_differentiator

def extract_pre_bracket_operand(expression):
    pre_bracket_operand, no_operand_expression = simple_differentiator.first_symbol_analyser
    return(pre_bracket_operand, no_operand_expression)

def extract_pre_bracket_coefficient(expression):
    pre_bracket_coefficient = simple_differentiator.monomial_coefficient_parser (expression)
    return(pre_bracket_coefficient)



def extract_expression_in_brackets(expression):
    open_bracket_index = expression.find('(')
    close_bracket_index = expression.rfind(')')
    expression_in_brackets=expression[(open_bracket_index + 1): close_bracket_index]
    return(expression_in_brackets)



# def remove_coefficient_from_monomial (monomial): #What is this about?
#     if monomial[0] in ('+','-'):
#         monomial = monomial[1:]
#     if monomial.isdigit():
#         return('')
#     else:
#         for i,symbol in enumerate(monomial):
#             if symbol.isalpha() or symbol == '(':
#                 break
#         base_start_index=i
      
#     monomial_without_coefficient = monomial[base_start_index:]
#     return(monomial_without_coefficient)


def transform_expression_to_polynomial(expression): 
    pre_bracket_operand, no_operand_expression = extract_pre_bracket_operand(expression)
    pre_bracket_coefficient = extract_pre_bracket_coefficient(no_operand_expression)
    




    monomials_in_brackets = simple_differentiator.polynomial_parser(expression_in_brackets)
    polynomial = ''

    for monomial in monomials_in_brackets:
        monomial_operand,monomial = simple_differentiator.first_symbol_analyser(monomial)
        print(f'Monomial operand is {monomial_operand}')

        print(f'monomial  without operand is {monomial}')
        monomial_coefficient = simple_differentiator.monomial_coefficient_parser(monomial)
        print(f'Original monomial coefficient is {monomial_coefficient}')
        monomial_without_coefficient = remove_coefficient_from_monomial(monomial)
        print(f'Monomial without the coefficient {monomial_without_coefficient}')

        new_monomial_coefficient = str(pre_bracket_coefficient * monomial_coefficient)
        print(f'New monomial coefficient {new_monomial_coefficient}')

        
        new_monomial = monomial_operand + new_monomial_coefficient + monomial_without_coefficient
        print(f'New monomial {new_monomial}')
        polynomial+=new_monomial

    return(polynomial)    


s='-3(x+1)'
k=pre_bracket_coefficient(s)

b=extract_expression_in_brackets(s)

p=transform_expression_to_polynomial(k,b)
print(p)





# s='(x+1)'
# sign=extract_pre_bracket_sign(s)
# coefficient=extract_pre_bracket_coefficient(s)
# print(f'Sign is {sign}, coefficient is {coefficient}')   
# p=extract_expression_in_brackets(s)
# print(f'Expression in the brackets is {p}')
# print(simple_differentiator.polynomial_parser(p))     
        


# def extract_pre_bracket_sign(expression):
#     if expression[0] == '-':
#         pre_bracket_sign = '-'
#     else:
#         pre_bracket_sign = '+'
#     return(pre_bracket_sign)

# def extract_pre_bracket_coefficient(expression):
#     open_bracket_index = expression.find('(')
#     if expression[0].isdigit():
#         pre_bracket_coefficient = expression[0:open_bracket_index]
#     elif open_bracket_index in (0,1):
#         pre_bracket_coefficient = 1
#     else:
#         pre_bracket_coefficient = expression[1:open_bracket_index]
#     return(pre_bracket_coefficient)



# def bracket_counter(opens, closes, symbol):
#     if symbol=='(':
#         opens+=1
#     if symbol==')':
#         closes+=1 
#     return opens, closes   

# def is_plus_or_minus(symbol):
#     return symbol in ['+', '-']

# def polynomial_parser(input_string):
#     parsed_polynomial=[]
#     i=0
#     while i<len(input_string):
#         monomial=''
#         opens,closes=0,0
#         for symbol in input_string[i: len(input_string)]:
#             i+=1
#             opens, closes=bracket_counter(opens,closes, symbol)
#             if all ([
#                 monomial,
#                 is_plus_or_minus(symbol),
#                 opens==closes
#                 ]): 
#                     i=i-1
#                     break 
#             else:
#                 monomial+=symbol   
#         parsed_polynomial.append(monomial)
#     return parsed_polynomial

# def monomial_coefficient_parser(monomial):
#     coefficient=''
#     for symbol in monomial:
#         if symbol.isdigit() or symbol in ('+','-'):
#             coefficient+=symbol
#         else:
#             break
    
#     if coefficient=='-':
#         coefficient='-1'
#     elif coefficient=='+':
#         coefficient='+1'    
    
#     return int(coefficient) if coefficient else 1      


# def monomial_base_parser(monomial):
#     for i,symbol in enumerate(monomial):
#         if symbol.isalpha() or symbol=='(':
#             break
#     base_start_index=i

#     power_symbol_index=monomial.find('^')
#     base_end_index=power_symbol_index if power_symbol_index!=-1 else len(monomial)           
#     base=monomial[base_start_index:base_end_index]
#     return base


# def monomial_exponent_parser(monomial):
#     power_index=monomial.rfind('^')
#     try:
#         exponent= int(monomial[power_index+1:]) if power_index!=-1 else 1
#     except ValueError:
#             exponent=1
#     return exponent   

# def first_symbol_analyser(monomial):
#     if monomial[0] in ('+','-'):
#         monomial_operand=monomial[0] 
#         monomial=monomial[1:]
#     else:
#         monomial_operand='' 
#     return(monomial_operand, monomial)     

# def differentiate_monomial(monomial, monomial_operand):
#     coefficient=monomial_coefficient_parser(monomial)
#     base=monomial_base_parser(monomial)
#     exponent=monomial_exponent_parser(monomial)

#     print(f'Monomial operand is {monomial_operand}')
#     print(f'Coef is {coefficient}')
#     print(f'Base is {base}')
#     print(f'Exp is {exponent}')

#     if exponent==1:
#         return(monomial_operand+str(coefficient))

#     derivative_coefficient=str(coefficient*exponent)

#     if exponent==2:
#         return(monomial_operand+derivative_coefficient+base)

#     derivative_exponent=str(exponent-1)

#     return(monomial_operand+derivative_coefficient+base+'^'+derivative_exponent)         

# def monomial_contains_brackets(monomial):
#     for symbol in monomial:
#         if symbol == '(':
#             return(True)
#         else:
#             return(False)    

# def monomial_has_exponent (monomial):
#     close_bracket_index = monomial.rfind(')') 
#     monomial_exponent_index = monomial.rfind('^')
#     if monomial_exponent_index > close_bracket_index:
#         return(True)
#     else:
#         return (False)               

# def monomial_brackets_remover(monomial,monomial_operand):
#     open_bracket_index=monomial.find('(')
#     closed_bracket_index=monomial.rfind(')')
#     monomial=monomial[0:open_bracket_index]+monomial[open_bracket_index+1:closed_bracket_index]
#     parsed_monomial=polynomial_parser(monomial)
#     monomial=''
#     if monomial_operand=='-':
#         for submonomial in parsed_monomial: 
#             if submonomial[0]=='-':
#                 submonomial='+'+ submonomial[1:]
#             elif submonomial[0]=='+':
#                 submonomial='-'+submonomial[1:]
#             else: 
#                 submonomial='-'+submonomial    
#             monomial+=str(submonomial)    
#     else:
#         for submonomial in parsed_monomial:
#             if submonomial[0].isalpha() or submonomial[0].isdigit():
#                 submonomial='+'+submonomial
#             monomial+=str(submonomial)    
#     return (monomial)



# def monomial_differentiator(monomial):
#     monomial_operand,monomial=first_symbol_analyser(monomial)
#     if monomial.isdigit():
#         return('')
#     else:
#         if not monomial_contains_brackets:
#             differentiate_monomial(monomial, monomial_operand)
#         else:
#             if monomial_has_exponent(monomial):
#                 differentiate_monomial(monomial, monomial_operand)    
#             else:
#                 inner_polynomial=monomial_brackets_remover(monomial, monomial_operand)
#                 differentiate_polynomial(inner_polynomial)

# def output_plus_sign_remover (polynomial_derivative):
#     formatted_derivative=''.join(symbol for symbol in polynomial_derivative[1:] if symbol.isdigit())
#     if len(polynomial_derivative[1:])==len(formatted_derivative):
#         polynomial_derivative=formatted_derivative
#     return(polynomial_derivative)    



# def differentiate_polynomial(input_string):
#     polynomial_derivative=''
    
#     parsed_polynomial=polynomial_parser(input_string)
#     for monomial in parsed_polynomial:
#         print(f'This is monomial {monomial}')
#         monomial_derivative=differentiate_monomial(monomial)
#         print(f'This is the derivative {monomial_derivative}')
#         polynomial_derivative+=monomial_derivative
#     if not polynomial_derivative:
#         return('') 
       
#     if polynomial_derivative[0]=='+':
#         polynomial_derivative = output_plus_sign_remover (polynomial_derivative)

#     return(polynomial_derivative)    


          

# s='-14x'
# m=differentiate_polynomial(s)
# print(m)





# # user_input=input('Please enter a polynomial: ')
# # derivative=differentiate_polynomial(user_input)
# # if derivative:
# #     print(f'The derivative of this polynomial is \n{derivative}')
# # else:
# #     print(f'The derivative of this polynomial is 0')



    