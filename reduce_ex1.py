"""
@file reduce_ex1.py
@brief Demonstrates 'reduce'
"""
import functools


values = [1.23, -2.74, 8.314, 43.8, -11.78, 4.72]


def get_sum(inp, prev_out):
    return inp + prev_out


class MeanTest():
    """ Calculate mean """
    def __init__(self):
        self.idx = 0
        self.sum = 0.0
        self.mean = 0.0

    def calculate_mean(self, in_val, out_val):
        print("Current index: %d" % self.idx)
        print("Current sum %f" % self.sum)
        self.idx += 1
        self.sum = in_val + out_val
        self.mean = self.sum / self.idx
        print("Mean of values is now: %f" % self.mean)
        #
        return self.sum


def simple_mean(inval, prev):
    pidx, pval, pdummy = prev
    cidx, cval, cdummy = inval
    sum = pval + cval
    idx = cidx + 1
    mean = sum / idx
    print("Current index: %d" % idx)
    print("Current sum: %f" % sum)
    print("Current mean: %f" % mean)
    #
    return idx, sum, mean


if __name__ == "__main__":
    """ 3 ways to skin a cat (recursively ...) """
    sumsum = functools.reduce(get_sum, values, 0.0)
    mean = sumsum / len(values)
    print("Sum = %f" % sumsum)
    print("Mean = %f" % mean)
    print("****************")
    print("")
    # Now something tougher ...
    meany = MeanTest()
    fsum = functools.reduce(meany.calculate_mean, values, 0.0)
    print("Final sum = %f" % fsum)
    print("Final mean = %f" % meany.mean)
    print("")
    # indexed_values:
    indexed_values = []
    for idx, val in enumerate(values):
        indexed_values.append((idx, val, 0.0))
    #
    iter_len, total_sum, mean_val = functools.reduce(simple_mean, indexed_values, (0, 0.0, 0.0))
    print("=========================")
    print("Sequence length: %d" % iter_len)
    print("Final sum = %f" % total_sum)
    print("Final mean = %f" % mean_val)






