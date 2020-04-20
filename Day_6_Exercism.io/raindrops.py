# The rules of raindrops are that if a given number:

# has 3 as a factor, add 'Pling' to the result.
# has 5 as a factor, add 'Plang' to the result.
# has 7 as a factor, add 'Plong' to the result.
# does not have any of 3, 5, or 7 as a factor, the result should be the digits of the number.

# Examples

# 28 has 7 as a factor, but not 3 or 5, so the result would be "Plong".
# 30 has both 3 and 5 as factors, but not 7, so the result would be "PlingPlang".
# 34 is not factored by 3, 5, or 7, so the result would be "34".

def conversion(num):
    """ Convert given number into a string that contains raindrop sounds, or a string with the given digit."""
    word = ""
    if num % 3 == 0:
        word += "Pling"
    if num % 5 == 0:
        word += "Plang"
    if num % 7 == 0:
        word += "Plong"
    if word == "":
        word = str(num)
    return word

if __name__ == "__main__":
    print(conversion(15))