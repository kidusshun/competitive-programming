class Solution:
    def fizzBuzz(self, n: int):
        lst=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                lst.append("FizzBuzz")
            elif i%3==0 and i%5!=0:
                lst.append("Fizz")
            elif i%3!=0 and i%5==0:
                lst.append("Buzz")
            else:
                lst.append(str(i))
        return lst
