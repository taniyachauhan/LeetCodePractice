class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            temp = ""
            base = 1
            curr_num = 0
            if char == ']':
                while stack[-1] != '[':
                    temp = stack.pop()+temp

                stack.pop()
                while stack and stack[-1].isdigit():
                    curr_num = curr_num + int(stack[-1])*base
                    base *= 10
                    stack.pop()
                stack.append(curr_num * temp)
                curr_num = 0
                temp = ""
                base = 1

            else:
                stack.append(char)

        return "".join(stack)

        