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
    # TEST CASES
    # Pling 3:
    print("Given 6:", conversion(6)) # Expected output: "Pling"
    print("Given 24:", conversion(24)) # Expected ouput: "Pling"
    # Plang 5:
    print("Given 20:", conversion(20)) # Expected output: "Plang"
    print("Given 100:", conversion(100)) # Expected output: "Plang"
    # Plong 7:
    print("Given 63:", conversion(63)) # Expected output: "Plong"
    print("Given 77:", conversion(77)) # Expected output: "Plong"
    # Combinations:
    print("Given 15:", conversion(15)) # Expected output: "PlingPlang"
    print("Given 70:", conversion(70)) # Expected output: "PlangPlong"
    # Given number:
    print("Given 13:", conversion(13)) # Expected output: "13"
    print("Given 2:", conversion(2)) # Expected output: "2"