#finding the fixed point from a sorted array using Binary search method 

# fixed point is when A[i] = i and in this case it's 7 
#index   0    1   2  3  4  5  6  7  8   9
A =    [-10, -5, -2, 1, 3, 4, 5, 7, 9, 10 ]

# if there is no Fixed point it will return None

#iterative way of doing The binary search method 
def Fixed_point_binary_search(data):
    low = 0 
    high = len(data)-1 
    
    while low <= high:
        mid = (low+high) // 2
        print(mid)
        if data[mid] == mid:
            return mid
        elif data[mid] > mid:
            high = mid -1
        else:
            low = mid + 1
    
    return None
    
    
# Recursive way of the binary search: 

def FP_BS_recursive(data,low,high):
    
    if low > high:
        return None
    else:
        mid = (low+high) // 2

        if data[mid] == mid:
            return mid
        elif data[mid] > mid:
            return FP_BS_recursive(data,low,mid -1 )
        else:
            return FP_BS_recursive(data,mid +1,high) 
