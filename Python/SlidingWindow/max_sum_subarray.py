def max_sum_array(k, array):
    '''
    Sliding window approach:
    Move the window across the array and check if numbers in the window (window_sum) > max_sum and update max_sum
    
    Time complexity: O(n)
    '''
    max_sum = 0
    window_sum =0
    # loop till the end of the array. As window moves till len(array)-k element. All the array elements are covered
    for i in range(len(array)-k+1):
        window_sum = 0 # As the window moves one step ahead, reset to 0
        # loop to sum the elements in the window
        for j in range(i, i+k):
            window_sum += array[j]
        # compare window sum with the max sum    
        max_sum = max(max_sum, window_sum)
    # get the max sum of all windows    
    return max_sum
    