class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        my_list = []

        for i in range(len(number)):
            if number[i] == digit:
                my_list.append(int(number[:i] + number[i+1:]))
        
        my_list.sort()

        return str(my_list[-1])
