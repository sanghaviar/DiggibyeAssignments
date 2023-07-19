def merge_the_tools(string, k):
    # Initialized empty list
    temp = []
    # initialized temp variable to 0
    len_temp = 0
    for item in string:
        len_temp += 1
        if item not in temp:
            temp.append(item)
        # Grouping the string
        if len_temp == k:
            res= ''.join(temp)
            print(res)
            temp = []
            len_temp = 0


