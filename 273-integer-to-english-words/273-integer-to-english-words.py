class Solution:
    def numberToWords(self, num: int) -> str:
        if not num: return "Zero"
        one = {
                1: 'One',
                2: 'Two',
                3: 'Three',
                4: 'Four',
                5: 'Five',
                6: 'Six',
                7: 'Seven',
                8: 'Eight',
                9: 'Nine'
            }
        
        two_less_than_20 = {
                10: 'Ten',
                11: 'Eleven',
                12: 'Twelve',
                13: 'Thirteen',
                14: 'Fourteen',
                15: 'Fifteen',
                16: 'Sixteen',
                17: 'Seventeen',
                18: 'Eighteen',
                19: 'Nineteen'
            }
        
        ten = {
                2: 'Twenty',
                3: 'Thirty',
                4: 'Forty',
                5: 'Fifty',
                6: 'Sixty',
                7: 'Seventy',
                8: 'Eighty',
                9: 'Ninety'
            }
        
        def two(num):
            if num<10:
                return one[num]
            elif num<20:
                return two_less_than_20[num]
            else:
                tenner = num//10
                rest = num-tenner*10
                return ten[tenner]+ ((' '+one[rest]) if rest else '')
        
        def three(num):
            hundred = num//100
            rest=num-hundred*100
            if hundred:
                return one[hundred]+' '+'Hundred'+((' '+two(rest)) if rest else '')
            else: return two(num)
        
        billion = num//pow(10,9)
        million = (num - billion*pow(10,9))//pow(10,6)
        thousand = (num - billion*pow(10,9) - million*pow(10,6))//1000
        rest = num%1000
        res = ''
        if billion:
            res += three(billion)+' '+'Billion'+' '
        if million:
            res+= three(million)+' '+'Million'+' '
        if thousand:
            res+= three(thousand)+' '+'Thousand'+ ' '
        if rest:
            res+= three(rest)
        
        return res.rstrip(' ')
                
            