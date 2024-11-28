#Rearrange a list such that it alternates between the largest and smallest elements.

def rearrange_alternate(lst):
    lst.sort()
    result = []
    while lst:
        if lst:
            result.append(lst.pop(-1))
        if lst:
            result.append(lst.pop(0))
    return result
