

def _lcs(a, i, b, j, c, k, memo):
    if i == 0 or j == 0 or k == 0:
        return 0
    
    if (i, j, k) not in memo:
        if a[i-1] == b[j-1] == c[k-1]:
            memo[(i, j, k)] = 1 + _lcs(a, i-1, b, j-1, c, k-1, memo)
        else:
            memo[(i, j, k)] = max(
                _lcs(a, i-1, b, j, c, k, memo),
                _lcs(a, i, b, j-1, c, k, memo),
                _lcs(a, i, b, j, c, k-1, memo),
            )

    return memo[(i, j, k)]


class Solution:
    def solve(self, a, b, c):
        memo = {}
        return _lcs(a, len(a), b, len(b), c, len(c), memo)
