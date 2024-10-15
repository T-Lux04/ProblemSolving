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

# print(InsertionSort(nums = [2,4,3,1,5]))

def MergeSort(nums):
    if len(nums) > 1:
        mid = len(nums)//2
        left = nums[0:mid]
        right = nums[mid:len(nums)]

        MergeSort(left)
        MergeSort(right)

        i = j = k = 0

        while i<len(left) and j<len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i+=1
            else:
                nums[k] = right[j]
                j+=1
            k+=1
        
        while i<len(left):
            nums[k] = left[i]
            i+=1
            k+=1
        while j<len(right):
            nums[k] = right[j]
            j+=1
            k+=1
        return nums
        
print(MergeSort(nums = [2,4,3,1,5]))


