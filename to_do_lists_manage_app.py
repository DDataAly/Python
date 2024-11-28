# Request the location of the list to be edited/specify a new list
def file_search():
    file_path=input(r'Please enter the file path without the quotes, or type "new" to create a new file: ')
    return(file_path)

# Create a new list if necessary
def create_new_list():
    to_do_list=[]
    file_path=input("Please enter a name: ")+'.txt'
    with open(file_path,'w') as fp:
        for item in to_do_list:
            fp.write(item)
    return(file_path, to_do_list)

# Read the contents of the file and record them to a list
def file_read(file_path):
    to_do_list=[]
    with open(file_path,'r') as fp:
        for line in fp:
            to_do_list.append(line[:-1:])
        return(to_do_list)
    if len(to_do_list)==0:        
        return(to_do_list)

# Check if the user has access rights for the file. 
# If so, check if the existing records should be cleared or kept. 
def password_check(to_do_list, file_path):
    if len(to_do_list)==0:
        return(to_do_list)
    else:
        password='abc'
        user_password=input('Please enter a password: ')
        if user_password==password:
            print(f'The file has following records:{to_do_list}')
            kd=input("Please press K to keep them or D to clear all list ")
            if kd.lower()=='k':
                    return(to_do_list)
            if kd.lower()=='d':
                    with open(file_path,'r') as fp:
                        pass
                    to_do_list=[]
                    return(to_do_list)
        else:
            return('wrong_password')

# Get a request from the user and parse it on action/to_do list item
def request_parsing():
    invalid_input='True'
    while invalid_input=='True':
        try:
            request=input('Please add item to add, remove or type "exit" to finish the program: ')
            if request.strip().lower().startswith('exit'):
                r_command='exit'
                r_body=''
            else:
                r_command, r_body=request.strip().split(" ",1)
                r_body=r_body.strip()
            invalid_input=='False'
            return(r_command,r_body)          
        except ValueError:
            print('The request should have format "command"+"list item".')

# Add an item to the list
def adding_request(r_body, to_do_list):
    to_do_list.append(r_body)
    return(to_do_list)

# Remove an item from the list
def deleting_request(r_body, to_do_list):
    to_do_list=[x for x in to_do_list if x!=r_body]
    return(to_do_list)

# Write the updated list to the file
def file_updating(to_do_list, file_path):
    print(to_do_list)
    with open(file_path,'w') as fp:
        for item in to_do_list:
            fp.write(f'{item}\n')

# Display the updated list to the user   
def file_display(file_path):
    n=1 
    print('\n')   
    with open(file_path,'r') as fp:
        for line in fp:
            print(str(n)+'. ' + line)
            n=n+1

# Get the file path/new list indication from the user. 
# Repeat the action till a valid input is provided. 
valid_path='False'
while valid_path=='False':
    fp=file_search()
    if fp=='new':
        fp,my_list=create_new_list()
        valid_path='True'
    else:
        try:
            my_list=file_read(fp)
            valid_path='True'
        except FileNotFoundError:
            print('File not found. Please check the path') 
print(len(my_list))

# Check if the user has rights to open and amend the file.
# If it's the case, keep asking the user for the items to be added/removed until exit command is entered.
# Display the amended file as a numbered list.
my_list=password_check(my_list,fp)       
if my_list=='wrong_password':
    print("Wrong password. Good buy!")
else:
    print(my_list)
    more_requests='True'
    while more_requests=='True':
        r_com,r_b=request_parsing()
        if r_com=='add':
            my_list=adding_request(r_b,my_list)
            file_updating(my_list,fp)
        elif r_com=='remove':
            my_list=deleting_request (r_b,my_list)
            file_updating(my_list,fp)
        elif r_com=='exit':
            more_requests='False'
            break
        else:
            print("Unknown command. The request should start with 'add','remove' or 'exit'")
    file_display(fp)        


