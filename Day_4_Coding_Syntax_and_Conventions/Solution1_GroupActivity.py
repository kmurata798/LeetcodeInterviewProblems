def duplicates(arr):
    duplicates = list()
    for num in arr:
        if num not in duplicates:
            duplicates.append(num)
        else:
            return True
    return False

a = [1, 2, 3, 4, 6]
b = [1, 2, 3, 4, 6, 6]
print(duplicates(b))
c = []