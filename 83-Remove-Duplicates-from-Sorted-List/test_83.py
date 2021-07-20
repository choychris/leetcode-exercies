from solution_83 import Solution
from solution_83 import ListNode


class Matcher:
    expected: ListNode

    def __init__(self, expected: ListNode):
        self.expected = expected

    def __eq__(self, other):
        if self.expected.next.next and other.next.next:
            return self.expected.val == other.val and self.expected.next.next.val == other.next.next.val

        return self.expected.val == other.val and self.expected.next.val == other.next.val


def tests():
    input1 = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3, None)))))
    output1 = Solution().deleteDuplicates(input1)
    actual1 = ListNode(1, ListNode(2, ListNode(3, None)))
    assert Matcher(output1) == actual1

    # input1 = ListNode(1, ListNode(1, ListNode(2, None)))
    # output1 = Solution().deleteDuplicates(input1)
    # actual1 = ListNode(1, ListNode(2, None))
    # assert Matcher(output1) == actual1

    # input2 = ListNode(1, ListNode(1, ListNode(2, ListNode(2, ListNode(3, None)))))
    # output2 = Solution().deleteDuplicates(input2)
    # actual2 = ListNode(1, ListNode(2, ListNode(3, None)))
    # assert Matcher(output2) == actual2
