# import modules
from itertools import combinations
def iters(mylist, k):
    # the formula for combination is: n!/ (n-r)! r! so to achieve this we import combinations
    c = list(combinations(mylist, k))
    # these are the possible combinations
    # [('a', 'a'), ('a', 'c'), ('a', 'd'), ('a', 'c'), ('a', 'd'), ('c', 'd')]
    # print(c)
    # checking if letter 'a' is present in the combinations
    # here 'a' is present in  5 out of 6 possibilities so 5/6 = 0.833
    r = [i for i in c if 'a' in i]
    result = ('{:.3f}'.format(len(r) / len(c)))
    # Printing result and round-off up-to 3 decimal places
    # print('{:.3f}'.format(result))
    print(result)
    # print(type(result))
    return result

