# Tracy Sun, CSW 8 (F21)

'''
SO I HAVE TO DO THIS SHIT AS WELL apparently:
You must correctly and appropriately comment your code
to clearly explain your solution.

Every function should include an appropriate,
informative docstring that is included
immediately underneath the function signature.
You will be graded on the presence and quality of your documentation.
Include more extensive comments for the parts that you found harder to code.
There shouldn't be any pass or TODO or FIXME comments left in your code.
'''
def print_main_menu(user_menu):
    print('*' * 26)
    print('What would you like to do?')
    for key, value in user_menu.items(): 
        print('{} - {}'.format(key,value)) 
    print('*' * 26)
    '''
    this function iterates through the dictionary,
    printing every key and value into the format
    '''

def check_option(option,menu):
    if (type(option) == int) or (option.isdigit() == True):
        if option in menu:
            return 'valid'
        else:
            print('WARNING: `{}` is an invalid option.'.format(option))
            print('Please enter a valid option.') 
            return 'invalid'
    else:
        print('WARNING: `{}` is not an integer.'.format(option))
        print('Please enter an integer.') 
        return 'invalid'
    '''
    check if the option is an integer using isdigit()
    if so, see if it is in menu
    (they should both be strings so this should work)
    numbers that are not in menu and non-number inputs
    will have corresponding error messages
    and the main program will reprompt the user to enter a valid input
    '''

#option 1
def list_categories(user_dict, showID = False):
    if user_dict == {}:
        print('There are no categories.')
    elif len(user_dict) == 1:
        print('There is only 1 category:')
        if showID == False:
            for key, values in user_dict.items():
                print('{} : {}%'.format(values[0].upper(), values[1]))
        else:
            for key, values in user_dict.items():
                print(f'{key} - {values[0].upper()} : {values[1]}%')
    else:
        print('There are',len(user_dict),'categories:')
        if showID == False:
            for key, values in user_dict.items():
                print('{} : {}%'.format(values[0].upper(), values[1]))
        else:
            for key, values in user_dict.items():
                print(f'{key} - {values[0].upper()} : {values[1]}%')
    return len(user_dict)
    '''
    different cases depending on number of categories, but same process
    showID shows the key of the dictionary
    '''

#option 2
def is_numeric(val):
    if val.count('.') == 1:
        new_val = val.replace('.','') #remove period, see if actually float
        if new_val.isdigit() == True:
            return True
        else:
            return False
    elif val.isdigit() == True:
        return True
    '''
    FINDING FLOAT:
    take out a period, find if the rest of it are digits
    count to see if there's only 1 period
    remove period, see if actually float
    '''

def create_id(storage_dict, offset=0):
    if storage_dict == {}:
        return offset
    else:
        keys_list = []
        for index in storage_dict.keys():
            num_index = int(index)
            keys_list.append(num_index)
        return (1 + max(keys_list))
    '''
    modified my add_element function from lab 10.12
    it should now return the proper id number for some value,
    with offset and deletion of keys factored in
    '''

def add_category(db, cid, info_str):
    info_str = info_str.split()
    if len(info_str) != 2:
        return -2
    else:
        percentage = info_str[1]
        if is_numeric(percentage) == True:
            db[cid] = [info_str[0],float(percentage)]
            return cid
        else:
            return -1
    '''
    adds cid from create_id() function with info_str to dictionary db
    if percentage in info_str is not int or float, returns -1
    (causing add_categories() to do something different)
    otherwise returns the id of category
    '''
    
def add_categories(db, max_num, id_offset):
    print("You can add up to",max_num,"categories.") 
    print("::: How many categories will you add?")
    num_categories = input('> ')
    while True: #repeats this process until user input is correct format
        if num_categories.isdigit() == True:
            num_categories = int(num_categories)
            if (num_categories > max_num) or (num_categories + (len(db)) > max_num):
                print(f'WARNING: Adding {num_categories} categories would exceed the allowable max.')
                print(f'You can store up to {max_num} categories.')
                print(f'Current total of categories is {len(db)}.')
                break
            else:
                for num in range(num_categories):
                    print(f'::: Enter the category {num+1} name (no spaces) followed by its percentage')
                    info_str = input('> ')
                    info_list = info_str.split()
                    cid = str(create_id(db, id_offset))
                    if add_category(db, cid, info_str) == -1:
                        print('WARNING: invalid input for the name and percentage.')
                        print(f'::: Enter the category {num+1} name (no spaces) followed by its percentage')
                        print('::: or enter M to return back to the menu.')
                        user_choice = input('> ')
                        if (user_choice == 'M') or (user_choice == 'm'):
                            return None
                        else:
                            add_category(db, cid, user_choice)
                            continue
                    elif (len(info_list) != 2) or (is_numeric(info_list[1]) != True):
                        print('WARNING: invalid input for the name and percentage.')
                        print(f'::: Enter the category {num+1} name (no spaces) followed by its percentage')
                        print('::: or enter M to return back to the menu.')
                        user_choice = input('> ')
                        if (user_choice == 'M') or (user_choice == 'm'):
                            return None
                        else:
                            add_category(db, cid, user_choice)
                            continue
                    else:
                        add_category(db, cid, info_str)
                        continue
                    continue
                break
        else:
            print(f'`{num_categories}` is not a valid integer.')
            print('::: Enter a valid number of categories you plan to add')
            new_num = input('> ')
            num_categories = new_num
            continue
                    
    '''
    interactive part of option 2:
    adds as many categories to db as user wishes using add_category()
    keys are the cid from create_id() function
    it took me a long time to figure out how to make the function go back
    i finally just used a while true loop for the input part
    and had correct inputs break out of it
    while incorrect inputs would continue
    '''

#OPTION 3
def update_category(db):
    print('Below is the info for the current categories.')
    list_categories(db, showID = True)
    if len(db) == 0:
        return None
    else:
        print('::: Enter the category ID that you want to update')
        user_id = input('> ')
        key_list = []
        for key in db.keys():
            key_list.append(key)
        while True:
            if user_id in key_list:
                print(f'Found a category with ID `{user_id}`:')
                print('::: Enter the updated info:')
                print('    category name followed by the percentage.')
                new_info = input('> ')
                info_str = new_info.split()
                if len(info_str) != 2:
                    print('WARNING: insufficient information for the update.')
                    print(f'Record with ID `{user_id}` was not updated!')
                    break
                else:
                    percentage = info_str[1]
                    if is_numeric(percentage) == True:
                        db[user_id] = [info_str[0],float(percentage)]
                        break
                    else:
                        print('WARNING: invalid input for the name and/or percentage.')
                        print(f'Record with ID `{user_id}` was not updated!')
                        return None
            else:
                print(f'WARNING: `{user_id}` is not an ID of an existing category.')
                print('::: Enter the category ID that you want to update')
                print('::: or enter M to return back to the menu.')
                user_choice = input('> ')
                if (user_choice == 'M') or (user_choice == 'm'):
                    return None
                elif user_choice.isdigit() == True:
                    user_id = user_choice
                    continue
    '''
    this function updates categories woo
    with right error messages
    calls on previous function to do the actual adding
    '''

#*sigh* OPTION FOUR NOW GOING STRONG AT 12 AM!
def delete_category(db):    
    print('Below is the info for the current categories.')
    len_db = list_categories(db, showID = True)
    loop_var = 1
    if len(db) == 0:
        return None    
    else:
        print('::: Enter the category ID that you want to delete')
        user_id = input('> ')
        key_list = []
        for key in db.keys():
            key_list.append(key)
        if int(user_id) in key_list:
            print(f'Found a category with ID `{user_id}`:')
            print(db[user_id])
            print('::: Are you sure? Type Y or N')
            user_choice = input('> ')
            if user_choice == 'Y':
                print('Deleted')
                del db[user_id]
            else:
                print("Looks like you aren't 100% sure.")
                print('Cancelling the deletion.')
                return None
        else:
            print(f'WARNING: `{user_id}` is not an ID of an existing category.')
            print('::: Enter the ID of the category you want to delete')
            print('::: or enter M to return back to the menu.')
            user_choice = input('> ')
            if (user_choice == 'M') or (user_choice == 'm'):
                return None
            elif user_choice in key_list:
                print('Deleted')
                del db[user_choice]
            else:
                print('lol that wasnt a given option but ok menu it is')
                return None
    '''
    deletes categories from the dictionary
    prompts user an additional time to be sure
    error messages if given ID does not exist 
    '''

#option 6
def show_grades(db):
    print('Below is the info for the current categories.')
    list_categories(db, showID = True)
    if len(db) == 0:
        return None
    else:
        print('::: Enter the category ID for which you want to see the grades')
        print('::: or enter A to list all of them.')
        user_id = input('> ')
        while True:
            if user_id in db:
                show_grades_category(db, user_id)
                return None
            elif user_id == 'A':
                for key in db:
                    if show_grades_category(db, key) == 0:
                        print(f'No grades were provided for category ID `{key}`.')
                        continue
                    else:
                        continue
                return None
            else:
                print(f'WARNING: `{user_id}` is not an ID of an existing category.')
                print('::: Enter a valid category ID to see the grades')
                print('::: or enter M to return back to the menu.')
                user_choice = input('> ')
                if (user_choice == 'M') or (user_choice == 'm'):
                    break
                elif user_choice in db:
                    user_id = user_choice
                continue
    '''
    uses show_grades_category() function to display grades
    (the list that is the third entry of matching value of key in dictionary)
    'A' displays grades for all categories at once,
    unless one doesn't have any grades yet
        that took me a bit to get right, it kept printing twice bc i mentioned
        show_grades_category() twice
    '''

def show_grades_category(db, cid):
    if (len(db[cid]) <= 2) or (db[cid][2] == []):
        return 0
    else:
        grades_list = db[cid][2]
        print(f'{db[cid][0].upper()} grades',grades_list)
        return len(grades_list)
    '''
    function that show_grades() relies on
    prints category name followed by grades
    if no grades are there, exits function
    '''

#option 5
def add_grades(db):
    print('Below is the info for the current categories.')
    list_categories(db, showID = True)
    if len(db) == 0:
        return None
    else:
        print('::: Enter the category ID for which you want to add grades')
        user_id = input('> ')
        key_list = []
        for key in db.keys():
            key_list.append(key)
        while True:
            if user_id in key_list:
                print(f'You selected a {db[user_id][0].upper()} category.')
                print('::: Enter space-separated grades')
                print('::: or enter M to return back to the menu.')
                user_grades = input('> ')
                if (user_grades == 'M') or (user_grades == 'm'):
                    break
                else:
                    if len(db[user_id]) <= 2:
                        print(f'Success! Grades for the {db[user_id][0].upper()} category were added.')
                    else:
                        print(f'Success! Grades for the {db[user_id][0].upper()} category were updated.')
                    add_category_grades(db, user_id, user_grades)
                    break
            else:
                print(f'`{user_id}` is not an ID of an existing category.')
                print('::: Enter the ID of the category to add grades to')
                print('::: or enter M to return back to the menu.')
                user_choice = input('> ')
                if (user_choice == 'M') or (user_choice == 'm'):
                    return None
                elif user_choice.isdigit() == True:
                    user_id = user_choice
                continue
    """
    adds grades to a category
    or updates them if there are already grades in that category
        uses function from option 6 to show grades if they do exist
    error message if given ID does not exist
    """

def add_category_grades(db, cid, grades_str):
    grades_list = grades_str.split()
    for(index, grade) in enumerate(grades_list):
        if is_numeric(grade) == False:
            return -1
        else:
            grades_list[index] = float(grade)
    if len(db[cid]) > 2:
        show_grades_category(db, cid)
        for grade in grades_list:
            db[cid][2].append(grade)
        show_grades_category(db, cid)
        return len(grades_list)
    else:
        db[cid].append(grades_list)
        return len(grades_list)
    '''
    actually does the adding
    checks if each number given is a number or not
    then converts them to float type and adds them to a list
    which is then added to the dictionary
    if there are already grades, shows the grades before and after adding
    using show_grades_category()
    otherwise just adds grades
    '''

#option 7

#option 8
import csv
def save_data(db):
    print('Below is the info for the current categories.')
    list_categories(db, showID = True)
    if len(db) == 0:
        print('Skipping the creation of an empty file.')
        return None
    else:
        print('::: Save to the default file (grade_data.csv)? Type Y or N')
        user_choice = input('> ')
        if user_choice == 'Y':
            save_dict_to_csv(db, 'grade_data.csv')
            print('Saving the database in grade_data.csv')
            print('Database contents:')
            print(db)
        else:
            print('::: Enter a file name to save to.')
            filename = input('> ')
            save_dict_to_csv(db, filename)
            print(f'Saving the database in {filename}')
            print('Database contents:')
            print(db)
    '''
    saves user's dictionary to csv file
    under either default or user given name
    
    '''

def save_dict_to_csv(db, filename):
    fileline = ''
    with open(filename, 'w', newline = '') as file:
        for key, value in db.items():
            fileline = f'{key},{value[0]},{value[1]},'
            if len(value) > 2:
                index_list = []
                for index in range(len(value[2])):
                    index_list.append(index)
                for index,num in enumerate(value[2]):
                    if index == max(index_list): #splitting the rows (this took me forever)
                        fileline += f'{str(num)}\n'
                    else:
                        fileline += f'{str(num)},'
                file.writelines(fileline)
            else:
                file.writelines(fileline)
                file.writelines('\n')
    return file
    '''
    saves dictionary to a csv file
    splits each key-value pair into individual row
    '''

#option 9
def load_data(db):
    import csv
    import os
    filename = 'grade_data.csv'
    print(f"::: Load the default file ({filename})? Type Y or N")
    user_choice = input('> ')
    if user_choice == 'Y':
        print(f"Reading the database from {filename}")
        new_db = load_dict_from_csv(filename)
        print("Resulting database:\n", new_db)
        db.update(new_db)
    elif user_choice == 'N':
        print('::: Enter the name of the csv file to load.')
        user_file = input('> ')
        while True:
            if '.csv' != user_file[-4:]:
                print(f'WARNING: {user_file} does not end with `.csv`')
                print('::: Enter the name of an existing csv file.')
                user_file = input('> ')
                continue
            elif not os.path.isfile(user_file):
                print(f"WARNING: Cannot find a CSV file named '{user_file}'")
                print('::: Enter the name of an existing csv file.')
                user_file = input('> ')
                continue
            else:
                print(f"Reading the database from {user_file}")
                new_db = load_dict_from_csv(user_file)
                print("Resulting database:\n", new_db)
                db.update(new_db)
            break
    '''
    interacts with user to transfer content from csv file to dictionary in program
    error messages if file is not .csv or file doesn't exist
    transfers empty dict if csv file is empty
    '''

def load_dict_from_csv(filename):
    new_dict = {}
    with open(filename, 'r') as file:
        read_file = csv.reader(file)
        if read_file == []:
            return {}
        else:
            for row in read_file:
                if len(row) <= 3:
                    new_dict[int(row[0])] = [row[1], float(row[2])]
                else:
                    grades_list = row[3:]
                    for index, grade in enumerate(grades_list):
                        if grade == '':
                            grades_list.remove(grade)
                        else:
                            grades_list[index] = float(grade)
                    new_dict[int(row[0])] = [row[1], float(row[2]), grades_list]
    return new_dict
    '''
    transfers csv file data to dictionary in program
    different options based on if there is a grades list or not
    '''

if __name__ == '__main__':
    the_menu = {'1':'List categories',
                '2':'Add a category',
                '3':'Update a category',
                '4':'Delete a category',
                '5':'Add grades',
                '6':'Show grades',
                '7':'Grade statistics',
                '8':'Save the data',
                '9':'Upload data from file',
                'Q':'Quit this program'}

    main_db = {} # stores the grading categories and info
    #main_db = {'100': ['coding <3','percentage1',['gradesfiller1']],'101': ['nerd hours','percentage2',['gradesfiller2']]}
    max_cat = 10 # the max total num of categories a user can provide
    cat_id_offset = 100 # the starting value for the category ID

    opt = None

    while True:
        print_main_menu(the_menu) # DONE: uncomment and call with the menu as an argument
        print("::: Enter an option")
        opt = input("> ")
        if (opt == 'Q') or (opt == 'q'): # DONE: make Q or q quit the program
            print("Goodbye")
            break
        else:
            if check_option(opt, the_menu) == "invalid": # DONE: implement check_option
                continue
            print("You selected option {} to > {}.".format(opt, the_menu[opt]))

        if opt == '1':
            list_categories(main_db)
        elif opt == '2':
            add_categories(main_db, max_cat, cat_id_offset)
        elif opt == '3':
            update_category(main_db)
        elif opt == '4':
            delete_category(main_db)
        elif opt == '5':
            add_grades(main_db)
        elif opt == '6':
            show_grades(main_db)
        elif opt == '7':
            print('maybe i\'ll get to the extra credit if i have time??')
            print('(if you\'re seeing this message, i evidently did not)')
        elif opt == '8':
            save_data(main_db)
        elif opt == '9':
            load_data(main_db)
        else:
            print('please enter a valid option from menu <3')

        opt = input("::: Press Enter to continue...")

    print("See you next time!")
