class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len, p_len, p_idx, s_idx, p_star, s_backtrack = len(s), len(p), 0, 0, -1, -1
        
        while s_idx < s_len:
            if p_idx < p_len and p[p_idx] in ['?', s[s_idx]]:
                p_idx += 1
                s_idx += 1
            elif p_idx < p_len and p[p_idx] == '*':
                p_star = p_idx
                s_backtrack = s_idx
                p_idx += 1
            else: #elif p_idx == p_len or p[p_idx] != s[s_idx]:
                if p_star == -1:
                    return False
                else:
                    #backtrack
                    p_idx = p_star + 1
                    s_idx = s_backtrack + 1
                    s_backtrack = s_idx

        return all(p[idx] == '*' for idx in range(p_idx, p_len))
