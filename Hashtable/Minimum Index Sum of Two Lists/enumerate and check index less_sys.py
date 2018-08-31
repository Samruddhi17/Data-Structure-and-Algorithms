class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        index_sum = sys.maxint
        hashmap = {}
        res=[]
        
        for i,rest in enumerate(list1):
            if rest not in hashmap:
                hashmap[rest] =i
                
        for i,rest in enumerate(list2):
            if rest in hashmap:
                isum = i +hashmap[rest]
                if isum < index_sum:
                    index_sum =isum
                    res = [rest]	#for least match
                elif isum==index_sum:
                    index_sum =isum
                    res += [rest]	#more than one least matches
        return res