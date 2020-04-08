# Restate problem: Finding the indices of two numbers in a list who's sum equals the target value
# Clarifying questions: Are the given lists assumed to be sorted?
# Assumptions: Given lists are assumed UNSORTED. Given lists can vary in sizes. There is only one exact pair for each given list.
# Think Outloud: 
# My function must output the answer pair as a list of indices corresponding to the elements in the given list.
# At first I thought of the naive solution which would be to use a nested for loop to check every element in the list,
# and compare one another. But this would not be the best solution due to the runtime resulting in O(n^2).
# The next solution I thought of was how to solve the problem if the given lists were indeed SORTED:

# def twoSum(nums, target):
# '''ASSUMING GIVEN LIST IS SORTED'''
#     answer = []
#     for i in range(len(nums)):
#         if nums[i] + nums[i+1] == target:
#             answer.append(i)
#             answer.append(i+1)
#             return answer

# If the given lists were SORTED, the elements would be stored in increasing order, which would make it easier to compare them by
# checking the sum of the current element, and the following element, to see if it equals the target value.

# After finding the solution for this SORTED case, I decided to find a solution for if the given lists were UNSORTED:

def twoSum(nums, target):
# '''ASSUMING GIVEN LIST IS UNSORTED'''
    # IF the given list is assumed to be UNSORTED, I would want to use a dictionary to reduce the runtime complexity of my solution.
    # The use of a hashtable would allow me to use only one for loop to compare each element to find the sum ==> O(n)
    index_map = {}
    # I decide to use a dictionary in order to keep track of / have direct access to elements I traverse in the list.
    for i in range(len(nums)):
    # loop through each element, i == current index
        num = nums[i]
        # num == element in index i
        pair = target - num
        # pair == number needed in order for num + pair = target to be TRUE
        if pair in index_map:
        # Check if the number needed has been seen previously (Currently stored in dictionary)
            return [index_map[pair], i]
            # If the number has indeed been seen previously, I have found the twoSum, and I return a list holding the indeces of the 
            # two elements
        index_map[num] = i
        # if the pair does not exist in the dictionary, append it to the dictionary.
    return None

if __name__ == "__main__":
    nums = [14, 7, 2, 6]
    print(nums)
    target = 16
    print(twoSum(nums, target))

# By finding the solution to the UNSORTED case, my solution is more efficient because I only require one for loop.
# This makes my solution O(n), which is better than the nested for loop O(n^2) solution I brainstormed at the start.