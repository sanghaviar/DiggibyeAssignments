def no_idea(my_array,a,b):
    h1 = 0 # considering h1 as Hapiness

    for item in my_array:
        if item in a:
            h1 = h1 + 1 # adding 1 as A for happiness
        elif item in b:
            h1= h1- 1   # subtracting 1 as B for sadness
    print(h1)
    return h1