# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first_list = self.convert_into_list(l1)
        second_list = self.convert_into_list(l2)

        number1 = self.convert_into_number(first_list)
        number2 = self.convert_into_number(second_list)
        total = number1 + number2
        temp_list=list("".join(str(total)))
        temp=[int(temp_list[i]) for i in range(len(temp_list))]
        temp=temp[::-1]
        
        
        curr =dummy= ListNode(0)
        for i in range(len(temp)):
            curr.next = ListNode(temp[i])
            curr = curr.next
        return dummy.next


    def convert_into_list(self, linked_list):
        lst=[]
        curr = linked_list
        while curr:
            lst.append(curr.val)
            curr = curr.next
        return lst
    def convert_into_number(self, input_list):
        n = len(input_list)
        num = 0
        for i in range(n-1,-1,-1):
            num += int(input_list[i])*10**i
        return num
    



