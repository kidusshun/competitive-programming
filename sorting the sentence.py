def sortSentence(s: str) -> str:
       arr=s.split(' ')
       arr.sort()
       new=[None]*len(arr)
       for word in arr:
           index=int(word[len(word)-1])
           new[index-1]=word[:len(word)-1]
       s=' '.join(new)
       return s
print(sortSentence("Myself2 Me1 I4 and3"))