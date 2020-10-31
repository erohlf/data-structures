def bears(n):
    n = round(n)
    if n == 42:
        return True
    if n < 42:
        return False
    else:
        if n % 5 == 0:
            if bears(n - 42) == True:
                return True
        if (n % 3 == 0 or n % 4 == 0):
            if n % 10 != 0 and (n // 10) % 10 != 0:
                if bears(n - (n % 10)*((n // 10) % 10)) == True:
                    return True
        if n % 2 == 0:
            if bears(n/2):
                return True
        else:
            return False            
