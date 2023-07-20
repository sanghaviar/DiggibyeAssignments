import numpy
def determinant_linalg(my_array):

    result = numpy.linalg.det(my_array)
    result1 = ('{:.2f}'.format(result))
    print(result1)
    #print(type(result1))
    return result1