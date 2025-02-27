# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def rev_list(head):
            prev = None
            curr = head

            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev

        head = rev_list(head)


        max_node = 0
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        temp = head
        
        while temp:
            max_node = max(max_node, temp.val)

            if max_node>temp.val:
                prev.next = temp.next
                temp = temp.next
                continue
            
            temp = temp.next
            prev = prev.next

        temp2 = rev_list(dummy.next)

        return temp2
