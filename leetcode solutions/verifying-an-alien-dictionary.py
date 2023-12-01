class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {}
        for i in range(len(order)):
            d[order[i]] = i
        def check(word_1, word_2):
            for i in range(min(len(word_1), len(word_2))):
                if d[word_1[i]] > d[word_2[i]]:
                    return False
                elif d[word_1[i]] < d[word_2[i]]:
                    return True
            if len(word_1) <= len(word_2):
                return True
            return False
        for i in range(1,len(words)):
            word_1 = words[i-1]
            word_2 = words[i]
            if check(word_1, word_2):
                continue
            else:
                return False
        return True