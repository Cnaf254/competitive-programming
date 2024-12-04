class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Use a fast and slow pointer to find the middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the list
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # Compare the two halves
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left, right = left.next, right.next

        return True
