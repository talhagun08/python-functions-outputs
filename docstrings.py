#Doc strings are using for explain our functions
#Example
def format_name(f_name,l_name):
    """ Take a first and Last name and format it
    to return the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You didn't provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"result: {formated_f_name} {formated_l_name}"
format_name(input("What is your first name?"), input("What is your last name?"))
#Rotate your mouse to "format_name" and you can see the docs.
#As you can see we use this method  """ ... """ and write inside what
# about our function. Biggest difference between string you can use enter while you write lines.

