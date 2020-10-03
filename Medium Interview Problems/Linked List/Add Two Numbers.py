class ListNode(object):
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution(object):
    def addTwoNumbers(self,l1,l2):

#        print('')
#        print('inside function...')

        #Declare pointers for traversal. Added for clarity
        p1 = l1
        p2 = l2

        #Declare Current carry over
        currentCarry = 0

        #Declare cur to help traverse and add nodes to new lists.
        #Declare head variable to be head of the list.
        head = cur = ListNode(0)

        #Iteration condition
        while p1 or p2 or currentCarry:

#            print(p1.val , p2.val , currentCarry);

            #determine current variable and carry over
            currentVal = currentCarry
            currentVal += 0 if p1 is None else p1.val;
            currentVal += 0 if p2 is None else p2.val;
            if currentVal >= 10:
                currentVal = (currentVal % 10)
                currentCarry = 1
            else:
                currentCarry = 0

#            print(currentVal, currentCarry)

            #Add current value as it will always be 1
            cur.next = ListNode(currentVal)
            cur = cur.next

            #Add base cases for iterating linked lists.
            if p1 is None and p2 is None:
                break
            elif p1 is None:
                p2 = p2.next
            elif p2 is None:
                p1 = p1.next
            else:
                p1 = p1.next
                p2 = p2.next
            
#        print('existing')
#        print('')

        return head.next

