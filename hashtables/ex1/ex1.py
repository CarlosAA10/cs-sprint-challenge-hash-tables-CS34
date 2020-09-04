def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    weights_dic = {}

    if length == 1:
        return None
    
    for i in range(len(weights)):
        if weights[i] not in weights_dic:
            # adding weight to our dictionary
            # then we will do another loop checking if the weight minus the limit is equal to an entry
            # with that weight in our dic, if there is we have found a pair, if not we continue till we loop and 
            # find out it's not there
            # the value for each key is the index
            weights_dic[str(weights[i])] = i
    print(weights_dic)
        
    # dictionary made now we will loop again and compare values if they equal the limit
    
    for j in range(length):
        # print('hi')
        # this handles the special case if 
        if length == 2 and j == 0 and str(weights[j + 1]) in weights_dic:
            pair = (j + 1, j)
            # break
        elif length == 2 and j == 1:
            pass

        elif str(limit - weights[j]) in weights_dic:
            # print('found')
            # return f"Found it"
            if j > weights_dic[str(limit - weights[j])]:
                pair = (j, weights_dic[str(limit - weights[j])])
            else:
                pair = (weights_dic[str(limit - weights[j])], j)
            

    if pair:    
        return pair
    else:
        return None

weights_2 = [4,4]
answer_2 = get_indices_of_item_weights(weights_2, 2, 8)

print(answer_2)

weights_3 = [4, 6, 10, 15, 16]
answer_3 = get_indices_of_item_weights(weights_3, 5, 21)

print(answer_3)

weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
answer_4 = get_indices_of_item_weights(weights_4, 9, 7)

print(answer_4)