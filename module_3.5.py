def get_multiplied_ditits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_ditits(int(str_number[1:]))
    else:
        return first


result = get_multiplied_ditits(40203)
print(result)
