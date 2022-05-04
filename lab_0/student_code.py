def order(data):

    for i in range(len(data)):
        
        # set current element
        curr = data[i]
        
        # find previous element
        j = i - 1

        # insertion sort -> swap current element and previous element until we hit beginning
        while j >= 0 and curr < data[j]:
            # swap current element with previous element
            temp = data[j]
            data[j] = curr
            data[i] = temp

            # move indices
            i -= 1
            j -= 1

    return 0

