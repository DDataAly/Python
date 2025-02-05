def bracket_counter(opens, closes, symbol):
    if symbol=='(':
        opens+=1
    if symbol==')':
        closes+=1 
    return opens, closes   

def is_plus_or_minus(symbol):
    return symbol in ['+', '-']

def polynomial_parser(input_string):
    parsed_polynomial=[]
    i=0
    while i<len(input_string):
        monomial=''
        opens,closes=0,0
        for symbol in input_string[i: len(input_string)]:
            i+=1
            opens, closes=bracket_counter(opens,closes, symbol)
            if all ([
                monomial,
                is_plus_or_minus(symbol),
                opens==closes
                ]): 
                    i=i-1
                    break 
            else:
                monomial+=symbol   
        parsed_polynomial.append(monomial)
    return parsed_polynomial

def monomial_coefficient_parser(monomial):
    coefficient=''
    for symbol in monomial:
        if symbol.isdigit() or symbol in ('+','-'):
            coefficient+=symbol
        else:
            break
    
    if coefficient=='-':
        coefficient='-1'
    elif coefficient=='+':
        coefficient='+1'    
    
    return int(coefficient) if coefficient else 1      


def monomial_base_parser(monomial):
    for i,symbol in enumerate(monomial):
        if symbol.isalpha() or symbol=='(':
            break
    base_start_index=i

    power_symbol_index=monomial.find('^')
    base_end_index=power_symbol_index if power_symbol_index!=-1 else len(monomial)           
    base=monomial[base_start_index:base_end_index]
    return base


def monomial_exponent_parser(monomial):
    power_index=monomial.find('^')
    exponent= int(monomial[power_index+1:]) if power_index!=-1 else 1
    return exponent       


def monomial_differentiator(monomial):
    if monomial.isdigit():
        return('')
    else:
        coefficient=monomial_coefficient_parser(monomial)
        base=monomial_base_parser(monomial)
        exponent=monomial_exponent_parser(monomial)

        print(f'Coef is {coefficient}')
        print(f'Base is {base}')
        print(f'Exp is {exponent}')

        if exponent==1:
            return(str(coefficient))
        
        derivative_coefficient=str(coefficient*exponent)
        derivative_exponent=str(exponent-1)

        if exponent==2:
            return(derivative_coefficient+base)
            
        return(derivative_coefficient+base+'^'+derivative_exponent)     


def polynomial_differentiator(input_string):
    polynomial_derivative=''
    parsed_polynomial=polynomial_parser(input_string)
    for monomial in parsed_polynomial:
        print(monomial)
        monomial_derivative=monomial_differentiator(monomial)
        print(monomial_derivative)
        polynomial_derivative+=monomial_derivative
    return(polynomial_derivative)    


s='-24'
d=polynomial_differentiator(s)
#print(d)


# user_input=input('Please enter a polynomial: ')
# derivative=polynomial_differentiator(user_input)
# if derivative:
#     print(f'The derivative of this polynomial is \n{derivative}')
# else:
#     print(f'The derivative of this polynomial is 0')



    



# def bracket_counter(opens, closes, symbol):
#     if symbol=='(':
#         opens+=1
#     if symbol==')':
#         closes+=1 
#     return opens, closes   

# def is_plus_or_minus(symbol):
#     return symbol in ['+', '-']


# input_string='23(x+1)^5+3*x^4+6*x+11'
# parsed_polynomial=[]
# i=0
# while i<len(input_string):
#     monomial=''
#     opens,closes=0,0
#     for symbol in input_string[i: len(input_string)]:
#         i+=1
#         opens, closes=bracket_counter(opens,closes, symbol)
#         if is_plus_or_minus(symbol)==False:
#             monomial+= symbol
#         else:
#             if opens>closes:
#                 monomial+=symbol
#             else:
#                 break 
#     parsed_polynomial.append(monomial)


# print(parsed_polynomial)


#https://campus.datacamp.com/courses/writing-efficient-python-code/foundations-for-efficiencies?ex=7

# def bracket_counter(opens, closes, symbol):
#     if symbol=='(':
#         opens+=1
#     if symbol==')':
#         closes+=1 
#     return opens, closes   

# def is_plus_or_minus(symbol):
#     return symbol in ['+', '-']

# def create_operands_list(input_string):
#     if input_string[0]=='-':
#         operands_list=['-']
#     else: 
#         operands_list[0]='+'    
#     return(operands_list)    


# input_string='-23(x+1)^5+3*x^4+6*x-11'
# parsed_polynomial=[]
# polynomial_operands=create_operands_list(input_string)
# i=0
# while i<len(input_string):
#     monomial=''
#     opens,closes=0,0
#     for symbol in input_string[i: len(input_string)]:
#         i+=1
#         opens, closes=bracket_counter(opens,closes, symbol)
#         if is_plus_or_minus(symbol)==False:
#             monomial+= symbol
#         else:
#             if opens>closes:
#                 monomial+=symbol
#             else:
#                 polynomial_operands.append(symbol)
#                 #i=i-1
#                 break 
#     parsed_polynomial.append(monomial)


# print(parsed_polynomial)
# print(polynomial_operands)


# def monomial_differentiator(monomial):
#     derivative=''
#     if len(monomial)==1:
#         if monomial.isdigit():
#             pass
#         else:
#             derivative='1'
#     else:
#         a=monomial[0:monomial.index('*')]       
#         base=monomial[(monomial.index('*')+1):monomial.index('^')]
#         power=monomial[(monomial.index('^')+2):]
#         #derivative_a=a*power
#     return(a,base,power)    





# def monomial_playground(monomial):
#     for i,symbol in enumerate(monomial):
#         if symbol.isalpha() or symbol=='(':
#             break
#     base_start_index=i

#     # power_symbol_index=monomial.find('^')
#     # base_end_index=power_symbol_index if power_symbol_index!=-1 else len(monomial)           
#     # base=monomial[base_start_index:base_end_index]
#     return base_start_index


# monomial='2*(x+19)^6'  
# k=monomial_playground(monomial)
# print(k)   



# input_string='23(x+1)^5+3*x^4+6*x+11'
# parsed_polynomial=[]
# i=0
# while i<len(input_string):
#     monomial=''
#     opens,closes=0,0
#     for symbol in input_string[i: len(input_string)]:
#         i+=1
#         opens, closes=bracket_counter(opens,closes, symbol)
#         if all ([
#             monomial,
#             is_plus_or_minus(symbol),
#             opens==closes
#             ]): 
#                 i=i-1
#                 break 
#         else:
#             monomial+=symbol   
#     parsed_polynomial.append(monomial)


# print(parsed_polynomial)


# input_list = ['a', '6', 'b', '3', 'c']
# # def alpha_reversal(input_list):
# #     output_list=[]
# #     for i, item in enumerate(input_list):
# #         output_list.append (input_list[-i-1]) if item.isalpha() else output_list.append(item)
# #     return(output_list)

# def beta_reversal(input_list):
#     blist=[item for item in reversed(input_list) if item.isalpha()]
#     clist=[blist.pop(0) if item.isalpha() else item for item in input_list]
#     return(clist)

# alist=beta_reversal(input_list)
# print(alist)    