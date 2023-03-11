# class Solution(object):
#     def deleteDuplicates(self, head):
#         if head == None or head.next == None:
#             return head
        
#         list = head
        
#         while(list.next!=None):
#             if list.val == list.next.val:
#                 list.next = list.next.next
#             else:
#                 list = list.next
        
#         return head

# head = [1, 1, 2, 3, 4, 4, 5, 5]
# # if head == None or head.next == None:
# #     print(head)
# # list = head

# # while (list.next != None):
# #     if list.val == list.next.val:
# #         lidt.next = list.next.next
# #     else:
# #         list = list.next
# # print(head)

# while head and head.next != None:
#     if head.next.val == head.val:
#         head.next = head.next.next
#     else:
#         head = head.next
#         print(head)


def remove(head):
    temp = head

    while temp.next != None:
        if temp.data == temp.next.data:
            temp.next = temp.next.next
        else:
            temp = temp.next 

    return head
head = [1, 1, 2, 3, 4, 4, 5, 5]


print(remove(head)