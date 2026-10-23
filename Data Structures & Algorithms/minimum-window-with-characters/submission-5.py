class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ssize = len(s)
        tsize = len(t)
        smap = dict()
        tmap = dict()
        first = 0
        last = ssize + 1

        if ssize<tsize:
            return ""

        low = 0
        high = 0

        for char in t:
            tmap[char] = tmap.get(char,0)+1

        need = len(tmap)                          # CHANGE 1
        have = 0                                  # CHANGE 1
        
        while high!=ssize:

            if s[high] in tmap:
                smap[s[high]] = smap.get(s[high],0)+1
                if smap[s[high]] == tmap[s[high]]:    # CHANGE 2
                    have += 1

            while have == need:                       # CHANGE 3 (all() hata diya)
                if high-low+1 < last-first:
                    first = low
                    last = high+1

                if s[low] in tmap:
                    smap[s[low]]-=1
                    if smap[s[low]] < tmap[s[low]]:   # CHANGE 4
                        have -= 1
                low+=1   

            high+=1

        return "" if last > ssize else s[first:last]