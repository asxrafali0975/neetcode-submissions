class Solution:
    def isPalindrome(self, s: str) -> bool:
        news = ""
        for char in s:
            if char.isalnum():
                news+=char
        size = len(news)

        high = size-1
        low = 0
        news = news.lower()

        while low<=high:
            if news[low]!=news[high]:
                return False
            low+=1
            high-=1
        return True
        