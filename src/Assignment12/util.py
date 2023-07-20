import numpy
def min_max(my_array):

    # min of axis 1 = [2,3,1,0]
    mini = numpy.min(my_array, axis=1)
    # max = 3
    print(numpy.max(mini))
    return numpy.max(mini)