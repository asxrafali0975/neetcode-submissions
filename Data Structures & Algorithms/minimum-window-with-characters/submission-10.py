class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ssize = len(s)
        tsize = len(t)

        if ssize < tsize:
            return ""

        flag = 0

        low = 0
        high = 0

        start = 0
        end = 0

        tdict = dict()
        sdict = dict()

        for key in t:
            tdict[key] = tdict.get(key,0)+1
        
        for high in range(ssize):
            
            if s[high] in tdict:
                
                sdict[s[high]] = sdict.get(s[high], 0) + 1

            
            while self.is_valid(sdict, tdict):
                if flag ==0:
                        #means first time
                    start = low
                    end = high
                    flag =1
                else:
                    if high-low < end-start:
                        end = high
                        start = low
                        #now shrink to max we can
                        
                    

                if s[low] in tdict:
                    sdict[s[low]]-=1
                    if sdict[s[low]]==0:
                        del sdict[s[low]]

                low+=1

        if flag==0:
            return ""
        return s[start:end+1]

    def is_valid(self,sdict, tdict):
        for key, value in tdict.items():
            if sdict.get(key, 0) < value:
                return False
        return True




            
            



        
        