class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            num = len(string)
            res += str(num) + "#" + string
        return res
    def decode(self, s: str) -> List[str]:
        start = 0
        if not str:
            return [""]
        res = []
        while start < len(s):
            numIdx = ""
            while s[start] != "#":
                numIdx += s[start]
                start += 1
            start += 1
            end = start + int(numIdx)
            res.append(s[start:end])
            start = end
        return res