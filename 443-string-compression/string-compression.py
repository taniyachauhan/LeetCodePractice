class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        count = 1
        
        for read in range(1, len(chars) + 1):
            if read < len(chars) and chars[read] == chars[read - 1]:
                count += 1
            else:
                chars[write] = chars[read - 1]
                write += 1
                
                if count > 1:
                    for digit in str(count):
                        chars[write] = digit
                        write += 1
                
                count = 1
        
        return write
            
                




