class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashdict = dict()
        size = len(strs)
        finalanswer = []

        for index in range(size):
            sorted_word = "".join(sorted(strs[index]))
            if not hashdict.get(sorted_word):
                hashdict[sorted_word] = [index]
            else:
                hashdict[sorted_word].append(index)

        for keys in hashdict:
            value_list = hashdict[keys]
            answer = []

            for indexes in value_list:
                answer.append(strs[indexes])

            finalanswer.append(answer)

        return finalanswer


        