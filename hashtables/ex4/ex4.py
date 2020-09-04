def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []

    value_storage = {}
    # we will classify each number as negative or positive in our value storage
    # dictionary,then we will loop through the array again
    # and this time we will specifically if a number is negative,
    # and if it has both an entry for negative and also a entry for positive
    # then that number has one of both and we will append it to our result array
    # 
    for number in a:

        if number < 0:
            value_storage[number] = "Negative"
        else:
            value_storage[number] = "Positive"
    # print(value_storage)

    for number in a:
        # we will check specifically for negative numbers and if they are in the cache
        # and if that number turned postiive has a key in the dictionary
        # then we have found a number that has negatives and we will append it to our result array
        if number < 0 and number in value_storage and abs(number) in value_storage:
            result.append(abs(number))
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
