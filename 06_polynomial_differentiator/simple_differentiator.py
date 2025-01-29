def polynomial_parser(polynomial):
    addition_parsed_list=polynomial.split('+')
    fully_parsed_list=[]
    for item in addition_parsed_list:
        subtraction_parsed_item=item.split('-')
        for monomial in subtraction_parsed_item:
            fully_parsed_list.append(monomial)
    return(fully_parsed_list)

def polynomial_operands(polynomial):
    operands_list=[symbol for symbol in polynomial if symbol in ['+','-']]
    return(operands_list)

def monomial_differentiator(monomial):
    monomial_derivative=''
    if len(monomial)==1:
        if monomial.isdigit()==True:
            pass
        else:
            monomial_derivative='1'
    else:
        a=monomial[0:monomial.index('*')]       
        base=monomial[(monomial.index('*')+1):monomial.index('^')]
        power=monomial[(monomial.index('^')+2):]
        #derivative_a=a*power
    return(a,base,power)    


def monomial_coefficient_parser(monomial):
    coefficient=''
    for symbol in monomial:
        if symbol.isalpha()==True or symbol=='(':
            break
        else:
            if symbol.isdigit()==True:
                coefficient=coefficient+symbol
            else:
                break
    if coefficient=='':
        coefficient=1
    else:
        coefficient=int(coefficient)            
    return(coefficient)        

def monomial_base_parser(monomial):
    i=0
    for symbol in monomial:
        if symbol.isalpha()==True or symbol=='(':
            break
        else:
            i=i+1
    base_start_index=i
    power_symbol_index=monomial.find('^')
    if power_symbol_index!=-1:
        base_end_index=power_symbol_index
    else:
        base_end_index=len(monomial)           
    base=monomial[base_start_index:base_end_index]
    return(base)

def monomial_power_parser(monomial):
    power_symbol_index=monomial.find('^')
    if power_symbol_index==-1:
        power=1
    else:
        power=int(monomial[power_symbol_index+1:]) 
    return(power)       



s='8(x-4)^5'
c=monomial_coefficient_parser(s)
b=monomial_base_parser(s)
p=monomial_power_parser(s)
print(f'Coefficient is {c}, base is {b}, power is {p}.')


