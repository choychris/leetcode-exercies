from solution_33 import Solution
from solution_33 import BinarySearchSolution

def tests():
  # assert Solution().search([4,5,6,7,0,1,2], 0) == 4

  # assert Solution().search([4,5,6,7,0,1,2], 3) == -1

  # assert Solution().search([6,7,0,1,2,4,5], 3) == -1

  assert BinarySearchSolution().search([4,5,6,7,0,1,2], 0) == 4

  assert BinarySearchSolution().search([4,5,6,7,0,1,2], 3) == -1

  assert BinarySearchSolution().search([1,3,0], 1) == 0