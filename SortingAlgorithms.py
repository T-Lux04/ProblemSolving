def bubbleSort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            print(nums)
            if nums[j] > nums[j+1]:
                tempNum = nums[j+1]
                nums[j+1] = nums[j]
                nums[j] = tempNum
    return nums

def SelectionAlgorithm(nums):
    for i in range(len(nums)-1):
        min_index = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_index]:
                tempNum = nums[min_index]
                nums[min_index] = nums[j]
                nums[j] = tempNum
    return nums

def InsertionSort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i -1
        while j>=0 and nums[j]>key:
            nums[j+1] = nums[j]
            j=j-1
        nums[j+1] = key
    return nums

print(InsertionSort(nums = [2,4,3,1,5]))


