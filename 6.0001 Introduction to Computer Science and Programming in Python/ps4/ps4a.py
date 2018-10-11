# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    

    if len(sequence) == 1:
        return [sequence]
    else:
        perm_list = []
        first_char = sequence[0]
        rest_of_chars = sequence[1:]
        
#        Recursively creates the permutation list of the word minus the first character
        subsequent_perm_list = get_permutations(rest_of_chars)
        
#        By the time the program reaches here, the subsequent perm_list will have been created
#        for each instance, the next character is inserted at each index of each permutation forming
#        
        for perm in subsequent_perm_list:
            for i in range(len(perm) + 1):
                new_perm = perm[:i] + first_char + perm[i:]
                perm_list.append(new_perm)
                
        return perm_list
        
        
    




if __name__ == '__main__':
#    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    
#    #EXAMPLE2
    example_input2 = 'ab'
    print('Input:', example_input2)
    print('Expected Output:', ['ab', 'ba'])
    print('Actual Output:', get_permutations(example_input2))
    
#    #EXAMPLE3
    example_input3 = 'a'
    print('Input:', example_input3)
    print('Expected Output:', ['a'])
    print('Actual Output:', get_permutations(example_input3))
    
#    #EXAMPLE3
    example_input4 = 'bust'
    print('Input:', example_input4)
    print('Expected Output:', ['bust', 'ubst', 'usbt', 'ustb', 
                               'bsut', 'sbut', 'subt', 'sutb', 
                               'bstu', 'sbtu', 'stbu', 'stub', 
                               'buts', 'ubts', 'utbs', 'utsb', 
                               'btus', 'tbus', 'tubs', 'tusb', 
                               'btsu', 'tbsu', 'tsbu', 'tsub'])
    print('Actual Output:', get_permutations(example_input4))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    pass #delete this line and replace with your code here

