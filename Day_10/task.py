'''def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    
    return f"{formated_f_name} {formated_l_name}"
    
formated_string = format_name(f_name= "angela", l_name="yu")
print(formated_string)

def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_2(function_1("Tests"))

print(output)'''


def format_name(f_name, l_name):
    '''Take a first and last name and format it to return a title case'''
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"result: {formated_f_name} {formated_l_name}"

print(format_name(input("Whats is your first name?"), input("What is your lastname? "))) 


def is_leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print(f"The year {year} is a Leap year")
        return True
    else:
        print(f"The year {year} is not a Leap year")
        return False
        
    
is_leap_year(2001)