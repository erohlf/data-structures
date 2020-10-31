
def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""    
    if b < 2 or b > 16:
       return None
    if num // b == 0:
        return str(num)
    elif num % b < 10:
        return str(convert(num // b,b)) + str(num % b)
    elif num % b == 10:
        return str(convert(num // b,b)) + 'A'
    elif num % b == 11:
        return str(convert(num // b,b)) + 'B'
    elif num % b == 12:
        return str(convert(num // b,b)) + 'C'
    elif num % b == 13:
        return str(convert(num // b,b)) + 'D'
    elif num % b == 14:
        return str(convert(num // b,b)) + 'E'
    elif num % b == 15:
        return str(convert(num // b,b)) + 'F'

