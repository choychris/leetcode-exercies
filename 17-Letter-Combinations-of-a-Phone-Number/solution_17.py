

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
      if (len(digits) == 0):
        return []
      
      numberDict = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
      }

      head = []
      for num in digits:
        words = numberDict[num]
        if(len(head) == 0):
          head = [w for w in words]
        else:
          newHead = []
          for w in words:
            for h in head:
              newHead.append(h + w)
          head = newHead
      
      return head

          