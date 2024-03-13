class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

val = ListNode([1, 0, 1])

s = ''
while val is not None:
    s = s + str(val.val)
    val = val.next

print(s)