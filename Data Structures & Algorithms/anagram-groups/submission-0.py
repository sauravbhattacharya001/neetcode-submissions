class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for string in strs:
            srt = "".join(sorted(string))
            groups[srt].append(string)

        return list(groups.values())