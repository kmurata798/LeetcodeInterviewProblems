# Given a sorted array and a value, return the indeces in which the target value is located inside the array, or return the indeces of where the value should be stored if
# doesn't exist.

# VARIABLE TABLE:
# lst1 = [1, 3, 6, 8, 9]
# Target = 2

# i = 0 -> 1
# Expected output: 1

def searchInsert(nums, target):
    #Checking if it would be the first index in the list
    if target <= nums[0]:
        return 0
    for i in range(len(nums)-1):
        if target > nums[i] and target <= nums[i+1]:
            return i+1
    #For if the number would be put at the end of the list
    return len(nums)


if __name__ == '__main__':
    lst1 = [1, 3, 6, 8, 9]
    print(searchInsert(lst1, 2))