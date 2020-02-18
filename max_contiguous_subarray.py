def ALG(list):
        
    #BASE CASE
    if len(list) == 1:
        return list
    
    #RECURSIVE CASE
    else:

        #Split the list in half into a left and a right sublist
        split = int(len(list)/2)
        left = list[:split]
        right = list[split:]
        
        #Get the minimum contiguous subarray of each half recursively
        left_max = ALG(left)
        right_max = ALG(right)

        #To check if the maximum contiguous subarray is split by the lists,
        #compute the maximum subarray of the left side starting from the 
        #end and working backwards, and compute the maximum subarray of the 
        #right side starting from the beginning and working forwards. 
        #Adding these two lists together gives the maximum split contiguous 
        #subarray.
        #-->Find max left
        index_left = len(left)-1
        max_sum_left = -1000000
        current_sum = 0
        i = 0
        for i in range(len(left)-1, 0, -1):
            current_sum = current_sum + left[i]
            if current_sum >= max_sum_left:
                index_left = i
                max_sum_left = current_sum
        left_sub = left[i:]
        #-->Find max right
        index_right = 0
        max_sum_right = -1000000
        current_sum = 0
        i = 0
        for i in range(len(right)):
            current_sum = current_sum + right[i]
            if current_sum >= max_sum_right:
                index_right = i
                max_sum_right = current_sum
        right_sub = right[:i]
        
        middle = left_sub + right_sub
        
        #Find the maximum of the three maximum contiguous values.
        left_max = sum(left)
        mid_max = sum(middle)
        right_max = sum(right)
        new_max = max(left_max, mid_max, right_max)
        
        #Return the maximum contiguous subarray
        if new_max == left_max:
            return left
        elif new_max == mid_max:
            return middle
        elif new_max == right_max:
            return right
