def word_order(n,words_list):
    # getting input from user
    # n = int(input().strip())
    counter = {}
    words = []
    for word in words_list:
    #     word = input().strip()
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
            words.append(word)
    print(len(words))
    print(' '.join([str(counter[word]) for word in words]))