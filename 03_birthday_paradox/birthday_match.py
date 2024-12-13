import random
# Credentials
def intro():
    print('''\nBirthday Paradox Simulation, from Al Sweigart's Big Book of Small Projects. The birthday paradox
shows us that in a group of N people, the odds that two of them have matching birthdays is surprisingly large. 
This program does a Monte Carlo simulation to explore this concept. Code is written by me.''')
    
# Ask user to input the parameters of the probability calculation
def experiment_parameters():
    n_experiments=int(input('\nPlease enter the number of experiments: '))
    valid_input=False
    while valid_input==False:
        n_ppl=int(input('Please enter the number of ppl in the group (up to 100 ppl): '))
        if n_ppl>0 and n_ppl<100:
            valid_input=True
        else:
            print('Please enter a valid size of the group. ')    
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

# Display birthdays in text format, separating them with commas
def birthday_display(n_ppl):
    group_birthdays=[]
    months=('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
    for person in range(1, n_ppl+1):
        p_month=bd_month()
        p_date=bd_date(p_month)     
        for index,month in enumerate(months):
            if p_month==index+1:
                dm=(str(p_date)+' '+month)
        group_birthdays.append(dm)
    for index,birthday in enumerate(group_birthdays):
        if index!=0:
            print(', '+birthday, end =' ')
        else:
            print(birthday, end =' ')
    return(group_birthdays)


# Check if there is at least one duplicating birthday in the group of given size 
def duplicates_checker(group_birthdays):    
    unique_group_birthdays=set(group_birthdays)
    duplicates=set([birthday for birthday in unique_group_birthdays if group_birthdays.count(birthday)>1])
    if len(unique_group_birthdays)!=len(group_birthdays):
        print(f'\nIn this simulation, multiple people have birthdays on: ')
        for birthday in duplicates:
            print(birthday, ' ')
        return(True)
    else:
        print(f'\nIn this simulation, there are no matching birthdays in the group. ')
        return(False)


# Calculating probability of two or more people in the group having birthday at the same day
intro()
num_experiments, group_size = experiment_parameters()
total_experiments=num_experiments
match=0
notification_counter=1
print('Ready to start simulations.')
input('Press enter to begin...')
while num_experiments>0:
    print('\nRunning the experiment...')
    group_birthdays=birthday_display(group_size)
    m=duplicates_checker(group_birthdays)
    if m==True:
        match+=1
    num_experiments-=1 
    if (total_experiments - num_experiments)%1_00==0 and (total_experiments!=(total_experiments-num_experiments)):
        print(f'We run {notification_counter*100} experiments. Work in progress...')
        notification_counter+=1

print(f'''\nWe run {total_experiments} simulations for a group of {group_size} people.
There were {match} cases where at least two people in the group had a birthday at the same day.      
The probability of at least two people having birthday at the same day in this group is {(match/total_experiments):.2%}''')    









