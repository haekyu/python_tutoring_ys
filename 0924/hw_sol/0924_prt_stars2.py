"""
2. loop문 연습2 - 별 출력하기

아래 모양대로 출력을 해 보세요.

    *
   **
  ***
 ****
*****

힌트2) 띄어쓰기 하나를 출력하고 싶으면 print(' ') 을 하면 됩니다.
"""

def prt_stars():
    for i in range(1, 6):
        print(' ' * (5 - i) + '*' * i)

prt_stars()

