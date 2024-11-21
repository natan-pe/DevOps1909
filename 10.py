

def check_in_interval(what_to_ask, min_value, max_value,):
    current_value = int(input(what_to_ask))
    if min_value < current_value < max_value:
        return True
    return False

result = check_in_interval("enter your age: ",
                           0,
                           80)
if result:
    print("Your age")
else:
    print("Not good")

