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
                nums.append(int(nums.pop() / di))
            else:
                nums.append(int(i))
        
        return nums[0]