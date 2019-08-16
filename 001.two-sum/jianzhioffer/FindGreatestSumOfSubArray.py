def FindGreatestSumOfSubArray(array):
    if array == None or len(array)< 0:
        return 0
    cursum = 0
    result = array[0]
    for i in range(len(array)):
        if cursum <= 0:
            cursum = array[i]
        else:
            cursum += array[i]
        print("cu", cursum, "res", result)
        result = max(result, cursum)
    return result

FindGreatestSumOfSubArray([1,-2,3,10,4,7,2,-5])