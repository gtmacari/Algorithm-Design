def ALG(graph):
    
    #Create a temporary array to store running max values
    temp = []
    for i in range(0, len(graph[0])):
        temp.append(0)
    
    #Create variables to keep track of...
    #   -Starting and ending rows of max rectangle
    #   -Starting and ending cols of max rectangle
    #   -Running and total max values
    start_row = 0
    end_row = 0
    start_col = 0
    end_col = 0
    max_here = -1000000
    max_total = -1000000
    
    #Go through every row in the grid and compare the maximum subarray value 
	#of that row with the maximum subarray value of the previous row PLUS the
	#current row. 
	#
	#If the maximum subarray value of the previous row PLUS the current row is
	#greater, then the maximum value to that point is set to it. If this new 
	#maximum for the entire list, only the ENDING row of the grid is changed 
	#to the current row and colums change.
	#
	#Else if the maximum subarray value of the current row is greater, then 
	#the maximum value to that point is set to it. If this is the new maximum 
	#for the entire list, starting and ending row are both changed to the current
	#row and columns change.
	#
	#Basically it's Kadane's Algorithm with extra steps...
    for i in range(0, len(graph)):
        for j in range(0, len(graph[i])):
                temp[j] = temp[j] + graph[i][j]
        kadane_row = KADANE_ALG(graph[i])
        kadane_temp = KADANE_ALG(temp)
        if kadane_temp[0] > kadane_row[0]:
            max_here = kadane_temp[0]
            if max_here > max_total:
                max_total = max_here
                end_row = i
                start_col = kadane_temp[1]
                end_col = kadane_temp[2]
        else:
            temp = graph[i]
            max_here = kadane_row[0] 
            if max_here > max_total:
                max_total = max_here
                start_row = i
                end_row = i
                start_col = kadane_row[1]
                end_col = kadane_row[2]
    
    return ["Sum: "+str(max_total), "Starting Row: "+str(start_row), "Ending Row: "+str(end_row), 
			"Starting Column: "+str(start_col), "Ending Column: "+str(end_col)]
   
#Modified version of Kadane's Algorithm that returns the sum of the maximum 
#subarray, the starting index of the of the maximum subarray, and the ending
#index of the maximum subarray. 
#
#The format of the return value is: [Maximum Sum, Starting Index, Ending Index]
def KADANE_ALG(array):
    max_here = array[0]
    max_total = array[0]
    start_index = 0
    end_index = 0
    for i in range(1,len(array)):
        if max_here+array[i] > array[i]:
            max_here = max_here+array[i]
            if max_here > max_total:
                max_total = max_here
                end_index = i
        else:
            max_here = array[i]
            if max_here > max_total:
                max_total = max_here
                start_index = i
                end_index = i
    return [max_total, start_index, end_index]
