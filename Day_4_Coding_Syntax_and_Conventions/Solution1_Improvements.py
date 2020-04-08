def duplicates(arr):
    duplicates = list()
    for num in arr:
        # Check if current number has been seen before
        if num not in duplicates:
            duplicates.append(num)
        # If number has been seen before, return True
        else:
            return True
    return False

a = [1, 2, 3, 4, 6]
print(duplicates(a)) # OUTPUT == False
b = [1, 2, 3, 4, 6, 6]
print(duplicates(b)) # OUTPUT == True
c = [1,2, 3, 4, 2, 5]
print(duplicates(c)) # OUTPUT == True
d = []
print(duplicates(d)) # OUTPUT == False