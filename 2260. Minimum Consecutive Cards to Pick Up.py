class Solution:
    def findSmallestGap(self, lst):
        lst.sort()
        new_list = []
        for i in range(len(lst) - 1):
            new_list.append(lst[i+1] - lst[i])
        new_list.sort()
        return new_list[0] + 1
        
            
    
    def minimumCardPickup(self, cards: List[int]) -> int:
        my_dict = {}
        
        for index in range(len(cards)):
            if cards[index] in my_dict.keys():
                my_dict[cards[index]].append(index)
            else:
                my_dict[cards[index]] = [index]
                
        current = len(cards)+1
        for key in my_dict:
            if len(my_dict[key]) > 1:
                if self.findSmallestGap(my_dict[key]) < current:
                    current = self.findSmallestGap(my_dict[key])
                    
        if current == len(cards) + 1:
            current = -1
        
        return current
        
