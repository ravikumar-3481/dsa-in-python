class MoveZero:
    def __init__(self, nums):
        self.num = nums

    def move_zero(self):
        count = 0
        for i in range(len(self.num)):
            if self.num[i] != 0:
                self.num[count] = self.num[i]
                count += 1
        while count < len(self.num):
            self.num[count] = 0
            count += 1
    
    def create_array(self):
        import random as rd
        size = rd.randint(10, 20)
        print("size:", size)
        percentage_zero = rd.randint(30, 70) / 100
        print("percentage of zeros:", percentage_zero)
        non_zero_arr = [rd.randint(0, 10) for _ in range(size)]
        zero_arr = [0] * int(size * percentage_zero)
        self.num = []
        for i in range(size):
            ele = rd.choice(non_zero_arr + zero_arr)
            if self.num.count(0) < (size*percentage_zero) or ele != 0:
                self.num.append(ele)
            else:
                while self.num.count(0) >= (size*percentage_zero):
                    ele = rd.choice(non_zero_arr + zero_arr)
                    if self.num.count(0) < (size*percentage_zero) or ele != 0:
                        self.num.append(ele)
                        break
        return self.num
    
  

arr = MoveZero([]).create_array()
print("original array:", arr)
mz = MoveZero(arr)
mz.move_zero()
print("array after moving zeros:", arr)
print("number of zeros:", arr.count(0))
print("number of non-zero elements:", len(arr) - arr.count(0))

print()
print("Testing two_nums function:")
target = int(input("Enter a target sum: "))
print("target:", target)
result = mz.two_nums(target)
print("two numbers sum to target:", result)
