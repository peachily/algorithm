# 파이썬 자료구조 deque의 메서드 연습 파일입니다.
# https://devdocs.programmers.co.kr/python~3.8/
from collections import deque

def main():
    # 정적 입력
    data = [10, 20, 30]
    q = deque()
  

    # 1️. data의 숫자를 순서대로 큐에 넣어라.
    for x in data:
        q.append(x)   # 뒤쪽에 x 추가

    # 2️. 큐 맨 앞의 값을 꺼내 변수 front에 저장하고 출력하라.
    front = q.popleft()
    
    print("popleft:", front)

    # 3️. 큐 맨 앞에 5를 추가하고, 맨 뒤의 값을 꺼내 변수 back에 저장하라.
    q.appendleft(5)      # 앞쪽에 5 추가
    back = q.pop() # 뒤쪽에서 꺼내기
    print("appendleft+pop:", back)

    # 4️. 큐의 현재 길이를 출력하라.
    size = len(q)
    print("length:", size)

if __name__ == "__main__":
    main()