# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        temp1 = temp2 = head

        while temp1 != None:
            temp1 = temp1.next
            if not temp1 or temp1.val != temp2.val:
                temp2.next = temp1
                temp2 = temp2.next

        return head
