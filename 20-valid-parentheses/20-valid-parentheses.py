class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        types = {
            '(':')',
            '[':']',
            '{':'}'
        }
        for bracket in s:
            if bracket in ['(', '[', '{']:
                stack.append(types[bracket])
            elif bracket in [')', ']', '}']:
                if len(stack)==0 or bracket!=stack.pop():
                    return False
        return len(stack)==0
        