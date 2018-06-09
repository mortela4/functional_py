"""
@file map_ex1.py
@brief Demonstrates 'map'
"""

values = [1.23, -2.74, 8.314, 43.8, -11.78, 4.72]


def to_int(f_val):
    try:
        return int(f_val)
    except ValueError:
        print("Cannot convert %s to INT!" % f_val)
        return None


def to_float(i_val):
    try:
        return float(i_val)
    except ValueError:
        print("Cannot convert %s to FLOAT!" % i_val)
        return None


if __name__ == "__main__":
    ints = map(to_int, values)
    # 'ints' is a 'map'-object, but we can still iterate over its (iterable) values:
    for ival in ints:
        print(ival)
    # 'ints' is (in FOR-loop context) just an iterator -
    # cannot reuse it after 1st use (or, have to reset it ...)!
    # Need to convert 'map'-object to 'list' before using 'map()' again:
    ilist = list(map(to_int, values))
    print(ilist)
    floats = map(to_float, ilist)
    for fval in floats:
        print(fval)




