from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs = []
        letter_logs = []
        for log in logs:
            if log.split()[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        for i in range(1, len(letter_logs)):
            value = letter_logs[i]
            j = i-1
            while j >= 0:
                if self.compareLog(letter_logs[j], value) > 0:
                    letter_logs[j+1] = letter_logs[j]
                else:
                    break
                j -= 1
            letter_logs[j+1] = value
        return letter_logs + digit_logs

    def compareLog(self, l1: str, l2: str) -> int:
        if l1 == l2:
            return 0
        idx1 = l1.find(' ')
        idx2 = l2.find(' ')
        id1 = l1[0:idx1]
        id2 = l2[0:idx2]
        letters1 = l1[idx1+1:]
        letters2 = l2[idx2+1:]
        if letters1 < letters2:
            return -1
        elif letters1 > letters2:
            return 1
        else:
            if id1 < id2:
                return -1
            elif id1 > id2:
                return 1
            else:
                return 0

logs = Solution().reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"])
print(logs)
