class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        iter_list_node = head
        while iter_list_node and iter_list_node.next is not None:
            while iter_list_node and iter_list_node.next and iter_list_node.val == iter_list_node.next.val:
                iter_list_node.next = iter_list_node.next.next
            iter_list_node = iter_list_node.next
        return head


def go_through_list_node(head: ListNode) -> list:
    result = []
    iter_list_node = head
    while iter_list_node is not None:
        result.append(iter_list_node.val)
        iter_list_node = iter_list_node.next
    return result


if __name__ == '__main__':
    third_node = ListNode(2)
    second_node = ListNode(1, third_node)
    first_node = ListNode(1, second_node)
    result = Solution().deleteDuplicates(first_node)
    assert (go_through_list_node(result) == [1, 2])
    fifth_node = ListNode(3)
    forth_node = ListNode(3, fifth_node)
    third_node = ListNode(2, forth_node)
    second_node = ListNode(1, third_node)
    first_node = ListNode(1, second_node)
    result = Solution().deleteDuplicates(first_node)
    assert (go_through_list_node(result) == [1, 2, 3])
    print('all test cases pass')
