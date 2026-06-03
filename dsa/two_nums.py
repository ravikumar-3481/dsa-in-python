class TwoNums:
    def __init__(self, num):
         self.num = num   

    def two_nums(self, target):
              s = set()
              for num in self.num:
                  complement = target - num
                  if complement in s:
                      return True
              return False
    
tn = TwoNums()
arr = [2, 3, 4, 5, 1, 6]
target = 6
print(tn.two_nums(arr, target))
