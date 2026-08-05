class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # If either string is '0', the result is '0'
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        # The maximum possible length of the product string is m + n
        res = [0] * (m + n)
        
        # Iterate over both strings from right to left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Multiply the current digits
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                
                # Positions in the result array
                p1, p2 = i + j, i + j + 1
                
                # Add the multiplication result to the current value at p2
                total = mul + res[p2]
                
                # Update the result array
                res[p2] = total % 10
                res[p1] += total // 10
                
        # Skip leading zeros
        start = 0
        while start < len(res) and res[start] == 0:
            start += 1
            
        # Convert the result array back to a string
        return "".join(map(str, res[start:]))
