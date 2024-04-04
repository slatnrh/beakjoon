import sys
input = sys.stdin.readline

# 기존 방정식 입력
formula = list(input())
# 후위 표기식으로 출력(pop을 이용)
stack = []
# 최종 결과 출력
rslt = ''

for f in formula:
    # isalpha: 문자열인지 판단(문자열이면 True, 아니면 False)
    if f.isalpha():
        # 알파벳이 아닌 문자가 나올 때까지 rslt에 +
        rslt += f
    else:
        # '('를 받으면 stack에 append
        if f == '(':
            stack.append(f)
        # '*' or '/'를 받으면
        elif f == '*' or f == '/':
            # '*' or '/'이 나올때까지 rslt에 +
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                rslt += stack.pop()
            # stack에 append(후위표기식이기 때문에)
            stack.append(f)
        # '+' or '-'를 받으면
        elif f == '+' or f == '-':
            # '('를 받을 때까지 rslt에 +
            while stack and stack[-1] != '(':
                rslt += stack.pop()
            # stack에 append(후위표기식이기 때문에)
            stack.append(f)
        # ')'를 받으면
        elif f == ')':
            # '('를 받을 때까지 rslt에 +
            while stack and stack[-1] != '(':
                rslt += stack.pop()
            # stack에 append(후위표기식이기 때문에)
            stack.pop()

while stack:
    rslt += stack.pop()
print(rslt)