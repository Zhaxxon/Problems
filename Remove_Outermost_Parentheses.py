# A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings,
# and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses
# strings.
#
# A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B,
# with A and B nonempty valid parentheses strings.
#
# Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are
# primitive valid parentheses strings.
#
# Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.
#
#
#
# Example 1:
#
# Input: "(()())(())"
# Output: "()()()"
# Explanation:
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
# Example 2:
#
# Input: "(()())(())(()(()))"
# Output: "()()()()(())"
# Explanation:
# The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
# After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
# Example 3:
#
# Input: "()()"
# Output: ""
# Explanation:
# The input string is "()()", with primitive decomposition "()" + "()".
# After removing outer parentheses of each part, this is "" + "" = "".


class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        res = ""
        j = 0
        my_stack = []

        for i in range(len(S)):
            if my_stack and S[i] == ')':
                if len(my_stack) == 1:
                    my_stack.pop()
                    res += S[j+1:i]
                    j = i + 1
                else:
                    my_stack.pop()
            else:
                my_stack.append(S[i])

        return res