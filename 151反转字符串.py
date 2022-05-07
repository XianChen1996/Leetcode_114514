class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))

    #结论：split()的时候，多个空格当成一个空格；split(' ')的时候，多个空格都要分割，每个空格分割出来空。