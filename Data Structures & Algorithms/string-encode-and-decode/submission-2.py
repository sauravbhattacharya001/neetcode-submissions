class Solution:

    def encode(self, strs: List[str]) -> str:
        lengths=[]
        result = []

        if not strs:
            return "EMPTY_LIST"

        for string in strs:
            result.append(str(len(string)))
            result.append(",")
        result.pop()
        result.append("#")

        for string in strs:
            result.append(string)

        return "".join(result)

    def decode(self, s: str) -> List[str]:

        if s == "EMPTY_LIST":
            return []

        counts = s.split("#")[0]
        
        current_word_index=s.index("#") + 1
        
        result = []
        for count in counts.split(","):
            numcount = int(count)
            result.append(s[current_word_index:current_word_index+numcount])
            current_word_index += numcount

        return result