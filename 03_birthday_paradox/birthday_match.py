import random

def group_size():
    n=int(input('Please enter the number of ppl in the group (up to 100 ppl): '))
    return(n)

def bd_month():
    month=random.randint(1,12)
    return(month)

def bd_date_Feb_leap():
    l_dates, l_weights=[],[]
    l_dates=[i for i in range (1,30)]
    l_weights=[4]*28
    l_weights.append(1)
    l_date=random.choices(l_dates,l_weights,k=1)
    date=l_date[0]
    return(date)

def bd_date(month):
    if month in [1,3,5,7,8,10,12]:
        date=random.randint(1,31)
    if month in [4,6,9,11]:
        date=random.randint(1,30)
    else:
        date=bd_date_Feb_leap()
    return(date)
    
group_num_ppl=group_size()
l_group_bds=[]
for person in range(1, group_num_ppl+1):
    p_month=bd_month()
    p_date=bd_date(p_month)
    dm=(p_date,p_month)
    l_group_bds.append(dm)
print(l_group_bds)    
print(f'The list has {len(l_group_bds)} items')
s_group_bds=set(l_group_bds)
print(s_group_bds)
print(f'The set has {len(s_group_bds)} items')



# group_num_ppl=group_size()
# l_group_bds=[]
# for person in range(1, group_num_ppl+1):
#     p_month=bd_month()
#     p_date=bd_date(p_month)
#     dm={p_date:p_month}
#     l_group_bds.append(dm)
# print(l_group_bds)
# if {29:2} in l_group_bds:
#     print(True)
#     i=l_group_bds.index({29:2})
#     print (i)
#     print(l_group_bds[0:i+1])
# else:
#     print(False)    
    














