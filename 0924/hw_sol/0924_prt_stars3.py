"""
3. loop문 연습3 - 별 출력하기

아래 모양대로 출력을 해 보세요.

*****
****
***
**
*

"""

def prt_stars():
    for i in range(5):
        print('*' * (5 - i))

prt_stars()

