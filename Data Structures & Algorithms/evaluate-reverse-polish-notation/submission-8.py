class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for i in tokens:
            if i == '+':
                nums.append(nums.pop() + nums.pop())
            elif i == '-':
                sml = nums.pop()
                nums.append(nums.pop() - sml)
            elif i == '*':
                nums.append(nums.pop() * nums.pop())
            elif i == '/':
                di = nums.pop()
                val = nums.pop()
                val2 = val / di
                nums.append(int(val2))
            else:
                nums.append(int(i))
        
        return nums[0]