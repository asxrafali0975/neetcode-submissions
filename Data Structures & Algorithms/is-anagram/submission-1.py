class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = dict({})
        for char in s:
            if hashmap.get(char):
                hashmap[char]+=1
            else:
                hashmap[char] = 1
        
        for char in t:
            if hashmap.get(char):
                hashmap[char]-=1
                if hashmap[char]==0:
                    del hashmap[char]     

            else:
                return False

        if len(hashmap)==0:
            return True
        return False


        