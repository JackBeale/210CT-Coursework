import unittest

#The following program will output a sentance
#With the words in the correct order
#But the words will be backwards.
def Mirror(word):
    Reverse = ""
    if (len(word) ==1):
        return word
    else:
        #print(word[::-1])
        Reverse+=word[::-1]
        print(Reverse, end=' ')
        return Mirror
    
sentence = "split the string recursivly"
for word in sentence.split():
    Mirror(word)

class UNITTESTING(unittest.TestCase):
      def MirrorStringInput(self):
            if __name__ == '__main__':
                sentence = "split the string recursivly"
            self.assertEqual(Mirror(),"ylvisrucer gnirts eht tlips")


if __name__=='__main__':
      unittest.main()