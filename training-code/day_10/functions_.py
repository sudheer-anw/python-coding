def format_name(f_name,l_name):
    if f_name == '' or l_name == '':
        return 'please provide a valid information'
    formated_f_name = f_name.title()
    fromated_l_name = l_name.title()
    return f"result : {formated_f_name}{fromated_l_name}"

print(format_name(input(('what is your firlst name ?')),input('what is your last name?')))






