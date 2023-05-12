from dblList import Node
from dblList import DList
from dblList import Stack
from dblList import Queue
# ============================================================================================================================================================================================================================
st = Stack()

# ============================================================================================================================================================================================================================
def toList(st):
    # 빈칸을 제거한다.
    st = st.replace(" ","")
    return list(st)
def checkparenthese(st):
    tokens = toList(st)
    st = Stack()

    for item in tokens:
        # 왼족 괄호면 stack에 넣는다 st.push(item)
        lefts = "({[<"
        right = ")}]>"
        metched = "(){}[]<>"
        if item in lefts:
            st.push(item)
        # 오른족 괄호이면 stack의 top원소를꺼내서(pop) 매칭여부 확인한다.
        # 매칭이 안돼면 매칭오류 발생 stack 비어있으면 발생
        elif item in right:
            chk = st.pop() + item
            if chk in metched:
                print("metched: %s" % (chk))  # 정상결과 출력
                # pass
            else:
                print("ismetched: %s" % (chk))
                return
        else:  # 괄호가 아닌 문자이므로
            print("unKoum token: [%s]" % (item))
            return

    # for문 종료후 stack이 비여잇어야 정상 비어있지않으면 오류
    if not st.isEmpty():
        print("미완성 문자열 입니다.")
    else:
        print("perfect !!")
#=================================================================================================================
#input: 12   *(34*(3 /56))
#ouput: [12, *, (, 34, *, (, 3, /, 56, ), )]

# 수식문자열 (피연산자(임의길이)) 연산자(+,-,*,/) 괄호((,))로 구성관공식.
# 를 입력 받아 totken 으로 구분하여 totken 들를 담은 List를
def totokens(strInput):
    chList = toList(strInput)
    token = ""
    tokenList = []
    ops = "+-*/()"
    while chList:
        ch = chList.pop(0)
        if ch in ops:
            tokenList.append(ch)
        elif ch.isdigit():
            token += ch
            while chList:
                if chList[0].isdigit():
                    token += chList.pop(0)
                else:
                    break
            tokenList.append(token)
            token = ""
        else:
            pass
    return tokenList
# 중의 표기법 로 표현한 수식을 후의 표기법 으로 변환한 결과를 반환
def infix2postfix(strInput):
    stack = Stack()
    queue = Queue()
    ops = "+-*/"
    prec = {'(': 1, '+': 2, '-': 2, '*': 3, '/': 3}

    # 입력한 수식 문자열 을 수식 문자열 을 token 단위로 먼저 구분 한다.
    tokens = totokens(strInput)

    # 토큰 에 있는 항목 하나씩 가져와 처리 한다.
    while tokens:
        # 수는 queue 에 출력
        token = tokens.pop(0)
        if token.isdigit():
            queue.add(token)
        elif token in ops:
            while not stack.isEmpty() and prec[stack.peek()] >= prec[token]:
                queue.add(stack.pop())
            stack.push(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while not stack.isEmpty() and stack.peek() != '(':
                queue.add(stack.pop())
            if not stack.isEmpty() and stack.peek() == '(':
                stack.pop()

    # stack 에 있는 모든것 을 pop 하여 queue 에 저장
    while not stack.isEmpty():
        queue.add(stack.pop())
    return queue

#// ===========================================================================================================================================
# 중의 표기법 로 표현한 수식을 저장한 queue 넘겨주면
# stack 이용하여 계산하고 그결과값을 stack 생성
#// ===========================================================================================================================================
def stackCalculatur(queue):
    stack = Stack() #계산에활용할 stack 함수 -숫자
    while not queue.isEmpty():
        token = queue.remove()

        #token의 수 이면 stack 에저장
        if token.isdigit():
            stack.push(int(token))
        else:
        # 연산자 계산한뒤 결과를 다시 stack 에 저장
            b = stack.pop()
            a = stack.pop()
        #연산자 에종류에따른 게산을 하소 결과는 stack에저장
            if token == '+':
                stack.push(a+b)
            elif token == '-':
                stack.push(a-b)
            elif token == '*':
                stack.push(a*b)
            elif token == '/':
                stack.push(a/b)
            else:
                pass

    return stack.pop()








st = "((9 - (4 / 2 + 1)) * (5 * 2 - 2 )) +23-23"

q = infix2postfix(st)
print("후위표기법결과 : ",q)

r = stackCalculatur(q)
print("계산결과 : ",r**2)






# ============================================================================================================================================================================================================================
#ps = "([{ }[ ]] < >)"
#checkparenthese(ps)