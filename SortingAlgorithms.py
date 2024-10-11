def bubbleSort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            print(nums)
            if nums[j] > nums[j+1]:
                tempNum = nums[j+1]
                nums[j+1] = nums[j]
                nums[j] = tempNum
    return nums
        
print(bubbleSort(nums = [2,4,3,1]))