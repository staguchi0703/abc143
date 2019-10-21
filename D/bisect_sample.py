# %%
from bisect import bisect
from bisect import bisect_left
from bisect import bisect_right

# %%
my_list = [0, 1, 2, 3, 3, 3, 4, 5]

#%%
print('bisect(my_list, 3)')
bisect(my_list, 3)

# %%
print('bisect_right(my_list, 3)')
bisect_right(my_list, 3)

#%%
print('bisect_left(my_list, 3)')
bisect_left(my_list, 3)

#%%
from bisect import bisect_left as bil
def index(my_list, val):
    i = bisect_left(my_list, val)
    if my_list[i] == val and len(my_list) != i:
        return bisect_left(my_list, val)
    else:
        raise ValueError

#%%
index(my_list, 3)


#%%
''' bisect source code  '''
def bisect_left(a, x, lo=0, hi=None):
    """ Return the index where to insert item x in list a, assuming a is sorted.
    The return value i is such that all e in a[:i] have e < x, and all e in 
    a[i:] have e >=x. so if x already appears in the list, a.insert(x) will insert just before 
    the leftmost x already there.

    Optional args lo and hi bound the slice of a to be searched.
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo