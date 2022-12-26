class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dictionary = {}
        for i in range(len(order)):
            dictionary[order[i]] = i
        
        for word_counter in range(len(words) - 1):
            current_word = words[word_counter]
            next_word = words[word_counter + 1]

            for i in range(len(current_word)):
                if i >= len(next_word):
                    return False
                elif dictionary[current_word[i]] < dictionary[next_word[i]]:
                    break
                elif dictionary[current_word[i]] == dictionary[next_word[i]]:
                    continue
                elif dictionary[current_word[i]] > dictionary[next_word[i]]:
                    return False
            
        return True
