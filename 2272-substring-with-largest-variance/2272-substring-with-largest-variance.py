class Solution:
    def largestVariance(self, s: str) -> int:
        from collections import defaultdict

        char_list = defaultdict(list)
        for i,char in enumerate(s):
            char_list[char].append(i)
        
        best_ans = 0
        for target in char_list.keys():
            for small_char in char_list.keys():
                if target != small_char:
                    char_array = char_list[small_char]
                    target_array = char_list[target]
                    i = 0
                    j = 0
                    target_count = 0
                    char_count = 0
                    while i < len(target_array) and j < len(char_array):
                        if char_array[j] < target_array[i]:
                            char_count += 1
                            j += 1
                            if char_count > target_count:
                                char_count = 0
                                target_count = 0
                        else:
                            target_count += 1
							## since the most recent char is target, no need to keep small char around, 
							## in our final answer we always assume at least one char_count because we know it's in the array
                            if target_count-char_count==0: 
                                target_count = 1
                                char_count = 0
                            best_ans = max(best_ans,target_count-max(char_count,1))
                            i += 1
                    if i < len(target_array):
                        best_ans = max(best_ans,target_count-max(char_count,1)+len(target_array)-i)
        return best_ans