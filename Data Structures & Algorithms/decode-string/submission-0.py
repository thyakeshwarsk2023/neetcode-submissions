class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_string = ""
        curr_k = 0

        for char in s:
            if char.isdigit():
                curr_k = curr_k * 10 + int(char)

            elif char == '[':
                stack.append(curr_string)
                stack.append(curr_k)
                curr_string = ""
                curr_k  = 0
            elif char == ']':
                prev_k = stack.pop()
                prev_string = stack.pop()
                curr_string = prev_string + curr_string * prev_k
            else:
                curr_string += char

        return curr_string                    

        