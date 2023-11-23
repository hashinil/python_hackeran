def rotLeft(a, d):
    # Write your code here
    old_shift = a[0:d]
    old_remain = a[d:]

    new = old_remain + old_shift
    return new
