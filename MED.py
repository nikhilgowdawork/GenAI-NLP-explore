''' USING NUMPY '''

import numpy as np
def min_edit_distance(str1, str2):
    m, n = len(str1), len(str2)
    dp = np.zeros((m + 1, n + 1), dtype=int)
    
    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = i # Deletion cost
    for j in range(n + 1):
        dp[0][j] = j # Insertion cost
    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] # No cost if same
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], # Deletion
                dp[i][j - 1], # Insertion

    dp[i - 1][j - 1]) # Substitution
    return dp[m][n]

# Test cases
pairs = [
("kitten", "sitting"), # Multiple edits
("flaw", "lawn"), # Reordering and substitution
("hello", "helo"), # Deletion
("example", "exampel"), # Typo swap
("abcdef", "azced") # Mix of edits
]

for s1, s2 in pairs:
    print(f"Edit Distance between '{s1}' and '{s2}': {min_edit_distance(s1, s2)}")



''' USING NLTK'''


    
'''
import nltk
from nltk.metrics import edit_distance

def test_med(str1, str2):
    # Compute and print the Minimum Edit Distance between two strings.

    distance = edit_distance(str1, str2)
    print(f"Edit Distance between '{str1}' and '{str2}': {distance}")

# Test cases with different types of variations
test_cases = [
("kitten", "sitting"), # Substitutions, Insertions
("flaw", "lawn"), # Substitutions
("intention", "execution"), # Multiple edits
("hello", "helo"), # Deletion

("abcdef", "azced"), # Mix of operations
("example", "exampel") # Typo swap
]

for str1, str2 in test_cases:
    test_med(str1, str2)'''