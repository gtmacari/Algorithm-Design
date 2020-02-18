def ALG(supply, a_rate, b_cost):
	
	#Create variables to keep track of...
    #   -The minimum shipment cost at the current point
	#	-The minimum shipment cost for shipments ending at the given index
	#	-The shipping company schedule for shipments ending at the given index
    current_min = 0
    min_position = []
    company_schedules = []
	
	#For every value in the list of weekly supply shipments...
    for i in range(len(supply)):
	
        #If the current index is the first in the list, there is no option. You 
		#must pick company A. 
		#
		#This is its own case because the company schedules array of arrays has to 
		#be created. For future case, the company schedule of prior indexes is used
		#but that can not be the case for the first index. 
        if i == 0:
            current_min += a_rate*supply[i]
            min_position.append(current_min)
            company_schedules.append(['A'])
			
		#If the current index is less than 4, there is no option. You must pick 
		#company A. 
        elif i < 4:
            current_min += a_rate*supply[i]
            min_position.append(current_min)
            current_schedule = company_schedules[i-1].copy()
            current_schedule.append('A')
            company_schedules.append(current_schedule)
			
		#If the current index is greater than or equal to 4, you much check if 
		#Company A or Company B is optimal. 
		#
		#Company A is optimal to choose if the previous index's optimal shipping 
		#cost plus the rate to ship the current index with Company A is less than 
		#the cost of shipping the four most recent indexes with Company B.
		#Company B is optimal to choose if the cost of shipping the four most recent 
		#indexes with Company B is less than the previous index's optimal shipping 
		#cost plus the rate to ship the current index with Company A. 
		#
		#If Company B is the optimal choice, then the four most recent shipments will 
		#use Company B, and all entries prior to the most recent 4 will revert back 
		#to the company schedule from when the (i-4)th was the last entry. 
        else:
            a_price = min_position[i-1]+(a_rate*supply[i])
            b_price = min_position[i-4]+(b_cost*4)
            if a_price <= b_price:
                current_min += a_rate*supply[i]
                min_position.append(current_min)
                current_schedule = company_schedules[i-1].copy()
                current_schedule.append('A')
                company_schedules.append(current_schedule)
            else:
                current_min = min_position[i-4]+(b_cost*4)
                min_position.append(current_min)
                current_schedule = company_schedules[i-4].copy()
                current_schedule.append('B')
                current_schedule.append('B')
                current_schedule.append('B')
                current_schedule.append('B')
                company_schedules.append(current_schedule)
	
    return company_schedules[len(company_schedules)-1]
