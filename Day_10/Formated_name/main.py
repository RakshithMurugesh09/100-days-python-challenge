def format_name(first_name, last_name):
    if first_name == "" or last_name == "" :
        return "You didn't provide valid inputs."
    else:
        formated_f_name = first_name.strip().title()
        formated_l_name = last_name.strip().title()
        return f"Result {formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name:"), input("What is your last name: ")))