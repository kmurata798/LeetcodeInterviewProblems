# Given a string containing only lowercase letters, remove all duplicate letters 
# Assuming given list is sorted...

# VARIABLE TABLE:
# Given list = [1, 1, 4, 5, 7, 8]

# head =>  1 => 1 => 4 => 5 => 7 => 8

# current = 8

# Expected output ==> [1, 4, 5, 7, 8]

def deleteDuplicates(head):
    """
    head: ListNode
    current: ListNode
    """
    if head is None:
        return head

    current = head
    while current.next is not None:
        if current.val == curr.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head