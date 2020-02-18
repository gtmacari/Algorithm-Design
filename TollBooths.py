#booths = a list of touples holding the mile marker and profit of each booth 
#	ie. booths[i] = [miles, profit]
#c = cost of contructing one toll booth
#k = minimum distance between toll booths
def ALG(booths, c, k):
    
    #Create variables to keep track of...
    #   -The mile marker of the last toll booth
    #    -The current revenue of the current toll booths built
    #    -The revenues of each solution of toll booth arrangements to a certain point 
    #    -The solutions of toll booth touples for each toll booth arrangement
    last_booth_mi = -1
    current_revenue = 0
    revenues = [0]
    solutions = [[[0, 0]]]
    
    #Check every booth in the list of potential booths
    #
    #If the current booth is profitable and it is at least k miles past the last booth, 
    #then you can add the booth to the previous list of used booths and update the revenue 
	#to that point
	#
	#Otherwise, if the booth is profitable and it is less than k miles past the last booth, 
	#then you have to go back in the list of constructed booths to find the most recent 
	#optimal solution where the nearest booth is greater than or equal to k miles away. If
	#adding the revenue from the current booth to the revenue of the nearest valid optimal 
	#solution is greater than the previous optimal solution, then add the revenue of the 
	#current booth to the revenue of the nearest valid optimal solution, add the touple for 
	#the current booth to the solution of the nearest valid optimal solution, and update 
	#the revenues and solutions arrays with the new values. If it is not greater, then 
	#ignore the current booth and move on. 
	#
	#Any booths that are not profitable (cost of construction exceeds booth profit) are 
	#ignored.
    for i in range(len(booths)):
    
        #Extract the mile marker (m) and the profit (p) of the toll booth from the touple
        m = booths[i][0]
        p = booths[i][1]
        
        #Only consider adding a toll booth if the profit exceeds the cost of building it
        if p-c > 0:
            
            #Special case for the first added value
            if len(solutions) == 1:
                last_booth_mi = m
                current_revenue = p-c
                revenues.append(current_revenue)
                solution = []
                solution.append(booths[i].copy())
                solutions.append(solution)
            
            #Everything else
            else:
                if last_booth_mi+k <= m:
                    last_booth_mi = m
                    current_revenue = revenues[-1]+(p-c)
                    revenues.append(current_revenue)
                    if solutions[-1] == [[0,0]]:
                        solution = []
                    else:
                        solution = solutions[-1].copy()
                        solution.append(booths[i].copy())
                        solutions.append(solution)
                else:
                    index = 0
                    for j in range(-1, (len(solutions)+1)*-1, -1):
                        if (solutions[j][-1][0])+k <= m:
                            index = j
                            break
                    if revenues[-1] < revenues[index]+(p-c):
                        last_booth_mi = m
                        current_revenue = revenues[index]+(p-c)
                        revenues.append(current_revenue)
                        if solutions[index] == [[0,0]]:
                            solution = []
                        else:
                            solution = solutions[index].copy()
                            solution.append(booths[i].copy())
                            solutions.append(solution)
 
    return(["Revenue: $"+str(revenues[-1]), "Booths: "+str(solutions[-1])])
