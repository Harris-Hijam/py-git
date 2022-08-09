#calculation of days to hours
calculation_to_units=24
name_of_units="hours"

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_units}"
   
def validate_and_execute():
    try:
        user_input_number=int(user_input)

        # for conversion only for positive integers
        if user_input_number > 0:
            calculate_values=days_to_units(user_input_number)
            print(calculate_values)
        elif user_input_number == 0:
            print ("A number of hour should be positive number")
        else:
            print("you entered a negative number")
    except ValueError:
        print ("Enter a number istead")

user_input = ""
while user_input != "exit":
    user_input = input("Enter the number of days: ")
    validate_and_execute()
