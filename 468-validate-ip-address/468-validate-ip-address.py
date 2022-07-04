import re
class Solution:
    def validIPAddress(self, IP: str) -> str:        
        if IP.count(".")==3:
            #check if IPv4
            chunks = IP.split(".")
            for chunk in chunks:
                if len(chunk)==1:
                    if not all(c.isdigit() for c in chunk): return "Neither"
                else:
                    if not chunk.isdigit() or chunk[0]=='0' or int(chunk)>255:
                        return "Neither"
                    
            return "IPv4"
        elif IP.count(":")==7:
            #check if IPv6
            hexdigits = "0123456789abcdefABCDEF"
            chunks = IP.split(':')
            for chunk in chunks:
                if not chunk or len(chunk)>4 or not all(c in hexdigits for c in chunk):
                    return "Neither"
            
            return "IPv6"
                    
        else:
            return "Neither"