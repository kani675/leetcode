class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
        
        # Step 1: find length and tail
        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1
        
        # Step 2: make it circular
        tail.next = head
        
        # Step 3: find new tail
        k = k % n
        steps = n - k - 1
        new_tail = head
        
        for _ in range(steps):
            new_tail = new_tail.next
        
        # Step 4: break the circle
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head