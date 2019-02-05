class Solution:
    def twoSum(self, numbers: 'List[int]', target: 'int') -> 'List[int]':
        left, right= 0, len(numbers)-1
        print(left,right)
        
        while(numbers[left]+numbers[right]!=target):
            if numbers[left] + numbers[right] < target:
                left = left+1
            else:
                right = right -1
        return [left+1, right+1]