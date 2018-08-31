class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        add =0
        present_nums =[]
        while n!=1:
            add=0
            while n: #repeat for each number
                rem=n%10
                add +=rem*rem
                n=n//10
            add+=n*n
            if add not in present_nums: #check duplicates
                present_nums.append(add)
            else:
                return False
            n = add
       