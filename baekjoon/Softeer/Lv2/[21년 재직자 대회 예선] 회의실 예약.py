import sys
input = sys.stdin.readline

s = input().rstrip()
result = ''

for i in range(len(s) - 1):
    result += s[i]
    if s[i] == '(' and s[i+1] == ')':
        result += '1'
    elif s[i] == ')' and s[i+1] == '(':
        result += '+'
result += s[-1]
print(result)