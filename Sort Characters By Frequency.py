class Solution:
    def frequencySort(self, s: str) -> str:
        dictionary = Counter(s)
        dictinary = dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))
        ans = ''.join([char * count for char, count in dictinary.items()])
        return ans