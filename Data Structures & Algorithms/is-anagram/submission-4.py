class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = []
        arr1 = []
        s = s.lower()
        t = t.lower()
        for i in range(0,len(s)):
            arr.append(ord(s[i]) - ord('a'))
        for j in range(0,len(t)):
            arr1.append(ord(t[j]) - ord('a'))
        
        arr = sorted(arr)
        arr1 = sorted(arr1)

        return arr==arr1