
def max_list_iter(int_list):
      # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""
    max = 0
    if int_list == None:
        raise ValueError('list is none')
    elif len(int_list) == 0:
        return None
    else:
        max = int_list[0]
        for i in int_list:
            if i > max:
                max = i
    return max

def reverse_rec(int_list):   # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    if int_list == None:
        raise ValueError("list is none")
    elif len(int_list) == 1 or len(int_list) == 0:
        return int_list
    else:
        return reverse_rec(int_list[1:]) + [int_list[0]]  

def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    if int_list == None:
        raise ValueError("list is none")
    elif len(int_list) == 0:
        return None
    elif target < int_list[low] or target > int_list[high]:
        return None
    elif target != int_list[low] and target != int_list[high]:
        return bin_search(target,low+1,high-1,int_list)
    elif int_list[low] == target:
        return low
    else:
        return high
