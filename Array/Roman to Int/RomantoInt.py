class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbol = {'I':1, 'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        summ =0
        prev='A'
        
        for letter in s:
            if letter in symbol:
                print(letter)
                if (letter =='V' or letter =='X') and prev =='I':
                    summ += symbol[letter] - 2*symbol[prev]
                    print('1',summ)
                elif (letter =='L' or letter =='C') and prev =='X':
                    summ += symbol[letter] - 2*symbol[prev]
                    print('2',summ)
                elif (letter =='D' or letter =='M') and prev =='C':
                    summ += symbol[letter] - 2*symbol[prev]
                    print('3',summ)
                else:
                    summ +=symbol[letter]
                    print('4',summ)
                prev = letter
        return summ