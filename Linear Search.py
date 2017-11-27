import unittest

#the following program will allow a user to search for a number
#In a list linearly.
List = [1,2,5,8,13,44]
SearchValue = int(input("Please enter a value to search for?:"))



#Below is the recursive function to search for the users inputtd value.

def Check(List, SearchValue):
    In_List = False
    increment = 0
    for increment in range(len(List)):
        if(List[increment] == SearchValue):
            In_List = True
            print("FOUND:", List[increment])
            break
    if(In_List == False):
        print("NOT IN LIST")
#The final line is the function call.
Check(List, SearchValue)


class UNITTESING(unittest.TestCase):
    def Check(self):
        if __name__ == '__main__':
            SearchValue = 44
        self.assertEqual(Check(), "FOUND:", 5)

    def Check(self):
        if __name__ == '__main__':
            SearchValue = 7
        self.assertEqual(Check(), "NOT IN LIST")


if __name__=='__main__':
    unittest.main()
