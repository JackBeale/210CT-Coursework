import unittest
class Node(object):
      def __init__(self, value):
          self.value=value
          self.next=None
          self.prev=None
 #Function which creates a value to be added.#
class List(object):
      def __init__(self):
          self.head=None
          self.tail=None
      def insert(self,n,x):
          #Not actually perfect: how do we prepend to an existing list?
          if n!=None:
              x.next=n.next
              n.next=x
              x.prev=n
              #Above applied to if its the only value in the list.#
              if x.next!=None:
                  x.next.prev=x              
          if self.head==None:
              self.head=self.tail=x
              x.prev=x.next=None
          elif self.tail==n:
              self.tail=x
      def display(self):
          values=[]
          n=self.head
          while n!=None:
              values.append(str(n.value))
              n=n.next
          print ("List:",",".join(values))
          return ','.join(values)
          #Outputs the numbers seperated by commas.#
      def delDouble(self):
            self =  nxt = self.head
            while self is not None:
                  #while you are not at the end of the list do the following.#
                  while nxt.next is not None:
                        if nxt.next.value == self.value:
                              nxt.next = nxt.next.next
                        else:
                              nxt = nxt.next
                  self = nxt = self.next
      #The above function will remove duplicate values from the linked list.#

      #Displays the above nodes which will be added to the list.#

class UNITTESING (unittest.TestCase):
      def testDoublesInList(self):
            if __name__ == '__main__':
                  l=List()
                  l.insert(None, Node(4))
                  l.insert(l.head,Node(2))
                  l.insert(l.head,Node(6))
                  l.insert(l.head,Node(8))
                  l.insert(l.head,Node(6))
                  l.insert(l.head,Node(8))
                  l.delDouble()
                  l.display()
            self.assertEqual(l.display(),"4,8,6,2")

      def testThreeOfANumber(self):
            l=List()
            l.insert(None, Node(4))
            l.insert(l.head,Node(2))
            l.insert(l.head,Node(6))
            l.insert(l.head,Node(8))
            l.insert(l.head,Node(6))
            l.insert(l.head,Node(8))
            l.insert(l.head,Node(8))
            l.delDouble()
            l.display()
            self.assertEqual(l.display(),"4,8,6,2")
            
      def testNoDoublesInList(self):
            l=List()
            l.insert(None, Node(1))
            l.insert(l.head,Node(5))
            l.insert(l.head,Node(4))
            l.insert(l.head,Node(3))
          
            
            l.delDouble()
            l.display()
            self.assertEqual(l.display(),'1,3,4,5')
if __name__=='__main__':
      unittest.main()
##
