# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}

    result = [] 

    for file in files:

        chopped = file.split("/")

        # return chopped[-1] returns last element in chopped list, our query if it exists
        # since there are repeated end values but different whole paths, i can still check the ending now
        # and if i do in, i am referring to my created object/dict which will keep the 0(1) complexity 
        if chopped[-1] in cache:
            cache[chopped[-1]].append(file) # we add that path to this key that will contain 
            # a list of all paths that include its ending path

        else:
            cache[chopped[-1]] = [file] # creates dictionary with last thing as key, and value as the whole pathj


    for query in queries:

        if query in cache:
            result += cache[query]
            # result.append(cache[query]) 


    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
