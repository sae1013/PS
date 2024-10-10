class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        # 스택에 인덱스를 내림차순으로 저장
        stack = []
        for i in range(len(nums)):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)

        max_width = 0
        # 배열을 뒤에서부터 순회하며 최대 너비를 갱신
        for j in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                max_width = max(max_width, j - stack.pop())
        
        return max_width
