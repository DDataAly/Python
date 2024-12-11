import random

# Ask user to input the parameters of the probability calculation
def experiment_parameters():
    n_experiments=int(input('Please enter the number of experiments: '))
    n_ppl=int(input('Please enter the number of ppl in the group (up to 100 ppl): '))
    return(n_experiments,n_ppl)

# Generate random month of birth
def bd_month():
    month=random.randint(1,12)
    return(month)

# Generate random date of birth for those who were born in Feb (leap year consideration)
def bd_date_feb_leap():
    l_dates, l_weights=[],[]
    l_dates=[i for i in range (1,30)]
    l_weights=[4]*28
    l_weights.append(1)
    l_date=random.choices(l_dates,l_weights,k=1)
    date=l_date[0]
    return(date)

# Generate random date of birth based on the number of days in a particular month 
def bd_date(month):
    if month in [1,3,5,7,8,10,12]:
        date=random.randint(1,31)
    if month in [4,6,9,11]:
        date=random.randint(1,30)
    else:
        date=bd_date_feb_leap()
    return(date)
    
# Check if there is at least one duplicating birthday in the group of given size 
def duplicates_checker(n_ppl):    
    group_birthdays=[]
    for person in range(1, n_ppl+1):
        p_month=bd_month()
        p_date=bd_date(p_month)
        dm=(p_date,p_month)
        group_birthdays.append(dm)
    unique_group_birthdays=set(group_birthdays)
    if len(unique_group_birthdays)!=len(group_birthdays):
        return(True)
    else:
        return(False)

# Calculating probability of two or more people in the group having birthday at the same day
num_experiments, group_size = experiment_parameters()
total_experiments=num_experiments
match=0
while num_experiments>0:
    m=duplicates_checker(group_size)
    if m==True:
        match+=1
    num_experiments-=1    
print(f'''We run {total_experiments} for a group of {group_size}.
The probability of at least two people having birthday at the same day in this group is {match/total_experiments}''')    

 
    














