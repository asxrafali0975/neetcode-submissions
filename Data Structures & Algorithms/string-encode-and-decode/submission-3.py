class Solution:

    def encode(self, strs: List[str]) -> str:
        size  = len(strs)
        if size==0:
            return ""

        string = ""

        for s in strs:
            if string=="" and s=="":
                string+='-'
            
            elif string=="" and s!="":
                string+=s

            elif string!="" and s=="":
                string+="ASH"
                string+='-'

            elif string!="" and s!="":
                string+="ASH"
                string+=s
        return string
        




    def decode(self, s: str) -> List[str]:
        size  = len(s)
        if size==0:
            return []

        listt = s.split("ASH")
        for i in range(len(listt)):
            if listt[i]=='-':
                listt[i]=""
        return listt
        
