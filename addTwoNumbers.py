class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pointer1 = l1.next
        pointer2 = l2.next
        if pointer1 == None and pointer2 == None:

            carry = int((l1.val+l2.val)/10)
            result = ListNode((l1.val+l2.val)%10)
            if carry >0:
                carryResult = ListNode(carry)
                result.next = carryResult
            return result
        else:
            if pointer1 ==None:
                l1.next = ListNode(0)
            elif pointer2 ==None:
                l2.next = ListNode(0)
            result = ListNode((l1.val+l2.val)%10)
            carry = int((l1.val+l2.val)/10)
            if carry >0 :
                l1.next.val=l1.next.val+carry
            result.next = self.addTwoNumbers(l1.next,l2.next)
            return result
