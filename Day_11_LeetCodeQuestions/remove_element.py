# Question: removing element from a list.
# This solution would come out to have a runtime complexity of O(n) because there is a while loop being used to traverse the array.
# The space complexity would be O(1) since no extra data structures were created.

def remove_element(lst1, target):
    # new_lst = []
    print("lst1 start:", lst1)
    i = 0
    while i < len(lst1)-1:
        if lst1[i] == target:
            lst1.remove(lst1[i])
            continue
        i += 1
    return lst1

if __name__ == "__main__":
    lst1 = [1, 3, 5, 6, 3, 3, 4]
    target = 3
    print(remove_element(lst1, target))


