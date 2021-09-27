def check_quiz(s):
    if not 'ABC' in s:
        return 'ABC'
    elif not 'ARC' in s:
        return 'ARC'
    elif not 'AGC' in s:
        return 'AGC'
    else:
        return 'AHC'

S = [input() for _ in range(3)]
print(check_quiz(S))