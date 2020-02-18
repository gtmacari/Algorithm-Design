def ALG(list1, list2, k):
    
    #BASE CASES 
    
    #If one list is empty, the kth smallest element (where 
    #k starts at 0) must be at index k in the other list.
    if len(list1) == 0:
        return list2[k]
    elif len(list2) == 0:
        return list1[k]
    
    #RECURSIVE CASES
    
    #The list1 is of size m and the list2 is of size n. Divide
    #their lengths by two to get the middle index of each list.
    m_div_2 = int(len(list1)/2)
    n_div_2 = int(len(list2)/2)
    
    #Case 1 - Indexes do not sum up to k
    if m_div_2 + n_div_2 < k:
        #If the larger middle value is in list1, cut list2 in 
        #half, keep the second half, and decrement k to 
        #accomodate the change in list2 size. 
        if list1[m_div_2] > list2[n_div_2]:
            return ALG(list1, list2[n_div_2+1:], k-(n_div_2)-1)
        #Else, the larger middle value is in list2 or the middle 
        #values are equal. Cut list1 in half, keep the second half, 
        #and decrement k to accomodate the change in list1 size.
        else:
            return ALG(list1[m_div_2+1:], list2, k-(m_div_2)-1)
    
    #Case 2 - Indexes sum up to or greater than k
    else:
        #If the larger middle value is in list1, cut list2 in 
        #half, keep the first half, and do not change k. 
        if list1[m_div_2] > list2[n_div_2]:
            return ALG(list1[:m_div_2], list2, k)
        #Else, the larger middle value is in list2 or the middle 
        #values are equal. Cut list2 in half, keep the first half,
        #and do not change k. 
        else:
            return ALG(list1, list2[:n_div_2], k)
