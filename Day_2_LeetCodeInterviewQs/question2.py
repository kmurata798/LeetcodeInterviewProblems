# Restate Problem: Write a function to determine whether a given integer can be read the same forwards and backwards.
# Clarifying Questions: Are single digits counted as palindromes? Are negative numbers counted as palindromes?
# Assumptions: Single digits are counted as palindromes. Negative numbers do not count as palindromes because of the minus sign.
#               Output is a boolean.
# Think Outloud:
# The way to solve this problem is to compare the first half of the given number with the second half.
# In order to do this, I need to convert the given number into a string so that I can traverse through each element as an array.
# I start off the function by first validating the edge cases: if the number is a negative or if the number ends in a zero.
def isPalindrome(num):
    if num < 0 or (num != 0 and num % 10 == 0):
    # Check if given number is either negative, or whether the final digit includes a 0.
    # Because these characteristics implies that the number is not a palindrome.
        return False
    str_num = str(num)
    # Convert num to string so that we can traverse each element in the string.
    i = 0
    while i < len(str_num) / 2:
    # loop over the length of half the array since we only need compare the first half with the ending half.
        if str_num[i] != str_num[-i-1]:
        # Check if the current number is equal to the number equidistant from the last index in the array.
        # The negative sign in front of i in num[-i-1] tells the computer to count the array starting from the ending. 
        # (read in reverse order)
            return False
            # If the current number does NOT equal the expected pair, the number is not a palindrome. Return FALSE
        i += 1
        # increment i so that we can loop to the next item in the array
    return True

if __name__ == "__main__":
    '''returns True'''
    # failing_num = 123421
    # print(isPalindrome(failing_num))

    '''returns False'''
    # passing_num = 1
    passing_num = 123321
    print(isPalindrome(passing_num))

# This solution seems to be acceptable since the runtime complexity is O(n) since there is only one while loop inside the function.