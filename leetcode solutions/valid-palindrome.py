class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        new_string=""
        for letter in s:
            if letter.isalnum():
                new_string+=letter
        return new_string==new_string[::-1]