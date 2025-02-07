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
    power_index=monomial.rfind('^')
    try:
        exponent= int(monomial[power_index+1:]) if power_index!=-1 else 1
    except ValueError:
            exponent=1
    return exponent       

def first_symbol_analyser(monomial):
    if monomial[0] in ('+','-'):
        monomial_operand=monomial[0] 
        monomial=monomial[1:]
    else:
        monomial_operand='' 
    return(monomial_operand, monomial)   


def monomial_brackets_remover(monomial,monomial_operand):
    open_bracket_index=monomial.find('(')
    closed_bracket_index=monomial.rfind(')')
    monomial=monomial[0:open_bracket_index]+monomial[open_bracket_index+1:closed_bracket_index]
    parsed_monomial=polynomial_parser(monomial)
    print(f'This is the monomial after the brackets remover {parsed_monomial}')
    monomial=''
    if monomial_operand=='-':
        for submonomial in parsed_monomial: 
            if submonomial[0]=='-':
                submonomial='+'+ submonomial[1:]
            elif submonomial[0]=='+':
                submonomial='-'+submonomial[1:]
            else: 
                submonomial='-'+submonomial    
            monomial+=str(submonomial)    
    else:
        for submonomial in parsed_monomial:
            if submonomial[0].isalpha() or submonomial[0].isdigit():
                submonomial='+'+submonomial
            monomial+=str(submonomial)    
    return (monomial)



# s='(x^5+4*x^3-7*x^2-2x+1)'
# m=monomial_brackets_remover(s,'-')
# print(m)



def polynomial_differentiator(input_string):
    polynomial_derivative=''
    parsed_polynomial=polynomial_parser(input_string)
    for monomial in parsed_polynomial:
        print(f'This is monomial {monomial}')
        monomial_derivative=monomial_differentiator(monomial)
        print(f'This is the derivative {monomial_derivative}')
        polynomial_derivative+=monomial_derivative
    if not polynomial_derivative:
        return('') 
       
    if polynomial_derivative[0]=='+':
        formatted_derivative=''.join(symbol for symbol in polynomial_derivative[1:] if symbol.isdigit())
        if len(polynomial_derivative[1:])==len(formatted_derivative):
            polynomial_derivative=formatted_derivative
    return(polynomial_derivative)    

def monomial_differentiator(monomial):
    monomial_operand,monomial=first_symbol_analyser(monomial)
    if monomial.isdigit():
        return('')
    else:
        coefficient=monomial_coefficient_parser(monomial)
        base=monomial_base_parser(monomial)
        exponent=monomial_exponent_parser(monomial)

        print(f'Monomial operand is {monomial_operand}')
        print(f'Coef is {coefficient}')
        print(f'Base is {base}')
        print(f'Exp is {exponent}')

        if exponent==1:
            if monomial.find('(')==-1:
                return(monomial_operand+str(coefficient))
            else:
                polynomial_from_the_brackets=monomial_brackets_remover(monomial,monomial_operand)
                return(polynomial_differentiator(polynomial_from_the_brackets))

        derivative_coefficient=str(coefficient*exponent)
        derivative_exponent=str(exponent-1)

        if exponent==2:
            return(monomial_operand+derivative_coefficient+base)
            
        return(monomial_operand+derivative_coefficient+base+'^'+derivative_exponent)     

# s='(x-7)'
# m=polynomial_differentiator(s)
# print(m)


# s='3*x+8'
# d=polynomial_parser(s)
# print(d)


user_input=input('Please enter a polynomial: ')
derivative=polynomial_differentiator(user_input)
if derivative:
    print(f'The derivative of this polynomial is \n{derivative}')
else:
    print(f'The derivative of this polynomial is 0')



    



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


#Brackets -number of open brackets should match number of closed brackets
# tbc brackets shouldn't be empty
# tbc nested brackets like (((x))) not allowed