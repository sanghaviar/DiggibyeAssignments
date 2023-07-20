import numpy
def elements(my_array):
    # rounds down to the nearest
    floor1 = numpy.floor(my_array)
    # rounds up to the nearest
    ceil1 = numpy.ceil(my_array)
    # rounds to the nearest integer
    rint1 = numpy.rint(my_array)
    print(floor1,ceil1,rint1,sep='\n')
