def perm_gen_lex(a): 
    '''makes all string permutatations and returns in lexographic order'''
    perms_list = []
    if len(a) == 1:
        return [a]
    else:
        for i in range(len(a)):
            new_str = a[0:i] + a[i+1:]
            perms = perm_gen_lex(new_str)
            for j in perms:
                perms_list.append(a[i] + j)
    return perms_list
 
