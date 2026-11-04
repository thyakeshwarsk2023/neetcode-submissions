class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        current_w = 0
        for i in range(k):
            if blocks[i] == "W":
                current_w += 1
        min_ops = current_w
        if min_ops == 0:
            return 0 

        for i in range(k,len(blocks)):
            if blocks[i] == "W":
                current_w += 1

            if blocks[i-k] == "W":
                current_w -= 1

            if current_w < min_ops:
                min_ops = current_w
                if min_ops == 0:
                    return 0

        return min_ops            

