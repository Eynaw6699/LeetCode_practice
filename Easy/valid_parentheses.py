class Solution:
    @staticmethod
    def isValid(s: str) -> bool:
        l = list()
        dictionary = {'}': '{', ')': '(', ']': '['}
        b_open = dictionary.values()

        for b in s:
            if b in b_open:
                l.append(b)
            else:
                # check if l list is not empty and the last element matches, then delete from l list
                if len(l) > 0 and l[-1] == dictionary[b]:
                    l.pop()
                else:
                    return False

        return len(l) == 0


if __name__ == "__main__":
    S = "()"
    print(Solution.isValid(s=S))
    S_1 = "([)]"
    print(Solution.isValid(s=S_1))
