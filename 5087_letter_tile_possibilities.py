class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = set()
        i = 1
        while i <= len(tiles):
            self.recurse('', tiles, res, i)
            i += 1
        return len(res)

    def recurse(self, used: str, tiles: str, set: set, size: int):
        if len(used) == size:
            set.add(used)
            return
        remains = self.subtract(used, tiles)
        for c in remains:
            self.recurse(used + c, tiles, set, size)


    def subtract(self, used: str, tiles: str) -> str:
        r = tiles
        for c in used:
            r = r.replace(c, '', 1)
        return r


print(Solution().numTilePossibilities('AAABBC'))
