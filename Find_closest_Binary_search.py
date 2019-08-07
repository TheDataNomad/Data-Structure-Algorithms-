data = [2,4,8,9,12,14,17,19,22,25,27,28,33,37,39,41,44,45,65,74,123,154,161,612,765,866,543,1212]
target = 34

#find the closest the integer to the target using binary search algorithm 

def Binary_search_iterative_closest(data,target):
    
    # This is to stop the function from reading out of index values  
    if target > data[-1]:
        return data[-1]
    elif target < data[0]:
        return data[0]
    
    #defining the low and high 
    low = 0 
    high = len(data)-1
    
    while low <= high:
        mid = (low+high)//2
        
        #find the difference between target and mid number and the
        #two numbers to either side  
        l_diff = abs(data[mid-1]-target)
        r_diff = abs(data[mid+1]-target)
        m_diff = abs(data[mid]-target)
        
        # the following print codes is for you how the inner working of the functions works
        #print(l_diff,r_diff,m_diff,mid)
        #print(data[mid])
            
        if l_diff < r_diff:  #if the left difference is less it means the closest is on the left side 
                             #because the the difference will grow if you move to the right
            if l_diff < m_diff: #if the left integer difference is less the the middle then we need to move left
                high = mid -1
            else:             #if middle difference is less, it is the closest value
                return print("closest number = ", data[mid])
        else:
            if r_diff < m_diff:
                low = mid + 1
            else:
                return print("closest number = ", data[mid])
