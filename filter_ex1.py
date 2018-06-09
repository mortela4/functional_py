"""
@file filter_ex1.py
@brief Demonstrates 'filter'
"""

values = [1.23, -2.74, 8.314, 0.0, 43.8, -11.78, 4.72]


def is_negative(f_val):
    try:
        val = int(f_val)
        return val < 0
    except ValueError:
        print("%s is NOT a FLOAT!" % f_val)
        return None


def is_positive(f_val):
    try:
        val = int(f_val)
        return val >= 0
    except ValueError:
        print("%s is NOT a FLOAT!" % f_val)
        return None

if __name__ == "__main__":
    positivos = filter(is_positive, values)
    for val in positivos:
        print(val)
    #
    print("=======================")
    #
    negativos = filter(is_negative, values)
    for val in negativos:
        print(val)

