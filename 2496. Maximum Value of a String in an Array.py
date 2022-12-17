class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        returning = 0
        for item in strs:
            if item.isdigit():
                current = int(item)
            else:
                current = len(item)
            if current > returning:
                returning = current
        return returning
